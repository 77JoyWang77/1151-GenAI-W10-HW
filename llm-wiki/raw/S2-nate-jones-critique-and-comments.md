---
id: S2
title: Karpathy's LLM Wiki — Full analysis with comments
author: aksel（整理 Nate Jones 評論 + gist 留言串約 30 則）
url: https://aksel.mataroa.blog/blog/karpathys-llm-wiki-full-analysis-with-comments/
published: 2026-04
accessed: 2026-11-21
type: 評論 (critique)
credibility: 中（二手整理，但觀點具體、有技術依據）
rank: 3
---
## 重點（改寫，非原文）

- Nate Jones 的核心框架：write-time vs query-time synthesis。LLM Wiki 在 ingest 時就做綜整（成本前置）；資料庫/RAG 把綜整延到查詢時
- 漂移 (drift)：沒被維護的 wiki 不會顯示缺口，舊的綜整在新資料進來後變錯卻仍然讀起來很有把握；過時的 wiki 像錯誤資訊，過時的資料庫只像不知道
- 規模：約 100–200 個來源時開始出問題
- 所有權：讀者分不清看到的是使用者自己的理解，還是 AI 對來源的詮釋
- Jones 的解法：以資料庫為 source of truth、從資料庫重新生成 wiki；錯誤在源資料修，不直接改 wiki
- 留言：index.md 在 100–200 頁左右會塞爆 context window，大文件又需要檢索 → RAG 又回來了；「哪個來源算數」的矛盾處理沒有規範
- 留言：某實作 1,602 個來源編成 161 頁，大約 150 頁時改用 graph view 取代 index.md 導覽，ingest 也需要額外分流步驟
- 留言：LLM 生成頁變成 source of truth，但缺少 provenance（出處）、權威性、新鮮度政策、權限
- 建議：不可變的原子筆記 + 穩定 ID，LLM 只新增筆記與連結不改寫舊的，綜整另外成頁並引用原子筆記 → 可稽核
- 建議：每個 belief 帶 confidence 與 status；新事實分類為 reinforce / weaken / qualify / contradict / create；低信心交給人判斷；在矛盾發生當下就抓
- 建議：機械性工作（hash、切分、重建 index）交給程式，LLM 只做內容
- 未解問題：錯誤是否會隨 wiki 成長而累積放大 (hallucination compounding)；schema 的品質決定所有綜整品質，但多數人會投資不足

## 原句
（逐字、每句 15 字以內；2026-11-21 經 WebFetch 取得。shell 無法直接下載原文，所以標出驗證程度）

- "The heavy work happens at the moment you need it."（單一擷取（WebFetch））
- "Wiki staleness looks like misinformation — you don't know you are wrong."（單一擷取；與第一次擷取的摘要「looks like misinformation」一致）
- "index.md breaks at ~100-200 pages (overflows context window)"（單一擷取（WebFetch））
- "We should catch contradictions at the moment they happen."（兩次擷取一致）
- "I just can't figure out any way to reduce hallucinations with growing wiki."（單一擷取（WebFetch））
