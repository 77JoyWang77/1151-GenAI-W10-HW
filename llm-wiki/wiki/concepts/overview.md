---
title: LLM Wiki 是什麼 (Overview)
type: concept
sources: [S1, S2]
updated: 2026-11-21
tldr: 讓 LLM 當「維護者」，把讀過的資料持續整理成一組互相連結的 markdown 頁面，知識會越積越多
---
# LLM Wiki 是什麼

## 一句話
- LLM Wiki 是一種個人知識庫的做法：LLM 逐步建立並維護一組互相連結的 markdown 檔 [S1]

## 解決什麼問題
- 一般「上傳文件問 AI」的工具（NotebookLM、ChatGPT 上傳、多數 RAG）在每次提問時才去找原始片段，答案每次重新推導，沒有任何東西被累積下來 [S1]
- LLM Wiki 把整理工作移到資料進來的時候：交叉引用、矛盾、綜整都先寫好，下一次提問時已經在那裡 [S1]
- 所以 wiki 是一個持續累積 (compounding) 的產物 [S1]

## 為什麼以前做不起來、現在可以
- 詳見 [[llm-makes-maintenance-cheap]] [S1]
- 人會放棄 wiki，是因為維護成本長得比價值快 [S1]
- LLM 不會厭倦更新交叉引用，維護成本趨近於零 [S1]

## 分工
- 人：挑來源、探索、問好問題、判斷「這代表什麼」[S1]
- LLM：摘要、交叉引用、歸檔、bookkeeping [S1]

## 結構與操作
- 三層：raw sources、wiki、schema → [[three-layers]] [S1]
- 三個操作：[[ingest]]、[[query]]、[[lint]] [S1]

## 有什麼風險
- 成本前置在寫入時，沒維護會漂移；規模約 100–200 來源時開始吃力；讀者分不清誰的理解 → [[failure-modes]]、[[mitigations]] [S2]

## 相關頁面
- [[wiki-accumulates-rag-rederives]]
- [[index-and-log]]
