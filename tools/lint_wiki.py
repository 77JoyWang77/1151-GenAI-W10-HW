"""LLM Wiki lint：檢查 wiki/ 是否符合 AGENTS.md（v2）第 7 節的四類規則。

用法：python tools/lint_wiki.py [wiki 根目錄]，預設 llm-wiki
回傳碼 0 = 通過，1 = 有 error
"""
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent.parent / "llm-wiki")
WIKI = ROOT / "wiki"
RAW = ROOT / "raw"
SPECIAL = {"index", "log"}
REQUIRED_KEYS = ["title", "type", "sources", "updated", "tldr"]
PAGE_TYPES = {"source", "concept", "claim"}           # AGENTS.md 第 3 節：只有三種
QUOTE_RE = re.compile(r'^>\s*"(.+?)"\s*\[(S\d+)\]\s*$')
MAX_QUOTE_WORDS = 15
LINK_RE = re.compile(r"\[\[([a-z0-9\-]+)\]\]")
SRC_RE = re.compile(r"\[(S\d+(?:\s*,\s*S\d+)*)\]")

errors, warnings = [], []


def parse(path):
    text = path.read_text(encoding="utf-8")
    fm = {}
    body = text
    if text.startswith("---"):
        _, head, body = text.split("---", 2)
        for line in head.strip().splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip()
    return fm, body


NUM_RE = re.compile(r"(?<![A-Za-z\d.])\d[\d,]*(?![\d])")
DATE_RE = re.compile(r"\d{4}-\d{2}(-\d{2})?")
raw_cards = {p.name.split("-")[0]: p.read_text(encoding="utf-8") for p in RAW.glob("S*.md")}
raw_nums = {k: set(NUM_RE.findall(DATE_RE.sub(" ", v))) for k, v in raw_cards.items()}
raw_ids = set(raw_cards)


def raw_section(text, name):
    m = re.search(rf"^## {name}\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    return m.group(1) if m else ""


raw_quotes = {k: raw_section(v, "原句") for k, v in raw_cards.items()}
raw_rank = {k: int(m.group(1)) for k, v in raw_cards.items() if (m := re.search(r"^rank:\s*(\d)", v, re.M))}
for sid in sorted(raw_ids - set(raw_rank)):
    errors.append(f"raw/{sid}: frontmatter 缺少 rank（可信度）")
pages = {p.stem: p for p in WIKI.rglob("*.md")}
inbound = {stem: 0 for stem in pages}

for stem, path in sorted(pages.items()):
    rel = path.relative_to(ROOT)
    fm, body = parse(path)
    for target in LINK_RE.findall(body):
        if target not in pages:
            # log.md 只追加不改寫，舊紀錄提到已刪除的頁面是正常的
            (warnings if stem == "log" else errors).append(f"{rel}: 斷掉的連結 [[{target}]]")
        elif target != stem:
            inbound[target] += 1
    if stem in SPECIAL:
        continue
    # ① frontmatter
    ptype = fm.get("type", "")
    allowed_types = {"query-result"} if path.parent.name == "queries" else PAGE_TYPES
    if ptype and ptype not in allowed_types:
        errors.append(f"{rel}: type「{ptype}」不在允許的 {sorted(allowed_types)}")
    for k in REQUIRED_KEYS:
        if k not in fm or not fm[k]:
            errors.append(f"{rel}: frontmatter 缺少 {k}")
    declared = set(re.findall(r"S\d+", fm.get("sources", "")))
    # 每條 bullet 要有來源或標推論；「相關頁面」段落不檢查
    cited = set()
    section = ""
    sec_ranks = {}                                     # ④ 主張頁各段落引用到的 rank
    for n, line in enumerate(body.splitlines(), 1):
        if line.startswith("#"):
            section = line
            continue
        s = line.strip()
        # ③ 英文原句：逐字出現在該來源 raw 卡片的「## 原句」，且不超過 15 字
        if s.startswith(">") and '"' in s:
            q = QUOTE_RE.match(s)
            if not q:
                errors.append(f"{rel}:{n}: 原句格式應為 > \"...\" [S1] → {s[:40]}")
                continue
            quote, sid = q.groups()
            cited.add(sid)
            if len(quote.split()) > MAX_QUOTE_WORDS:
                errors.append(f"{rel}:{n}: 原句 {len(quote.split())} 字，超過 {MAX_QUOTE_WORDS} 字")
            if quote not in raw_quotes.get(sid, ""):
                errors.append(f"{rel}:{n}: 原句不在 raw/{sid} 的「## 原句」中 → {quote[:40]}")
            continue
        if not s.startswith("- ") or "相關頁面" in section:
            continue
        m = SRC_RE.findall(s)
        line_ids = set()
        for group in m:
            line_ids.update(x.strip() for x in group.split(","))
        cited |= line_ids
        if ptype == "claim" and line_ids:
            sec_ranks.setdefault(section.strip("# ").strip(), []).extend(raw_rank.get(i, 9) for i in line_ids)
        # ④ 只有產品文（rank 4）支持的說法要標（廠商觀點）
        if line_ids and all(raw_rank.get(i) == 4 for i in line_ids) and "（廠商觀點）" not in s and "相關頁面" not in section:
            errors.append(f"{rel}:{n}: 只引用產品文的說法要加「（廠商觀點）」→ {s[:40]}")
        if not m and "（推論）" not in s:
            errors.append(f"{rel}:{n}: bullet 沒有來源標記 → {s[:40]}")
        # 數字 grounding：bullet 裡的數字必須出現在它引用的 raw 卡片中
        if m:
            ids = {x.strip() for g in m for x in g.split(",")}
            allowed_nums = set().union(*(raw_nums.get(i, set()) for i in ids))
            claim = DATE_RE.sub(" ", SRC_RE.sub("", s))
            for num in NUM_RE.findall(claim):
                if num not in allowed_nums:
                    errors.append(f"{rel}:{n}: 數字 {num} 不在來源 {sorted(ids)} 的 raw 卡片中 → {s[:40]}")
    for sid in cited - raw_ids:
        errors.append(f"{rel}: 引用不存在的來源 {sid}")
    if cited - declared:
        errors.append(f"{rel}: 內文引用 {sorted(cited - declared)} 但 frontmatter sources 沒列")
    if declared - cited:
        warnings.append(f"{rel}: frontmatter 列了 {sorted(declared - cited)} 但內文沒引用")
    # ④ 主張頁：採信的一方可信度要比註記高（rank 小）
    if ptype == "claim":
        if "## 主張" not in body:
            errors.append(f"{rel}: 主張頁缺少「## 主張」段落")
        main, note = sec_ranks.get("主張", []), sec_ranks.get("註記", [])
        if main and note and max(main) > min(note):
            errors.append(f"{rel}: 「主張」引用的來源 rank {max(main)} 比「註記」的 rank {min(note)} 還不可信，取捨反了")
    if "## 相關頁面" not in body:
        warnings.append(f"{rel}: 缺少「相關頁面」段落")

# index 覆蓋率
if "index" in pages:
    idx = pages["index"].read_text(encoding="utf-8")
    for stem in pages:
        if stem not in SPECIAL and f"[[{stem}]]" not in idx:
            errors.append(f"wiki/index.md: 沒有列出 [[{stem}]]")
else:
    errors.append("缺少 wiki/index.md")

for stem, count in inbound.items():
    if stem not in SPECIAL and count == 0:
        errors.append(f"孤兒頁：{stem}（沒有任何頁面連進來）")

# raw 來源都要被至少一個 source 頁摘要
for sid in sorted(raw_ids):
    if not any(s.startswith(sid.lower() + "-") for s in pages):
        warnings.append(f"raw/{sid} 還沒有對應的 sources/{sid.lower()}-*.md 摘要頁")

print(f"LLM Wiki lint｜{len(pages)} 頁、{len(raw_ids)} 個來源")
for e in errors:
    print("  ERROR  ", e)
for w in warnings:
    print("  WARN   ", w)
print("結果：", "PASS" if not errors else f"FAIL（{len(errors)} errors）", f"/ {len(warnings)} warnings")
sys.exit(1 if errors else 0)
