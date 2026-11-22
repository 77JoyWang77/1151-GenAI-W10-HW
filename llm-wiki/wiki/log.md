# Log（依時間、只追加）

格式：`## [日期] 操作 | 標題`，底下固定有「討論」「變更」「Lint」三段。

## [2026-11-21] schema | 建立 CLAUDE.md
- 討論：使用者選定主題「LLM Wiki 本身」；成果放在 GitHub repo W10
- 變更：建立三層結構、頁面格式、ingest/query/lint 流程、來源可信度規則

## [2026-11-21] ingest | S1 Karpathy — LLM Wiki (idea file)
### 討論（生成前）
- 分類：原始提案，可信度最高 → 作為整個 wiki 的骨架
- Takeaways：
  1. 核心對比是「查詢時重新推導 (RAG)」vs「進來時就整合、持續累積 (wiki)」
  2. 三層：raw / wiki / schema
  3. 三種操作：ingest / query / lint
  4. index.md（內容目錄）與 log.md（時間紀錄）是兩個導覽用的特殊檔
  5. 人與 LLM 分工：人問問題、判斷意義；LLM 做 bookkeeping
- 與現有頁面衝突：無（第一篇）
- 預計頁面：overview、three-layers、ingest、query、lint、index-and-log、tool-stack、llm-wiki-vs-rag、glossary、s1 摘要頁
- 刻意不寫：Memex 歷史細節（只有一句提到，不另開頁）
### 變更
- 新增 10 頁
### Lint
- PASS / 4 warnings（S2–S5 尚未 ingest，預期中）→ run-log/01-lint-after-S1.txt

## [2026-11-21] ingest | S2 Nate Jones 評論 + gist 留言整理
### 討論（生成前）
- 分類：評論（二手整理），可信度中；觀點具體，適合補「缺點」這塊 S1 沒寫的部分
- Takeaways：
  1. write-time vs query-time synthesis：LLM Wiki 是把成本前置，不是免費
  2. 漂移 (drift)：過時的 wiki 看起來像錯誤資訊，比資料庫的「不知道」更危險
  3. 規模上限約 100–200 個來源 / 頁
  4. 缺 provenance：讀者分不清是誰的理解
  5. 改善方向：confidence + status、不可變原子筆記、資料庫當 source of truth、機械工作交給程式
- **與現有頁面衝突**：S1 說約 100 來源、數百頁時 index 就夠用；S2 留言說 index 在 100–200 頁就塞爆 context → 依 schema 規則在 [[index-and-log]] 並列兩方，不裁決
- 預計頁面：新增 failure-modes、mitigations、s2 摘要頁；修改 llm-wiki-vs-rag（加 write-time vs query-time）、index-and-log（規模矛盾）、lint（矛盾當下偵測）、overview、glossary
### 變更
- 新增 failure-modes、mitigations、s2-critique-and-comments；修改 llm-wiki-vs-rag、index-and-log（並列矛盾）、lint、overview、glossary、index（共 9 頁）
### Lint
- PASS / 3 warnings → run-log/02-lint-after-S2.txt

## [2026-11-21] ingest | S3 Yu Wenhao — Zettelkasten 使用者的評價
### 討論（生成前）
- 分類：比較文章（個人使用經驗），可信度中
- Takeaways：
  1. 結構幾乎一樣（raw / 知識頁 / schema / index），差在「主題聚合」vs「原子卡片」
  2. 主題聚合要決定「併進哪一頁、邊界在哪」，作者試 ingest 時卡在這裡
  3. 人這端的風險：內化不足——wiki 很整齊但人沒吸收
  4. model collapse 疑慮：反覆改寫會把細節磨平；人逐張複核可以避免
- 與現有頁面的關係：
  - 補充 [[failure-modes]]：S2 講的是「wiki 本身錯」，S3 講的是「人沒學到」，是不同層次 → 新增一節，不合併
  - 補充 [[ingest]]：「決定歸屬」是 ingest 的隱藏成本
  - 與 S2「不可變原子筆記」建議方向一致 → 在 [[mitigations]] 互相引用
- 預計頁面：新增 llm-wiki-vs-zettelkasten、s3 摘要頁；修改 failure-modes、ingest、mitigations、glossary、index
### 變更
- 新增 llm-wiki-vs-zettelkasten、s3-zettelkasten-review；修改 failure-modes、ingest、mitigations、glossary、index（共 7 頁）
### Lint
- PASS / 2 warnings → run-log/03-lint-after-S3.txt

## [2026-11-21] ingest | S4 Hjarni — 雲端託管版 LLM Wiki
### 討論（生成前）
- 分類：**產品文**，作者在推銷自己的產品 → 依 schema 規則，可信度低–中，獨有主張標「（廠商觀點）」
- Takeaways：
  1. 同意 S1 的核心論點（bookkeeping 是瓶頸）→ 只算「附和」，不提高可信度
  2. 本地版的實際限制：綁一台電腦、只有接上檔案的工具能讀、不好分享
  3. 託管版的代價：沒有 git 歷史 / diff、沒有 graph view、不是 .md 檔
- 決定：不另開「託管方案」概念頁（只有一個來源、且是廠商）；只把「本地 vs 託管」寫進 [[tool-stack]]
### 變更
- 新增 s4-hjarni-hosted；修改 tool-stack、index（共 3 頁）
### Lint
- PASS / 1 warning → run-log/04-lint-after-S4.txt

## [2026-11-21] ingest | S5 Analytics Vidhya — 實作教學
### 討論（生成前）
- 分類：實作教學，可信度中；沒有給完整 prompt，但步驟具體
- Takeaways：
  1. ingest 前先依文件類型分類（論文逐節、推文取核心、會議取決策）
  2. 頁面模板：frontmatter + TLDR + 內文 + 反方論點 / 資料缺口
  3. query 的好答案存成新頁、標 `query-result`
  4. 起步建議：一個主題 5–10 篇、命名與 frontmatter 一開始就定
- 與現有頁面的關係：
  - [[index-and-log]] 的規模矛盾多了一個支持 S2 的來源（約 100 頁 index 可能就超過 context）→ 更新並列內容
  - 本 wiki 的 schema（CLAUDE.md）其實已經採用類似模板 → 不改 schema
- 預計頁面：新增 how-to-start、s5 摘要頁；修改 ingest、query、three-layers、index-and-log、tool-stack、index
### 變更
- 新增 how-to-start、s5-analyticsvidhya-how-to；修改 ingest、query、three-layers、index-and-log、tool-stack、index（共 8 頁）
### Lint
- PASS / 0 warnings → run-log/05-lint-after-S5.txt

## [2026-11-21] lint | 加入數字 grounding 檢查 + 人工複核
### 討論
- 結構 lint 五輪都 PASS，但它只檢查「有沒有標來源」，不檢查「內容跟來源對不對」
- 數字最容易漂移（例如 100–200 被寫成別的數字），所以加一條機械檢查：bullet 裡的數字必須出現在它引用的 raw 卡片
- 先在複製的 wiki 埋兩個錯誤自我測試 → 都抓到（run-log/07）
### 人工複核發現
- **lint 的盲點：表格不在檢查範圍**。[[llm-wiki-vs-zettelkasten]] 表格寫「Zettelkasten：人為主（LLM 輔助）」，但 S3 說兩種做法都讓 LLM 處理維護，差別在作者會複核每張卡 → 改成「LLM 協助維護，人複核每一張卡」
- 其餘 bullet 逐條對照 raw 卡片，無其他問題
### Lint
- PASS / 0 warnings → run-log/06-lint-numeric-grounding-v1.txt

## [2026-11-21] query | 教學簡報「LLM Wiki 是什麼？」
### 討論
- 對象：知道 ChatGPT、不懂 RAG 的人 → 從「上傳 PDF 問 AI」的情境切入，先教 RAG 再教 LLM Wiki
- 必須涵蓋的頁面：overview、llm-wiki-vs-rag、three-layers、ingest、query、lint、index-and-log、failure-modes、mitigations、how-to-start
### Graph v1：直接寫 HTML → 檢查 HTML
- run-log/09：6 errors。分析後 2 個是檢查器誤判（序號、日期），另外發現檢查器漏判（日期 2026-11-21 讓「11」永遠通過）
- 修檢查器後 run-log/11：5 errors，全部是「寫投影片」節點的問題：
  - 自己加了 wiki 沒有的數字：「15 分鐘」「10 份 PDF」、寫死「第 11 頁」
  - wiki / 來源對應錯：測驗頁沒標 data-wiki、回顧頁引用 S3–S5 卻只對應 overview
### Graph v2：大綱先檢查，再 render
- 這些錯都是「規劃」層級的決定 → 把檢查往前移到大綱（slides/outline.json）
- run-log/12 大綱 PASS → render HTML → run-log/13 HTML 與大綱一致性 PASS
- File back：tools/outline_to_wiki.py 把大綱轉成 [[teaching-deck-outline]]
  - run-log/14：13 errors，投影片編號被當成數字主張 → 生成器拿掉編號 → run-log/15 PASS
### 視覺檢查
- run-log/16：15 張都沒溢出；人工看截圖發現雙欄卡片被拉長、留大片空白 → 改 CSS → run-log/17

## [2026-11-21] fix | 簡報在小視窗跑版
- 使用者回報第 8 頁排版跑掉。原本的視覺檢查只測 1280×800；改測 7 種尺寸後，820×600 有 14 張出問題（字級固定、外框跟著視窗縮 → 內容被裁掉或壓到頁尾）
- 修法：投影片固定 1100×619 排版，整張等比例縮放；手機（< 700px）改直式捲動 → 7 種尺寸全 ok（run-log/18）
- 另修：預覽視窗（sandbox iframe）裡 history.replaceState 會報錯 → 包 try/catch

---
# v2：依需求訪談重建（AGENTS.md v2）

## [2026-11-21] schema | 需求訪談 9 題 → AGENTS.md v2
- 訪談紀錄 interview/answers.md、使用者確認的需求摘要 interview/summary.md
- v1 規則檔保留在 interview/schema-v1-one-shot.md 當對照組
- 根目錄 CLAUDE.md 只寫 `@AGENTS.md`

## [2026-11-21] migrate | raw 卡片補 rank 與「## 原句」
- 依 AGENTS.md §5 加 rank：S1=1、S5=2、S2=3、S3=3、S4=4
- 原句由 WebFetch 逐字擷取；S1 第一次擷取只回摘要，改用 S3、S4、implicator.ai 對 Karpathy 的引用交叉確認
- 每句標驗證程度（交叉確認／單一擷取），shell 無法直接下載原文

## [2026-11-21] ingest（批次）| S1–S5 依 v2 規則重寫
### 討論（寫入前）
- 頁面類型改成只有 source / concept / claim：
  - 刪除比較頁 llm-wiki-vs-rag → 改寫成主張頁 [[wiki-accumulates-rag-rederives]]、[[synthesis-cost-moved-to-write-time]]
  - 刪除比較頁 llm-wiki-vs-zettelkasten → 主張頁 [[topic-aggregation-has-boundary-problem]]
  - 刪除 glossary（不屬於三種類型；名詞改在概念頁第一次出現時附英文）
  - overview 的 type 改成 concept
- 矛盾取捨（v1 是並列不裁決，v2 改依 rank）：
  - index 能撐多大：S1（rank 1）說約 100 來源、數百頁靠 index 就夠；S5（rank 2）說超過 100 頁就讀不進一個 context；S2（rank 3）說 100–200 頁會爆 → 採信 S1，S5、S2 放註記 → [[index-enough-at-moderate-scale]]
  - 其餘來源之間是「補充」不是「矛盾」，不需取捨
- 只有產品文支持的說法：本地 vs 託管 → [[hosted-wiki-tradeoff]]，全部標（廠商觀點）
- 新增主張頁 10 頁；修改概念頁連結、來源頁連結、index
### 變更
- 新增 claims/ 10 頁；刪除 comparisons/ 2 頁、glossary；overview 移到 concepts/；修改 7 個概念頁、5 個來源頁、index
### Lint（最多 3 輪）
- 第 1 輪 FAIL 12（run-log/19）：6 處產品文說法沒標（廠商觀點）——v1 只要求「獨有主張」才標，舊頁面寫得鬆；4 處大綱連到已刪除的比較頁；log 舊紀錄的死連結；frontmatter 不一致
- 第 2 輪 FAIL 4（run-log/20）：只剩大綱，留到簡報階段修；log 的死連結改成 warning（log 只追加，不改寫歷史）
- 自我測試（run-log/21）：埋 3 個錯（改原句、拿掉廠商標記、把取捨反過來）→ 全部抓到
- 簡報改接新頁面、重新 file back 後 PASS（run-log/22）

## [2026-11-21] query | 簡報改接 v2 wiki
- 7 張投影片的 data-wiki 換成主張頁；第 11 張「規模」改成跟 wiki 的取捨一致（採信 S1，其他列為不同說法）
- 手機版頁尾因頁名變長換行、往上蓋到內容 → 頁尾改成一般排版（run-log/23）
