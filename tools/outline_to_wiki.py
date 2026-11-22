"""Query file-back：把 slides/outline.json 轉成 wiki 頁 queries/teaching-deck-outline.md（機械工作交給程式）"""
import json
from datetime import date
from pathlib import Path

BASE = Path(__file__).parent.parent
o = json.loads((BASE / "slides" / "outline.json").read_text(encoding="utf-8"))
srcs = sorted({s for sl in o["slides"] for s in sl["src"]}, key=lambda x: int(x[1:]))
lines = ["---", "title: 查詢結果：教學簡報大綱 (Query Result)", "type: query-result",
         f"sources: [{', '.join(srcs)}]", f"updated: {date.today()}",
         "tldr: 用本 wiki 產生「LLM Wiki 是什麼？」教學簡報時的大綱，每張投影片對應的 wiki 頁與來源", "---",
         "# 教學簡報大綱", "", f"查詢：{o['query']}", "", f"對象：{o['audience']}", "",
         "教學順序：" + " → ".join(o["teaching_arc"]), "", "## 投影片"]
for i, s in enumerate(o["slides"], 1):
    links = "、".join(f"[[{w}]]" for w in s["wiki"])
    # 不放張數編號：編號是結構標籤不是主張，會被 lint 的數字 grounding 誤判（順序由清單本身表示）
    lines.append(f"- {s['title']}｜根據 {links} [{', '.join(s['src'])}]")
lines += ["", "## 相關頁面", "- [[index]]", "- [[query]]", ""]
out = BASE / "llm-wiki" / "wiki" / "queries" / "teaching-deck-outline.md"
out.parent.mkdir(exist_ok=True)
out.write_text("\n".join(lines), encoding="utf-8")
print("wrote", out.relative_to(BASE))
