---
title: 來源摘要：Nate Jones 評論與 gist 留言整理
type: source
sources: [S2]
updated: 2026-11-21
tldr: LLM Wiki 把整理成本前置到寫入時，換來的風險是漂移、規模上限與出處不明
---
# S2：評論與留言整理

## 這份來源在講什麼
- aksel 整理 Nate Jones 的評論文章與 gist 底下約 30 則留言 [S2]

## 重點
- write-time vs query-time：wiki 在寫入時綜整、成本前置；資料庫延到查詢時 → [[wiki-accumulates-rag-rederives]] [S2]
- 漂移、規模、所有權三個問題 → [[failure-modes]] [S2]
- 改善建議：資料庫為準、confidence/status、原子筆記、機械工作交給程式 → [[mitigations]] [S2]
- 未解問題：錯誤會不會隨 wiki 成長而累積放大，留言串沒有答案 [S2]

## 相關頁面
- [[s1-karpathy-gist]]
