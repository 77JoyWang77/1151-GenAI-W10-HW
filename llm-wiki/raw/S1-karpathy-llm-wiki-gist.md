---
id: S1
title: LLM Wiki (idea file)
author: Andrej Karpathy
url: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
published: 2026-04
accessed: 2026-11-21
type: 原始提案 (primary)
credibility: 高（概念的原始出處）
rank: 1
---
## 重點（改寫，非原文）

- 提出一種用 LLM 建個人知識庫的 pattern：LLM 逐步建立並維護一組互相連結的 markdown 檔
- 定位是「idea file」：貼給 LLM agent，由 agent 跟使用者一起把細節實作出來；刻意寫得抽象
- 對照組：NotebookLM、ChatGPT 上傳檔案、多數 RAG 系統在提問時才去撈原始片段，每次重新推導，知識不會累積
- LLM Wiki 在來源進來時就整合進既有頁面；交叉引用、矛盾、綜整在下一次提問前就已經存在 → wiki 是會持續累積 (compounding) 的產物
- 三層：raw sources（不可改）、wiki（LLM 擁有並維護）、schema（CLAUDE.md / AGENTS.md，人和 LLM 一起修）
- 三種操作：ingest、query、lint
  - ingest：讀來源 → 跟人討論 takeaways → 寫摘要 → 更新 index → 修改相關頁 → 記 log；一篇來源可能動到 10–15 頁；作者偏好一次一篇、人保持參與
  - query：搜尋 wiki、讀相關頁、附引用回答；輸出可以是 markdown、表格、投影片 (Marp)、圖表；好的回答可以存回 wiki
  - lint：定期健康檢查：矛盾、過時主張、孤兒頁、缺少的概念或交叉引用、可用網路搜尋補的資料缺口
- index.md：以內容為主的分類目錄，每頁一行摘要；LLM 回答前先讀；約 100 個來源、數百頁的規模下不需要 embedding RAG
- log.md：依時間、只追加；固定前綴（如 `## [日期] ingest | 標題`）方便用 unix 工具解析
- 工具：Obsidian（看 wiki、graph view）、Web Clipper、qmd（本地 BM25 / 向量搜尋）、Marp、Dataview；整個 wiki 是 git repo
- 分工：人負責找來源、探索、問好問題、判斷意義；LLM 負責摘要、交叉引用、歸檔、記帳式維護 (bookkeeping)
- 比喻：Obsidian 是 IDE、LLM 是 programmer、wiki 是 codebase
- 為什麼可行：人放棄 wiki 是因為維護成本長得比價值快；LLM 不會厭倦更新交叉引用 → 維護成本趨近於零；呼應 Vannevar Bush 1945 年的 Memex

## 原句
（逐字、每句 15 字以內；2026-11-21 經 WebFetch 取得。shell 無法直接下載原文，所以標出驗證程度）

- "Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."（交叉確認：S3 與 implicator.ai 各自引用）
- "Humans abandon wikis because maintenance grows faster than value."（交叉確認：S4 引用 + gist 擷取摘要相同）
- "the wiki is a persistent, compounding artifact"（單一擷取（WebFetch），未能下載原文逐字比對）
- "Good answers can be filed back into the wiki"（單一擷取（WebFetch），未能下載原文逐字比對）
