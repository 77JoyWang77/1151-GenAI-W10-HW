# Index

AI 先讀這一頁：每頁一行 TLDR。頁面只有三種：概念 (concept)、主張 (claim)、來源 (source)。

## 概念 (concepts/)
- [[overview]] — LLM Wiki 是什麼：讓 LLM 持續維護互相連結的 markdown，知識會累積
- [[three-layers]] — raw / wiki / schema 三層，誰可以改什麼
- [[ingest]] — 加入來源：分類 → 討論 → 寫入 → 記 log
- [[query]] — 對 wiki 提問，好答案存回去
- [[lint]] — 定期健康檢查的項目
- [[index-and-log]] — 內容目錄與時間紀錄兩個特殊檔
- [[tool-stack]] — Obsidian、git、qmd、Marp；本地 vs 託管
- [[how-to-start]] — 起步步驟與容易後悔的事
- [[failure-modes]] — 漂移、規模、出處、錯誤累積、內化不足（總覽）
- [[mitigations]] — confidence、原子筆記、資料庫為準、人工複核

## 主張 (claims/)
- [[wiki-accumulates-rag-rederives]] — LLM Wiki 會累積，RAG 每次重新推導
- [[synthesis-cost-moved-to-write-time]] — 綜整成本前置到寫入時，wiki 不是免費的
- [[llm-makes-maintenance-cheap]] — LLM 讓維護成本趨近於零
- [[index-enough-at-moderate-scale]] — 中等規模只靠 index 就夠（有爭議，採信 S1）
- [[stale-wiki-looks-like-misinformation]] — 過時的 wiki 比過時的資料庫更危險
- [[catch-contradictions-at-ingest]] — 矛盾要在 ingest 當下抓
- [[topic-aggregation-has-boundary-problem]] — 主題聚合有「放哪頁」的問題
- [[human-may-not-internalize]] — LLM 寫筆記，人可能沒學到
- [[error-compounding-unresolved]] — 錯誤會不會累積放大：未解
- [[hosted-wiki-tradeoff]] — （廠商觀點）本地綁單機 vs 託管失去 git

## 來源 (sources/)
- [[s1-karpathy-gist]] — S1 原始提案（rank 1）
- [[s5-analyticsvidhya-how-to]] — S5 實作教學（rank 2）
- [[s2-critique-and-comments]] — S2 評論與留言（rank 3）
- [[s3-zettelkasten-review]] — S3 Zettelkasten 使用者評價（rank 3）
- [[s4-hjarni-hosted]] — S4 產品文（rank 4）

## 查詢結果 (queries/)
- [[teaching-deck-outline]] — 教學簡報大綱：每張投影片根據哪些頁（腳本產生）
