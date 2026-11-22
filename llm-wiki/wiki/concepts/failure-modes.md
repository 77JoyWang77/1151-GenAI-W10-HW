---
title: 失敗模式 (Failure Modes)
type: concept
sources: [S1, S2, S3]
updated: 2026-11-21
tldr: 漂移、規模上限、出處不明、錯誤累積——wiki 寫得越有把握，錯的時候越難被發現
---
# 失敗模式

| 問題 | 發生什麼事 | 為什麼危險 |
|---|---|---|
| 漂移 (drift) | 新資料沒整合進來，舊綜整悄悄變錯 | 讀起來仍然很有把握 |
| 規模 (scale) | 頁數多了 index 放不進 context | 又得回頭用檢索 |
| 出處 (provenance) | 頁面是 LLM 的詮釋，不是原文 | 分不清誰的理解 |
| 錯誤累積 | LLM 讀自己寫的頁再寫新頁 | 尚無定論 |
| 內化不足 | LLM 負責寫、人只負責問 | wiki 很整齊，人卻沒學到 |

## 漂移
- 沒被維護的 wiki 不會顯示缺口，舊的綜整在新資料出現後變錯，卻仍讀起來很有把握 [S2]
- 過時的 wiki 看起來像錯誤資訊，過時的資料庫只像「不知道」[S2]

## 規模
- 約 100–200 個來源時開始出問題 [S2]
- 有實作在約 150 頁時改用 graph view 取代 index 導覽，ingest 也要加分流步驟 [S2]
- 與 S1 的說法有出入，見 [[index-and-log]] [S2]

## 出處與所有權
- 讀者分不清看到的是使用者的理解，還是 AI 對來源的詮釋 [S2]
- LLM 生成頁變成 source of truth，卻缺少出處、權威性、新鮮度政策與權限 [S2]
- 來源互相矛盾時「哪個算數」沒有規範 [S2]

## 錯誤累積
- 錯誤是否會隨 wiki 成長而放大 (hallucination compounding) 是目前沒有答案的核心問題 [S2]

## 人這端的風險：內化不足
- 寫筆記本身就是產生想法的過程；若 LLM 負責產出、人只問問題，人可能從沒真正想過這些內容 [S3]
- Karpathy 把「這代表什麼」留給人，但評論者認為實務上多數人不會做 [S3]

## Model collapse 疑慮
- LLM 反覆改寫可能把細節磨平；若人逐頁複核、LLM 不讀未驗證的產出，可以避免 [S3]
- 這種做法還沒被長期驗證 [S3]

## 主張頁
- 漂移 → [[stale-wiki-looks-like-misinformation]] [S2]
- 規模 → [[index-enough-at-moderate-scale]] [S1, S2]
- 內化不足 → [[human-may-not-internalize]] [S3]
- 錯誤累積 → [[error-compounding-unresolved]] [S2, S3]

## 相關頁面
- [[mitigations]]
- [[lint]]
