---
title: 主張：中等規模下只靠 index.md 就夠，不需要向量檢索
type: claim
sources: [S1, S2, S5]
updated: 2026-11-21
tldr: 採信 S1：約 100 個來源、數百頁內靠 index 就夠；S5、S2 認為約 100–200 頁就撐不住（可信度較低，列於註記）
---
# 中等規模下只靠 index.md 就夠

## 主張
- 約 100 個來源、數百頁的規模下，LLM 先讀 index.md 就能找到頁面，不需要 embedding RAG [S1]
- index 不夠用時，再加 qmd 這類搜尋工具 [S1]

## 註記
- S5（實作教學，rank 2）：超過約 100 頁時 index 本身就讀不進一個 context window [S5]
> "The index becomes unreadable in one context window when you have more than 100 pages." [S5]
- S2（評論，rank 3）：留言指出 index.md 在 100–200 頁左右會塞爆 context，大文件需要檢索，等於 RAG 又回來 [S2]
> "index.md breaks at ~100-200 pages (overflows context window)" [S2]
- 差在哪：S1 說的是「來源數約 100」，S5、S2 說的是「頁數約 100–200」；依 AGENTS.md §5 採信 S1 [S1, S2, S5]
- （推論）兩邊數字的單位不同（來源 vs 頁），不一定真的衝突；本 wiki 只有約 25 頁，兩種說法都不影響

## 相關頁面
- [[index-and-log]]
