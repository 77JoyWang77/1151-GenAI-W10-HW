---
id: S3
title: What Is Karpathy's LLM Wiki? A Zettelkasten User's Honest Review
author: Yu Wenhao
url: https://yu-wenhao.com/en/blog/karpathy-zettelkasten-comparison/
published: 2026-04
accessed: 2026-11-21
type: 比較文章 (comparison)
credibility: 中（個人實際使用經驗）
rank: 3
---
## 重點（改寫，非原文）

- 作者自己的 LYT（Obsidian 知識管理）骨架跟 Karpathy 幾乎相同：raw 來源、維護中的知識頁、schema 檔、index
- 差異：Karpathy 是主題聚合 (topic aggregation)，一頁放一個主題目前最好的綜整；LYT/Zettelkasten 是原子卡片，一卡一概念，用連結與 MOC 串起來
- 主題聚合要決定「這篇來源併進哪一頁、主題邊界在哪」，作者認為這跟資料夾/標籤一樣是「放哪個容器」的問題；試 ingest 時卡在邊界判斷，覺得答案很隨意
- Karpathy 的流程有 ingest 時偵測矛盾、一篇更新 10–15 頁、定期 lint；作者的系統原本沒有，打算補上
- Model collapse 疑慮：LLM 反覆改寫可能把細節磨平；作者說自己每張卡都看過，LLM 不會讀未驗證的輸出；但 Karpathy 的做法還沒被長期驗證
- Vibe thinking 疑慮：把整理外包等於把思考外包；作者的回應是先在對話中想清楚再歸檔
- 主要擔憂是內化 (internalization)：寫筆記本身就是產生想法的過程；若 LLM 負責產出、人只負責問，wiki 看起來井然有序，人卻沒吸收多少
- 建議：主題清楚且長期、不介意決定資訊歸屬 → 試 Karpathy；想避開分類系統 → 原子筆記；不論哪種都要先自己想過、並複核 LLM 的產出

## 原句
（逐字、每句 15 字以內；2026-11-21 經 WebFetch 取得。shell 無法直接下載原文，所以標出驗證程度）

- "Karpathy’s topic aggregation is a step backward."（單一擷取；與第一次擷取摘要一致）
- "where are the topic boundaries?"（兩次擷取一致）
- "Whether this pattern actually triggers Model Collapse, nobody has run it long enough to prove."（單一擷取（WebFetch））
- "Thinking happens in the conversation."（單一擷取（WebFetch））
