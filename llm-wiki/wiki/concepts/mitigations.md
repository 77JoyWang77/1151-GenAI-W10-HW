---
title: 改善做法 (Mitigations)
type: concept
sources: [S2, S3]
updated: 2026-11-21
tldr: 讓錯誤可追溯（出處、原子筆記）、可提早發現（confidence、即時抓矛盾）、可重建（資料庫為準）
---
# 改善做法

| 做法 | 對應的問題 |
|---|---|
| 資料庫當 source of truth，從它重新生成 wiki | 漂移、錯誤累積 |
| 每個主張帶 confidence + status | 漂移、矛盾 |
| 不可變原子筆記 + 穩定 ID | 出處 |
| 機械工作交給程式 | 格式漂移 |

## 重點
- Nate Jones：以資料庫為準、從資料庫重新生成 wiki；錯誤在源資料修，不直接改 wiki [S2]
- 每個 belief 帶 confidence 與 status；新事實分成 reinforce / weaken / qualify / contradict / create，低信心交給人 [S2]
- 要在矛盾「發生當下」抓到，而不是等定期 lint [S2]
- 不可變原子筆記 + 穩定 ID：LLM 只新增筆記和連結、不改寫舊的，綜整另外成頁並引用原子筆記，整張圖可稽核 [S2]
- hash、切分、重建 index 這類機械工作交給程式，LLM 只做內容 [S2]
- schema 決定所有綜整的品質，但多數人會投資不足 [S2]

## 人這端
- 歸檔前先在對話中自己想清楚，讓 wiki 存的是「已經理解的東西」[S3]
- 複核 LLM 產出的每一頁，LLM 就不會讀到未驗證的內容 [S3]
- 原子筆記的做法見 [[topic-aggregation-has-boundary-problem]] [S3]

## 相關頁面
- [[failure-modes]]
- [[lint]]
