---
title: 匯入 (Ingest)
type: concept
sources: [S1, S3, S5]
updated: 2026-11-21
tldr: 加入一篇來源 → 先討論 takeaways → 再寫摘要、更新相關頁、記 log
---
# Ingest

## 步驟
- 把新來源放進 raw，請 LLM 處理 [S1]
- LLM 讀完先跟人討論重點 (takeaways)，再寫摘要頁 [S1]
- 更新 index、修改相關的概念 / 實體頁，最後在 log 記一筆 [S1]
- 一篇來源可能動到 10–15 個頁面 [S1]

## 先分類再萃取
- 不同文件萃取方式不同：論文逐節處理、推文取核心觀點與脈絡、會議逐字稿取決策與待辦 [S5]

## 為什麼「先討論、後生成」
- 作者偏好一次 ingest 一篇並全程參與，讓人引導 LLM 該強調什麼 [S1]

## 隱藏成本：決定歸屬
- 每篇來源都要決定「併進哪一頁、主題邊界在哪」，見 [[topic-aggregation-has-boundary-problem]] [S3]

## 相關頁面
- [[query]]
- [[lint]]
- [[index-and-log]]
