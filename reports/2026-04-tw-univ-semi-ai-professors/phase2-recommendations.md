# Phase 2 深度 Profile 建議清單（20 主選 + 5 備選）

- **依據**：phase1-candidates.md（11 校主表 ~210 位）+ 5 所統計所補強 pass + **2026-04-22 核實 pass**
- **篩選原則**：
  1. 🔴 Deep Bound 全排除（6 位）
  2. 7 大主題（T1-T7b）平衡覆蓋，不過度集中單一主題
  3. 優先「🎯 統計所 × AI 交叉」旗艦 PI（本次重大補強發現）
  4. 優先「實驗室規模大、產學合作紀錄明確、可進 Phase 2 的 PI」
  5. T7b LLM 軌獨立配額 2 位（工程師生產力工具）
- **提交方式**：主管可直接在本檔圈選、增刪、調整順序

## ⚠️ 核實 pass 後的修正（2026-04-22）

10 位統計所補強 PI 做 WebFetch 核實，發現 training-data 幻覺率 ~30%。本清單已反映核實結果：
- **#1 簡禎富**：實驗室名修正為 **DALab**（非 SMART Lab）；職銜加「兼執行副校長」
- **#13 彭健育**：實際在 **中研院統計所**（Academia Sinica），非 NTHU 統計
- **#15 唐麗英**：**已替換為 鄭少為**（NYCU IEM → NTHU 統計；原 PI 疑似榮休無 2022+ 論文）
- 核實結果詳見 `phase1-candidates.md §H` 與 `raw-materials/.../verification-results.md`

## ⚠️ Batch 2b 4 位修正（2026-04-22 新增）

4 位 Tier-1 完成 deep profile 後，**2 位發現新 🔴 Deep Bound**：

- **#6 張耀文 ⚠️ 🔴 MediaTek 獨立董事**（2024-5 就任；永續 & M&A 策略委員會）— Phase 1 低估風險。對非 MediaTek 廠商建議：法務先行，避開 IC Design 題目，改 Packaging EDA 切入。
- **#7 Kai-Chiang Wu ✅ 🟢/🟡 Open 確認**。2022 後研究轉 Edge AI / LLM 壓縮；ICCAD CAD Contest 出題人。
- **#9 林勇志 🔴 TSMC 重大綁定**（前 TSMC 13 年 → 特殊模組處經理；2 件 TSMC assignee 專利；2021 TSMC 黃金商秘獎銀獎；離職僅 2.5 年仍在 NDA 窗口）— 建議**替換為 宋振銘**（NCHU 研發長，🟢 Open）作為 T4 主要 PI。
- **#10 宋振銘 ✅ 🟢 Open 確認**。2025 未來科技獎 + i-ONE 儀器獎；3 層端到端架構（光誘導表面改質 → 電化學感測 → AI 預測）。主要風險：研發長行政負擔 30-40%。

### 累計隱形綁定發現（Batch 1 + 2a + 2b）

Phase 2 至今 12 位已 profile，發現 **3 位新 🔴 Deep Bound**（Phase 1 未標記）：
- **張孟凡**（NTHU）— TSMC Corporate Research Director 兼任
- **張耀文**（NTU）— MediaTek 獨立董事
- **林勇志**（NSYSU）— 前 TSMC 13 年 + 專利共有 + 商秘獎

**加上 Phase 1 已標 6 位，🔴 黑名單累計 9 位**。詳見 `phase1-candidates.md §D`。

詳見：`phase2-batch2b-summary.md`

## ⚠️ Batch 2a 4 位修正（2026-04-22 新增）

4 位 Tier-1 完成 deep profile 後，**3 位升 Tier-S、1 位姓名勘誤**：

- **#5 胡璧合**：✅ **升 Tier-S**；🟢 Open 確認；**Micron Foundation Chair Professor（2024）**；Lab 5 博 + 17 碩；可與鄭桂忠形成 device→circuit 研究鏈
- **#8 連震杰（姓名勘誤：原寫「連仁傑」）**：✅ **升 Tier-S 候選**；🟢 Open；5 項專利（工程化強）；嵌入式 CUDA 部署能力；南科地緣（距 Fab 20 分鐘）
- **#12 Jakey Blue**：✅ **升 Tier-S** 替補 #3 陳正剛；**師承陳正剛**（衣缽傳承者）；🟡 TSMC alumni 2010-11，離職 15 年，無返聘
- **新增 #ref1 鄭桂忠（NTHU 電機）**：✅ **新 Tier-S 候選** 替補 #4 張孟凡；🟡 Partial（無 TSMC 正式職，差別於張孟凡）；IEEE Fellow 2024 Class；ISSCC 7 篇 / 3 年；Delta 飛雁先例（2022）；Lab 2-4 主力 = 精品合作

詳見：`phase2-batch2a-summary.md`

## ⚠️ Batch 1 Tier-S 深度 profile 後的重大修正（2026-04-22）

4 位 Tier-S 做完 Phase 2 深度 profile 後，**2 位需重新分類**：

- **#3 陳正剛 🔻 降至「條件式 Tier-A」**：自 2009 轉生醫，近 3 年無半導體論文，Lab 僅 3 名學生。建議替換為 **Jakey Blue（原 #12，上升 Tier-S 位置）**。
- **#4 張孟凡 ⚠️ 對非 TSMC 廠商重新分級 🔴 Deep Bound**：現任 **TSMC Corporate Research Director（兼任）**；Nature 2025 致謝 4 個 TSMC 部門；畢業生首大流向 TSMC。若本公司非 TSMC，建議替換為 **鄭桂忠（NTHU 電機 Nature 合著者，🟢 Open）**。
- **#1 簡禎富 修正細節**：Fellow 列表只保留 APIEMS/CIIE/CSMOT（IEEE/IISE Fellow 無公開證據）；**美光講座教授（2018-）**為「可接非台積合作」的成功先例。
- **#2 李家岩 補強**：本人**有台積電工作背景**、**GitHub 93 stars**（`Manufacturing-Data-Science`）、**Profet AI 產品顧問** — 合作管道有商業化 path。

詳見：`phase2-batch1-tier-s-summary.md`

---

## §1 Phase 2 Top 20（主選）

### 🥇 Tier-S（4 位，必訪 PI，無異議）

| # | 姓名 | 校/系 | 主命中 | 為何 Tier-S | 綁定 |
|---|---|---|---|---|---|
| 1 | **簡禎富 Chen-Fu Chien** ✅核實 | NTHU 工工（講座教授兼執行副校長） | T1+T3+T6 | 🎯🎯🎯 **DALab**（Decision Analysis Lab）主持人 + AIMS 中心 PI；台灣半導體 AI 工工最強 PI；**2005-08 借調台積電工業工程處副處長**、清華-台積電卓越製造中心主任（2013 至今）、NSTC STEP 聯盟 PI；H-index 49、逾 200 篇期刊；博士生主動招生 | 🟢 |
| 2 | **李家岩 Chia-Yen Lee** | NTU 資管副院長 | T1+T3+T6 | 🎯 台灣半導體製造資料科學最高頻出版者；Multi-Agent RL、VM、WBM、PdM 全向；著《製造數據科學》專書；實戰連結最強 | 🟢 |
| 3 | **陳正剛 Argon Chen** 🔻Batch1 | NTU 工工 | T1（歷史）| 🎯 Rutgers IE+Stat 雙碩；**但 2009 起已轉生醫 75%+**；SRC/ISMT/DARPA Bell Labs 歷史成就；**近 3 年無半導體論文；Lab 僅 3 人** → 建議換成 Jakey Blue 升 Tier-S | 🟢（但半導體活躍度低）|
| 4 | **張孟凡 Meng-Fan Chang** ⚠️Batch1 | NTHU 電機（特聘）**+ TSMC CR Director** | T5+T2 | Science 2024 + Nature 2025；IEEE Fellow 2026；**TSMC Corporate Research Director 兼任**；Nature 2025 致謝 4 個 TSMC 部門；**對非 TSMC 廠商 🔴 Deep Bound** | 🔴（非 TSMC）/ 🟢（TSMC 內部）|

### 🥈 Tier-1（8 位，高優先）

| # | 姓名 | 校/系 | 主命中 | 推薦理由 | 綁定 |
|---|---|---|---|---|---|
| 5 | **胡璧合 Vita Pi-Ho Hu** | NTU 電機 | T5+T4 | FeFET × 3D IC × CIM 三方交集；IEDM/IRPS 常駐；L'ORÉAL 科學女性獎 | 🟢 |
| 6 | **張耀文 Yao-Wen Chang** | NTU 電機 | T2 | NTU EDA 旗艦；IEEE CEDA Fellow；Physical Design / DFM 360+ 論文；產業輸送人才中心 | 🟡 多方業界 |
| 7 | **Kai-Chiang Wu 吳凱強** | NYCU 資工 | T2 | CMU 博士；EDA+AI 頂級；Intel 經歷但非深綁；ML for EDA + Design-for-Testability | 🟡 Intel 輕 |
| 8 | **連震杰 James Lien** | NCKU 資工 | T3 | 3D 自動光學檢測、視覺機器人；T3 AOI 最直接命中 | 🟢 |
| 9 | **林勇志 Yung-Chih Lin** | NSYSU SAT | T4 | 3D 晶圓接合、異質整合、晶圓級整合；南科地緣優勢 | 🟡 TSMC AP 推測 |
| 10 | **宋振銘 Chen-Ming Sung** | NCHU 材料（研發長） | T4 | 3D 封裝智慧量測平台 AI；2025 未來科技獎、i-ONE 儀器獎；產業化程度最高 | 🟢 |
| 11 | **王俊明 Chun-Ming Wang** | NSYSU SAT | T6+T7b | 前 TSMC 製程部；光刻/OPC/RET × AI；出身產業背景 | 🟡 TSMC 出身 |
| 12 | **Jakey Blue 藍啓航** | NTU 工工（副教授） | T1+T6 | 🎯 新世代 APC/Equipment Control；Manifold Learning + Time Series；博士機械 × 工工方法論 | 🟢 |

### 🥉 Tier-2（8 位，差異化覆蓋）

| # | 姓名 | 校/系 | 主命中 | 推薦理由 | 綁定 |
|---|---|---|---|---|---|
| 13 | **彭健育 Chien-Yu Peng** 🔧核實 | **Academia Sinica 統計所（副研究員）** | T1+T3 | 🎯 Degradation Model（Wiener/Inverse Gaussian）、Bayesian 退化分析；2023 Bayesian Degradation paper + 2024 Wiener processes test planning；**中研院身份非大學教授，合作管道不同**；方向偏方法論非 DL 應用 | 🟢 |
| 14 | **洪英超 Ying-Chao Hung** | NTU 工工（教授） | T1+T3 | 🎯 密西根博士；SVR Profile Monitoring + DoE；統計所方法論強 | 🟢 |
| 15 | **鄭少為 Shao-Wei Cheng** 🔧核實 | **NTHU 統計所（教授）** | T1 | 🎯 DoE / Response Surface / Computer Experiments / Gaussian Process Emulator — 製程窗口模擬直接對口；2022-2024 持續開設 Experimental Design 課程；ResearchGate 確認活躍；個人頁 stat.nthu.edu.tw/~swcheng/ | 🟢 |
| 16 | **楊佳玲 Chia-Lin Yang** | NTU 資工（特聘） | T7b+T5 | Edge AI / NVM 方法論 PI；DAC 2024 Program Co-chair；IBM Faculty Award；Open 度高 | 🟢 |
| 17 | **王振興 Zhen-Xing Wang** | NCKU 電機（特聘 / AI 中心主任） | T6 | 🎯 AI 數位轉型中心主任；AIoT 實績明確；2024-25 AIoT 人因照明論文 | 🟢 |
| 18 | **蔡佩璇 Pei-Hsuan Tsai** | NCKU 製造資訊（教授） | T6 | 🎯 Cyber-Physical System Lab；Fab Digital Twin 潛力 | 🟢 |
| 19 | **蔡銘峰 Ming-Feng Tsai** | NCCU 資科（教授） | T7b | 🎯 Learning-to-Rank / RAG / IR；SIGIR 2025；**最契合 LLM 工程師效率工具** | 🟢 |
| 20 | **柏林 Berlin Chen** | NTNU 資工（教授） | T7b | 🎯 Taiwan Mandarin LLM 先驅；SMIL Lab；BERT + NLP 深度；教材形象強 | 🟢 |

---

## §2 備選 5 位（主管可替換 Top 20 中任一）

| 姓名 | 校/系 | 主命中 | 為何備選 | 替換建議 |
|---|---|---|---|---|
| **陳冠能 Kuan-Neng Chen** | NYCU ICST 院長 | T4 | 先進封裝首席、ICST 院長，制度層面對接強 | 替換 #11 王俊明（若不想要 TSMC 出身 PI） |
| **鄭桂忠 Kea-Tiong Tang** | NTHU 電機（特聘） | T2+T5 | AI 晶片 Nature 級、2025 NSTC 傑出 | 替換 #6 張耀文（若偏好 AI 晶片而非 EDA） |
| **賴志煌 Chih-Huang Lai** | NTHU 半導體學院 | T5 | MRAM/自旋電子全球領袖、H-index 36 | 替換 #5 胡璧合（若偏好 MRAM 而非 FeFET） |
| **謝孫源 Sun-Yuan Hsieh** | NCKU 資工（講座） | T1+T3 | NCKU AI 頂流、IAAM Fellow、NSTC 傑出 | 替換 #17 王振興（若偏好演算法 PI） |
| **陳立榜 Li-Pang Chen** ✅核實 | NCCU 統計（副教授） | T3 (Causal) | Causal Inference × 高維；2023 SMMR + 2026 JCGS 持續發表；**半導體直接關聯度低**，適合「方法論顧問」而非深度合作 | 替換 #15 鄭少為（若偏好 Causal 而非 DoE）|
| **楊素芬 Su-Fen Yang** ✅核實 | **NCCU** 統計（傑出教授） | T1 (SPC) | EWMA/CUSUM/多變量 SPC；2025 Scientific Reports + 2026 IJIE；品管會委員；活躍且直接命中 | 替換 #14 洪英超（若偏好實證紀錄） |

---

## §3 主題 × Phase 2 候選分佈

| 主題 | Phase 2 候選數 | PI |
|---|---|---|
| **T1 製程控制（SPC/APC/VM）** | 5 | 陳正剛、李家岩、Jakey Blue、洪英超、唐麗英、簡禎富（全棧） |
| **T2 AI-EDA / DTCO / DFM** | 3 | 張耀文、Kai-Chiang Wu、張孟凡（with T5）|
| **T3 良率/缺陷/量測** | 5 | 李家岩、陳正剛、連震杰、彭健育、宋振銘（with T4）、簡禎富（全棧）|
| **T4 先進封裝** | 3 | 林勇志、宋振銘、陳冠能（備選）|
| **T5 Device/新材料** | 3 | 胡璧合、張孟凡、賴志煌（備選）/鄭桂忠（備選）|
| **T6 智慧製造/IIoT** | 4 | 簡禎富、王振興、蔡佩璇、Jakey Blue、李家岩 |
| **T7a AI overlay** | 覆蓋於其他主題 | — |
| **T7b LLM / Agentic** | 3 | 楊佳玲（AI 加速器）、蔡銘峰（RAG）、柏林（Mandarin LLM）|

### 校別分佈（核實後）
- NTU：7 位（#2 李家岩、#3 陳正剛、#5 胡璧合、#6 張耀文、#12 Jakey Blue、#14 洪英超、#16 楊佳玲）
- NTHU：3 位（#1 簡禎富、#4 張孟凡、**#15 鄭少為**）
- Academia Sinica：1 位（#13 彭健育，**中研院非大學**）
- NYCU：1 位（#7 Kai-Chiang Wu）— 原唐麗英已換
- NCKU：3 位（#8 連震杰、#17 王振興、#18 蔡佩璇）
- NSYSU：2 位（#9 林勇志、#11 王俊明）
- NCHU：1 位（#10 宋振銘）
- NCCU：1 位（#19 蔡銘峰）
- NTNU：1 位（#20 柏林）
- NCU / NTUST / NTUT：0（可由備選補或下一輪考量）

---

## §4 Phase 2 每位深度 Profile 模板

對主管圈定的每位 PI，Phase 2 產出包含：

### 1. 技術契合度
- [ ] 個人頁、Lab 網站最新狀態（2026 現任職級、研究重點）
- [ ] 2024-2026 頂會/頂刊論文 5 篇（IEEE TSM、IEDM、ISSCC、ICCAD、DAC、CVPR、ICML、NeurIPS 等）
- [ ] 產學合作紀錄：MOST/NSTC 計畫、公司委案（台積/聯電/日月光/聯發科/NVIDIA...）
- [ ] 近 3 年獎項（IEEE Fellow、傑出研究獎、未來科技獎、AIAA Fellow 等）

### 2. 學生工程素質 & Lab 文化
- [ ] Lab GitHub / 開源專案 / 論文 code repo
- [ ] 學生在 IC/CAD Contest @ ICCAD / AICUP / Kaggle / ICCAD CAD Contest 得獎紀錄
- [ ] 博士/碩士畢業生 LinkedIn 流向（台積、聯發、NVIDIA、Synopsys、Cadence 比例）
- [ ] 是否有業界實習紀錄（協同論文作者、實習報告）
- [ ] Lab 會議規律性、開放日、產業 visit 狀況

### 3. 合作優缺點 & 建議切入方式
- [ ] 優點：方法論強 / 實驗室規模 / 產業 network / 學生素質 / 發表頻率
- [ ] 缺點：綁定風險（🟡/🔴）/ 研究太理論 / 招生困難 / 溝通成本 / 年齡與退休計畫
- [ ] 建議合作型態：
  - **A. 產學合作**（MOST 聯合計畫、公司委案）
  - **B. 實習合作**（碩博生 intern、短期共訓）
  - **C. 人才延攬**（指定學生畢業直接 offer）
  - **D. 顧問型**（單點諮詢、一次性專案）
  - **E. 長期綁定**（冠名講座 / Joint Center）

---

## §5 主管操作建議（下一步 workflow）

### 選項 A：圈選 15-25 位 → 進入 Phase 2
直接在本檔 §1 + §2 圈選，我產出 Phase 2 深度 profile 工作排程。

### 選項 B：針對 Tier-S 4 位先做 Phase 2，其他後批
優先完成 Tier-S 四位（簡禎富、李家岩、陳正剛、張孟凡）的 deep profile，視結果再決定後續。

### 選項 C：先補核實（⚠️ 標記）再圈選
所有 ⚠️ 標記 PI 先上網核實現任職級、2024 論文，再決定是否進 Phase 2。

### 選項 D：追加主題缺口補強
若覺得某主題候選不足（如 T2 EDA 才 3 位），我可針對該主題再做一輪補強 pass。

---

## §6 目前 Phase 2 清單的「風險與注意」

1. **台積電體系不衝突原則**：Top 20 內有 🟡 綁定者 3 位（張耀文、Kai-Chiang Wu、王俊明），皆非排他綁定；**#1 簡禎富 2005-08 曾借調台積電工業工程處副處長**，目前為清華-台積電卓越製造中心主任（非排他、但深度合作），合作題目需避開 TSMC 核心機密議題。
2. **核實 pass 已完成**：2026-04-22 對 10 位統計所補強 PI 做 WebFetch 核實，發現 training-data 幻覺率 ~30%。Top 20 已反映修正（#1 Lab 名、#13 改中研院、#15 換人）。剩餘待核實：#17 王振興、#18 蔡佩璇 為 Phase 1 主表 PI，可信度高於統計補強 PI，但 Phase 2 前仍建議核實。
3. **南科地緣**：NSYSU + NCKU + NCHU 共 6 位，若目標是 2nm 先進製程，南科 PI 的地緣優勢大。
4. **LLM 軌獨立**：#19 蔡銘峰、#20 柏林、#16 楊佳玲（AI 加速器角度）為「工程師效率」題目的關鍵 PI，與半導體 domain 不重疊，可視為獨立合作軌道。
5. **實驗室規模 vs. 學生素質**：Tier-S 的簡禎富 SMART Lab、李家岩 PoLab 學生人數最多；統計所 PI 如彭健育、陳正剛學生相對少但方法論深度高 — 建議兩種型態都保留。

---

**最終決定權在主管**。本清單為 Phase 1 廣度盤點後的建議，可自由調整。
