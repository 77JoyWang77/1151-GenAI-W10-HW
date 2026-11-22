---
title: 工具組合 (Tool Stack)
type: concept
sources: [S1, S4, S5]
updated: 2026-11-21
tldr: Obsidian 看、LLM agent 寫、git 管版本；搜尋與簡報工具視需要再加
---
# 工具組合

| 工具 | 用途 |
|---|---|
| LLM agent（Claude Code / Codex） | 讀來源、寫 wiki |
| Obsidian | 瀏覽 wiki、graph view |
| Obsidian Web Clipper | 把網頁轉成 markdown 放進 raw |
| qmd | 本地 markdown 搜尋（BM25 / 向量） |
| Marp | 從 markdown 產生投影片 |
| Dataview | 用 frontmatter 做查詢 |
| Git | 版本紀錄與協作 |

## 重點
- 作者的實際畫面：一邊是 LLM agent，一邊是 Obsidian，看著頁面即時更新 [S1]
- index 不夠用時再加 qmd 這類搜尋工具，或自己寫簡單的搜尋腳本 [S1]
- LLM 無法一次讀完文字裡的圖片，所以先讀文字、再分開看圖片 [S1]
- wiki 本身就是一個 git repo，自然有版本歷史 [S1]
- 每次 ingest 後 commit，壞掉的那次可以 diff / revert [S5]
- qmd 有關鍵字、語意、混合 + rerank 三種搜尋，可以當 MCP server 給 Claude Code 用 [S5]

## 本地 vs 託管
| | 本地（Obsidian + agent + git） | 託管（MCP server） |
|---|---|---|
| 存在哪 | 自己電腦的 .md 檔 | 廠商資料庫 |
| 誰讀得到 | 接上檔案的工具 | 任何 MCP client |
| 版本歷史 | git diff / revert | 無 |
| graph view | 有 | 無 |

- （廠商觀點）本地版綁單一電腦，手機或其他 AI 工具看不到 [S4]
- （廠商觀點）託管版讓多個 client 共用同一份 wiki；代價是失去 git 歷史與 graph view，見 [[hosted-wiki-tradeoff]] [S4]

## 相關頁面
- [[three-layers]]
- [[overview]]
