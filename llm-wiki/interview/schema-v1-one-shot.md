> **對照組**：這是沒有經過需求訪談、由 AI 一次寫出的第一版規則檔（v1）。目前使用的規則是根目錄的 AGENTS.md（v2，依 interview/summary.md 產生）。

# LLM Wiki Schema（給 LLM agent 的規則檔）

主題：**LLM Wiki 本身**——Karpathy 提出的「讓 LLM 維護個人知識庫」pattern，以及它跟 RAG、Zettelkasten 的比較、失敗模式與改善方式。

## 1. 三層結構

| 層 | 路徑 | 誰寫 | 規則 |
|---|---|---|---|
| Raw sources | `raw/` | 人（挑選） | 只讀不改。每篇一張 source card：URL、取得日期、類型、可信度、重點摘錄（用自己的話改寫，不貼原文全文） |
| Wiki | `wiki/` | LLM | 所有頁面由 LLM 撰寫與更新，人負責閱讀與複核 |
| Schema | `CLAUDE.md`（本檔） | 人 + LLM | 規則改動要寫進 `wiki/log.md` |

## 2. 頁面格式

每個 wiki 頁面（`index.md`、`log.md` 除外）必須有 frontmatter：

```yaml
---
title: 中文標題 (English Term)
type: concept | comparison | source | overview | glossary
sources: [S1, S3]        # 本頁引用到的來源
updated: YYYY-MM-DD
tldr: 一句話重點
---
```

- 檔名：小寫英文 + 連字號，例如 `llm-wiki-vs-rag.md`
- 內文每一條事實性 bullet（`- ` 開頭）結尾必須標來源 `[S1]`、`[S2, S5]`；不能標來源的推論要寫成 `- （推論）...`
- 頁面互連用 `[[page-stem]]`，例如 `[[ingest]]`
- 每頁最後一節為「相關頁面」

## 3. 操作流程

### Ingest（一次一篇，先討論、後生成）
1. **分類**：判斷來源類型（原始提案 / 評論 / 實作教學 / 比較文章 / 產品文）與可信度
2. **討論**：先列出 3–5 個 takeaways、跟現有頁面的衝突點、預計新增/修改哪些頁 → 記入 `log.md` 的「討論」段落，人確認後才寫
3. **生成**：寫 source 摘要頁 `sources/sN-*.md`，更新相關 concept / comparison 頁
4. **Lint**：跑 `python tools/lint_wiki.py`，不通過就回到步驟 3 修
5. **記錄**：在 `log.md` 追加 `## [日期] ingest | SN 標題`

### Query
1. 先讀 `index.md` 的 TLDR，再進相關頁面
2. 回答要附 wiki 頁面與來源 ID
3. 有價值的回答（例如簡報大綱）可以 file back 成新頁面

### Lint
- 每個 bullet 都有來源或標「推論」
- `[[link]]` 都指向存在的頁面；沒有孤兒頁（沒有任何頁面連進來）
- `index.md` 列出所有頁面
- frontmatter 的 `sources` 與內文實際引用一致
- 引用的來源 ID 在 `raw/` 中存在

## 4. 來源可信度規則
- 原始提案（S1）> 實作/教學（S5）> 評論（S2, S3）> 產品文（S4）
- 產品文的主張若無其他來源支持，標註「（廠商觀點）」
- 來源互相矛盾時，在頁面中並列兩方說法，不自行裁決
