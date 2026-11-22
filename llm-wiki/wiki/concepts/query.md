---
title: 查詢 (Query)
type: concept
sources: [S1, S5]
updated: 2026-11-21
tldr: 對 wiki 提問，LLM 讀相關頁面後附引用回答；好的答案可以存回 wiki
---
# Query

## 步驟
- LLM 先找相關頁面（從 index 開始），讀完後附引用回答 [S1]
- 輸出形式不限：markdown、表格、投影片 (Marp)、圖表 [S1]

## File back
- 好的回答可以存回 wiki 成為新頁面，讓「探索」本身也會累積 [S1]
> "Good answers can be filed back into the wiki" [S1]
- 實作上可以替這類頁面加上 `query-result` 標籤 [S5]

## 相關頁面
- [[teaching-deck-outline]]（本 wiki 的實際例子）
- [[ingest]]
- [[index-and-log]]
