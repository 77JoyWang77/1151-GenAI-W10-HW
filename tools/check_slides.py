"""檢查教學簡報是否「有根據」且「教學順序正確」。

每張 <section class="slide"> 需要：
  data-wiki="stem,stem"     這張投影片根據哪些 wiki 頁
  data-src="S1,S2"          引用哪些來源
  data-introduces="term"    (選填) 這張第一次解釋的名詞
  data-uses="term"          (選填) 這張用到、但需要先學過的名詞

用法：python tools/check_slides.py [slides.html|outline.json] [--outline outline.json]
  加 --outline 時，另外檢查 HTML 每張投影片的 data-wiki / data-src 是否跟大綱一致
"""
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

BASE = Path(__file__).parent.parent
WIKI = BASE / "llm-wiki" / "wiki"
args = sys.argv[1:]
outline_path = None
if "--outline" in args:
    k = args.index("--outline"); outline_path = Path(args[k + 1]); del args[k:k + 2]
target = Path(args[0] if args else BASE / "slides" / "index.html")

# 教學上必須涵蓋的 wiki 頁面
REQUIRED = ["overview", "wiki-accumulates-rag-rederives", "three-layers", "ingest", "query",
            "lint", "index-and-log", "failure-modes", "mitigations", "how-to-start"]
MAX_BULLETS = 6          # 一張投影片的條列上限（給初學者看）
NUM_RE = re.compile(r"(?<![A-Za-z\d.#])\d[\d,]*(?![\d])")
DATE_RE = re.compile(r"\d{4}-\d{2}(-\d{2})?")


def numbers(text):
    """去掉日期後的數字；個位數視為序號（第 1 步、2 / 3）不檢查"""
    return {n for n in NUM_RE.findall(DATE_RE.sub(" ", text)) if len(n) > 1}

pages = {p.stem: p.read_text(encoding="utf-8") for p in WIKI.rglob("*.md")}
pages_nodate = {k: DATE_RE.sub(" ", v) for k, v in pages.items()}


def page_sources(stem):
    m = re.search(r"^sources: \[(.*?)\]", pages[stem], re.M)
    return {s.strip() for s in m.group(1).split(",")} if m else set()


class Slides(HTMLParser):
    def __init__(self):
        super().__init__()
        self.slides, self.cur, self.depth = [], None, 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "section" and "slide" in (a.get("class") or ""):
            self.cur = {"attrs": a, "text": "", "li": 0}
            self.depth = 1
            return
        if self.cur is not None:
            if tag == "section":
                self.depth += 1
            if tag == "li":
                self.cur["li"] += 1
            if tag in ("script", "style"):
                self.cur["skip"] = True

    def handle_endtag(self, tag):
        if self.cur is None:
            return
        if tag in ("script", "style"):
            self.cur["skip"] = False
        if tag == "section":
            self.depth -= 1
            if self.depth == 0:
                self.slides.append(self.cur)
                self.cur = None

    def handle_data(self, data):
        if self.cur is not None and not self.cur.get("skip"):
            self.cur["text"] += data


def load(path):
    if path.suffix == ".json":
        out = []
        for s in json.loads(path.read_text(encoding="utf-8"))["slides"]:
            text = " ".join([s.get("title", "")] + s.get("points", []))
            out.append({"attrs": {"data-wiki": ",".join(s.get("wiki", [])),
                                  "data-src": ",".join(s.get("src", [])),
                                  "data-introduces": ",".join(s.get("introduces", [])),
                                  "data-uses": ",".join(s.get("uses", [])),
                                  "data-kind": s.get("kind", "")},
                        "text": text, "li": len(s.get("points", []))})
        return out
    p = Slides()
    p.feed(path.read_text(encoding="utf-8"))
    return p.slides


def split(v):
    return [x.strip() for x in (v or "").split(",") if x.strip()]


slides = load(target)
errors, warnings = [], []
known, covered = set(), set()

for i, s in enumerate(slides, 1):
    a = s["attrs"]
    kind = a.get("data-kind", "")
    wiki_refs, srcs = split(a.get("data-wiki")), set(split(a.get("data-src")))
    tag = f"slide {i:02d}"
    if not wiki_refs:
        errors.append(f"{tag}: 沒有標 data-wiki，看不出內容根據哪一頁")
    allowed = set()
    for w in wiki_refs:
        if w not in pages:
            errors.append(f"{tag}: data-wiki 指向不存在的頁面 {w}")
        else:
            covered.add(w)
            allowed |= page_sources(w)
    if wiki_refs and srcs - allowed:
        errors.append(f"{tag}: 引用 {sorted(srcs - allowed)}，但對應的 wiki 頁沒有這個來源（簡報自己加了 wiki 沒有的內容？）")
    # 數字必須出現在對應 wiki 頁
    wiki_nums = set().union(*(numbers(pages_nodate.get(w, "")) for w in wiki_refs)) if wiki_refs else set()
    if wiki_refs:
        for num in sorted(numbers(s["text"])):
            if num not in wiki_nums:
                errors.append(f"{tag}: 數字 {num} 不在 wiki 頁 {wiki_refs} 中")
    # 教學順序：用到的名詞要先介紹過
    intro = set(split(a.get("data-introduces")))
    for term in split(a.get("data-uses")):
        if term not in known and term not in intro:
            errors.append(f"{tag}: 用到「{term}」但前面還沒介紹")
    known |= intro
    if s["li"] > MAX_BULLETS:
        warnings.append(f"{tag}: {s['li']} 個條列，超過 {MAX_BULLETS}，初學者不好讀")

if outline_path:
    ref = load(outline_path)
    if len(ref) != len(slides):
        errors.append(f"張數不一致：大綱 {len(ref)} 張、HTML {len(slides)} 張")
    for i, (o, h) in enumerate(zip(ref, slides), 1):
        for key in ("data-wiki", "data-src"):
            if set(split(o["attrs"].get(key))) != set(split(h["attrs"].get(key))):
                errors.append(f"slide {i:02d}: {key} 跟大綱不一致（render 改動了根據）")

for w in REQUIRED:
    if w not in covered:
        errors.append(f"沒有任何投影片涵蓋必要頁面 {w}")

print(f"Slides check｜{target.name}｜{len(slides)} 張")
for e in errors:
    print("  ERROR  ", e)
for w in warnings:
    print("  WARN   ", w)
print("結果：", "PASS" if not errors else f"FAIL（{len(errors)} errors）", f"/ {len(warnings)} warnings")
sys.exit(1 if errors else 0)
