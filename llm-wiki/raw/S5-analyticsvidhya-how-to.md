---
id: S5
title: LLM Wiki Revolution: How Andrej Karpathy's Idea is Changing AI
author: Analytics Vidhya
url: https://www.analyticsvidhya.com/blog/2026/04/llm-wiki-by-andrej-karpathy/
published: 2026-04
accessed: 2026-11-21
type: 實作教學 (how-to)
credibility: 中（實作導向，沒有給完整 prompt）
rank: 2
---
## 重點（改寫，非原文）

- 資料夾：raw 來源資料夾（Web Clipper 存的文章、圖片下載到本地）、`wiki/`（根目錄 index.md、`wiki/concepts/` 子資料夾）；整個專案 `git init`
- 頁面模板：frontmatter（title、type、source、created、updated、tags，Dataview 範例另有 sources、confidence）+ 一句話 TLDR + 內文 + 反方論點或資料缺口
- 命名一致：`concept-name.md`、`firstname-lastname.md`
- Ingest：先分類文件再萃取——論文逐節處理、推文取核心觀點 + 脈絡、會議逐字稿取決策 / 待辦 / 關鍵發言；再寫或更新頁面、標出矛盾、需要時建新概念頁
- Query：從 index.md 開始掃 TLDR 再深入；有價值的答案存成新頁並標 `query-result`
- Lint：找矛盾與被新來源推翻的說法、孤兒頁、被提到但沒有自己頁面的概念
- 工具：Obsidian（Graph View、Dataview 把 frontmatter 當資料庫查）、Web Clipper、qmd（keyword / semantic / hybrid + rerank，可當 MCP server）、Git（每次 ingest 後 commit，可 diff / revert）
- 建議：從單一主題 5–10 篇開始；frontmatter 與命名規則一開始就定，事後很難改；超過約 100 頁 index 本身就可能超過一個 context window；定期 lint

## 原句
（逐字、每句 15 字以內；2026-11-21 經 WebFetch 取得。shell 無法直接下載原文，所以標出驗證程度）

- "give the AI 5-10 of your best sources."（單一擷取（WebFetch））
- "The index becomes unreadable in one context window when you have more than 100 pages."（單一擷取；與第一次擷取摘要一致）
- "By first classifying the type of document"（單一擷取（WebFetch））
