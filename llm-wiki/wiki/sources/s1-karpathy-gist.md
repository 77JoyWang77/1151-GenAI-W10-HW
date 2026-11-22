---
title: 來源摘要：Karpathy《LLM Wiki》idea file
type: source
sources: [S1]
updated: 2026-11-21
tldr: LLM Wiki 的原始提案——讓 LLM 持續維護一組互連的 markdown 頁，取代每次重新檢索推導
---
# S1：Karpathy《LLM Wiki》

## 這份來源在講什麼
- 一種用 LLM 建個人知識庫的 pattern，以 GitHub Gist 形式發表的「idea file」，設計成直接貼給 LLM agent 讓它幫你實作 [S1]
- 刻意寫得抽象：資料夾結構、頁面格式、工具都留給使用者和 LLM 自己決定 [S1]

## 重點
- 核心對比：RAG 每次提問都從原始片段重新推導；LLM Wiki 在來源進來時就整合，知識會累積 → [[wiki-accumulates-rag-rederives]] [S1]
- 三層結構 → [[three-layers]] [S1]
- 三種操作 → [[ingest]]、[[query]]、[[lint]] [S1]
- 兩個特殊檔 → [[index-and-log]] [S1]
- 比喻：Obsidian 是 IDE、LLM 是 programmer、wiki 是 codebase [S1]
- 可行的原因：人放棄 wiki 是因為維護成本長得比價值快，LLM 不嫌麻煩，維護成本趨近於零 [S1]

## 相關頁面
- [[overview]]
- [[tool-stack]]
