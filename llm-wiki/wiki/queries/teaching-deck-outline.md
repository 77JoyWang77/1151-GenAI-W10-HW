---
title: 查詢結果：教學簡報大綱 (Query Result)
type: query-result
sources: [S1, S2, S3, S4, S5]
updated: 2026-11-21
tldr: 用本 wiki 產生「LLM Wiki 是什麼？」教學簡報時的大綱，每張投影片對應的 wiki 頁與來源
---
# 教學簡報大綱

查詢：用這個 wiki 做一份給初學者的「LLM Wiki 是什麼？」教學簡報

對象：沒聽過 LLM Wiki、知道 ChatGPT 但不懂 RAG 的人

教學順序：情境引入 → 核心想法 → 結構與操作 → 為什麼可行 → 風險與改善 → 動手做 → 測驗 → 回顧

## 投影片
- LLM Wiki 是什麼？讓 AI 幫你維護一本會長大的筆記｜根據 [[overview]] [S1]
- 你丟一堆 PDF 給 AI，隔天再問，它記得昨天整理過的東西嗎？｜根據 [[overview]]、[[wiki-accumulates-rag-rederives]] [S1]
- LLM Wiki：把整理從提問時移到資料進來時｜根據 [[overview]] [S1]
- RAG vs LLM Wiki｜根據 [[wiki-accumulates-rag-rederives]]、[[synthesis-cost-moved-to-write-time]] [S1, S2]
- 三層結構：誰可以改什麼？｜根據 [[three-layers]] [S1, S5]
- Ingest：先討論，後生成｜根據 [[ingest]] [S1, S3, S5]
- Query：對 wiki 提問，好答案存回去｜根據 [[query]]、[[index-and-log]] [S1, S5]
- Lint：定期健康檢查｜根據 [[lint]]、[[catch-contradictions-at-ingest]] [S1, S2]
- index.md 和 log.md：給 LLM 的地圖和日記｜根據 [[index-and-log]] [S1]
- 人會放棄 wiki，是因為維護太累｜根據 [[llm-makes-maintenance-cheap]]、[[tool-stack]] [S1]
- wiki 寫得越有把握，錯的時候越難被發現｜根據 [[failure-modes]]、[[stale-wiki-looks-like-misinformation]]、[[index-enough-at-moderate-scale]]、[[human-may-not-internalize]] [S1, S2, S3]
- 三個方向：可追溯、早發現、可重建｜根據 [[mitigations]]、[[topic-aggregation-has-boundary-problem]] [S2, S3]
- 自己做一個 LLM Wiki：五個步驟｜根據 [[how-to-start]]、[[tool-stack]] [S1, S5]
- 小測驗｜根據 [[wiki-accumulates-rag-rederives]]、[[three-layers]]、[[stale-wiki-looks-like-misinformation]] [S1, S2]
- 重點回顧｜根據 [[overview]]、[[s1-karpathy-gist]]、[[s2-critique-and-comments]]、[[s3-zettelkasten-review]]、[[s4-hjarni-hosted]]、[[s5-analyticsvidhya-how-to]] [S1, S2, S3, S4, S5]

## 相關頁面
- [[index]]
- [[query]]
