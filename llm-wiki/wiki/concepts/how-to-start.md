---
title: 怎麼開始做一個 LLM Wiki (How to Start)
type: concept
sources: [S1, S5]
updated: 2026-11-21
tldr: 選一個主題、準備 5–10 篇來源、先寫好 schema，再一篇一篇 ingest
---
# 怎麼開始

## 步驟
- 把 Karpathy 的 idea file 交給 LLM agent，一起決定適合自己主題的版本 [S1]
- 建資料夾：raw 來源、wiki（根目錄放 index.md），整個專案 `git init` [S5]
- 先寫 schema：frontmatter 欄位、命名規則、什麼時候新增頁 vs 修改舊頁 [S5]
- 從單一主題 5–10 篇來源開始 [S5]
> "give the AI 5-10 of your best sources." [S5]
- 一次 ingest 一篇，每次 ingest 後 commit [S1, S5]
- 定期 lint，避免過時資訊和孤兒頁 [S5]

## 容易後悔的事
- frontmatter 和命名規則事後很難改，一開始就要定好 [S5]
- 超過約 100 頁時 index 本身可能就超過一個 context window，要提早規劃搜尋 [S5]

## 相關頁面
- [[three-layers]]
- [[ingest]]
- [[lint]]
