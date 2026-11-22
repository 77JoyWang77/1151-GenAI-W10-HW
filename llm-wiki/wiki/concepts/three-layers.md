---
title: 三層結構 (Three Layers)
type: concept
sources: [S1, S5]
updated: 2026-11-21
tldr: raw（原始資料，只讀）、wiki（LLM 寫）、schema（規則檔，人和 LLM 一起改）
---
# 三層結構

| 層 | 內容 | 誰負責 |
|---|---|---|
| Raw sources | 文章、論文、圖片、資料 | 人挑選；LLM 只讀不改 |
| Wiki | 摘要、概念頁、比較頁、總覽 | LLM 撰寫與維護，人閱讀 |
| Schema | CLAUDE.md / AGENTS.md 規則檔 | 人和 LLM 一起修 |

## 重點
- Raw sources 是不可變的 (immutable)，LLM 讀它們但從不修改 [S1]
- Wiki 層完全由 LLM 擁有：建立頁面、更新、維持交叉引用 [S1]
- Schema 是一份設定文件，定義結構、命名慣例與工作流程，隨使用逐步調整 [S1]

## 頁面模板（實作建議）
- frontmatter（title、type、source、created、updated、tags），再加一句話 TLDR、內文、反方論點或資料缺口 [S5]
- 命名一致，例如 `concept-name.md` [S5]

## 相關頁面
- [[overview]]
- [[ingest]]
