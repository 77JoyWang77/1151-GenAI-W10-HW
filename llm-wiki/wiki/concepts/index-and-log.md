---
title: index.md 與 log.md
type: concept
sources: [S1]
updated: 2026-11-21
tldr: index 是「內容目錄」，log 是「時間紀錄」，兩者都是給 LLM 導覽用
---
# index.md 與 log.md

| | index.md | log.md |
|---|---|---|
| 依什麼排 | 內容分類 | 時間 |
| 內容 | 每頁一個連結 + 一行摘要 | 每次 ingest / query / lint 的紀錄 |
| 怎麼更新 | 每次 ingest 改寫 | 只追加 (append-only) |

## 重點
- index.md 是分類目錄，LLM 回答問題時先讀它再深入 [S1]
- 在約 100 個來源、數百頁的規模下，靠 index 就夠用，不需要 embedding RAG [S1]

## 規模上限
- 來源對 index 能撐多大說法不一，依可信度取捨的結果見 [[index-enough-at-moderate-scale]] [S1]

## 相關頁面
- [[query]]
- [[ingest]]
