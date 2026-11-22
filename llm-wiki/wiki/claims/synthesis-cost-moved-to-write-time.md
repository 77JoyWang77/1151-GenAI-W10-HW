---
title: 主張：LLM Wiki 把綜整成本移到寫入時
type: claim
sources: [S2]
updated: 2026-11-21
tldr: wiki 在 ingest 時就做綜整（成本前置），資料庫／RAG 把綜整延到查詢時；wiki 不是免費的
---
# LLM Wiki 把綜整成本移到寫入時 (write-time vs query-time)

## 主張
- LLM Wiki 在寫入 (write-time) 就綜整，成本前置；資料庫在查詢 (query-time) 才綜整 [S2]
- 資料庫那一邊的特性是：需要時才做重工 [S2]
> "The heavy work happens at the moment you need it." [S2]
- 因此 wiki 沒有持續維護就會漂移 → [[stale-wiki-looks-like-misinformation]] [S2]

## 相關頁面
- [[wiki-accumulates-rag-rederives]]
