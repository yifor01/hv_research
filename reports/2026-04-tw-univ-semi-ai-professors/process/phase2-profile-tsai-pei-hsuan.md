# Phase 2 深度 Profile：蔡佩璇 Pei-Hsuan Tsai（NCKU IMIS，CPS Lab）

**撰寫日期：** 2026-04-22  
**資料時效：** 2024–2026  
**Phase 1 判定：** T6（CPS / Digital Twin / ML）｜綁定狀態：🟢 Open

---

## 基本資料

| 欄位 | 內容 |
|------|------|
| 現職 | 教授，國立成功大學 製造資訊與系統研究所（IMIS）& 資訊工程學系 |
| 實驗室 | Cyber-Physical System Lab（CPS Lab），前稱 ISA Lab，2011 年創立 |
| Email | phtsai@mail.ncku.edu.tw |
| 辦公室 | 照坤精密儀器大樓 5F 95523，台南東區 |
| 學術背景 | 博士：清華大學資工（2004–2010）；碩士：Cornell 資工（2003–2004）；學士：清華大學資工（1998–2003） |
| 國際經歷 | 2024–2025 Fulbright Senior Research Scholar，University of Pittsburgh（AI 醫療導引系統） |

---

## 1. 隱形綁定檢查 ⚠️

### TSMC 直接綁定：無明確跡象

搜尋「蔡佩璇 TSMC」「NCKU IMIS TSMC 框架合作」，**未發現**蔡教授本人有正式的台積電聯合研究計畫或框架協議。

**間接關聯（值得關注但非綁定）：**
- NCKU 整體層面有「台積電-成大聯合研發中心」（2014 年成立），但蔡教授所屬的 CPS Lab 研究方向（醫療 Digital Twin、火災緊急應變）與該中心核心課題（先進製程）**並不重疊**。
- 2024 年 11 月 TSMC IMC DAY 活動（400 人規模），由 NCKU CSIE 主辦，參與的主要是 Yang Chung-Ping 等智慧製造教授，蔡教授**未見列名**。
- CPS Lab 2024 屆畢業生：**林映君、呂承翰、陳彧庭（均任職 TSMC）**——顯示學生人才輸送給台積，但教授本人無合作捆綁。

### LinkedIn 兼職：未公開

LinkedIn 帳號存在（@pei-hsuan-tsai-63623ba0），但頁面狀態碼 999（LinkedIn 防爬蟲），無法直接取得資料。根據現有公開資料，**無發現顧問或兼職紀錄**。

### 論文致謝：無半導體廠商資助

近期論文（2023–2025）致謝方主要為國科會（NSTC）及台灣大學/研究機構合作。**無台積電、日月光、聯電等廠商贊助項目**。

**綁定風險評估：低。** 蔡教授目前 2024–2025 學年在美做 Fulbright，研究聚焦醫療 AI，與任何半導體廠的合作距離最遠。

---

## 2. 技術契合度分析

### 研究方向全覽（來自 CPS Lab 官網）

蔡教授的研究橫跨三大軸：

| 領域 | 核心課題 |
|------|---------|
| **Smart Healthcare** | 生理/心理 Digital Twin、AI 醫療決策導引、邊緣運算資源分配 |
| **Disaster Prevention** | 火災 CPS、路徑規劃、機器人自主疏散、人機協作 |
| **Smart Manufacturing** | 電腦視覺 SOP 驗證、IoT 整合、行為分析、即時排程 |

### 代表論文（2022–2025，5 篇精選）

1. **"A Multi-Objective Resource Allocation Strategy for Personal Healthcare Digital Twins in Dynamic Edge Environments"**  
   *IEEE Internet of Things Journal*，2025（接受中）  
   → Digital Twin 架構設計核心能力展示；邊緣動態環境多目標最佳化，與 Fab Edge Node 場景高度可遷移。

2. **"Semantic2Graph: Graph-Based Multi-Modal Feature Fusion for Action Segmentation in Videos"**  
   *Applied Intelligence*，2024，引用 49 次  
   → 多模態感測融合能力；視覺 + 語義圖網路；可延伸至 Fab 製程動作監控。

3. **"A Self-Evacuation Approach for Robots in Fire Disasters"**  
   *IEEE Systems Journal*，March 2024，引用 4 次  
   → CPS 即時決策；機器人路徑規劃；底層方法論與 Fab AMR/AMHS 自動化有共性。

4. **"An Efficient Graph Convolution Network for Skeleton-Based Dynamic Hand Gesture Recognition"**  
   *IEEE Transactions on Cognitive and Developmental Systems*，2023，引用 28 次  
   → 動作辨識 + GCN；應用於作業員動作標準化驗證（SOP Verification）——Fab 人機協作需求。

5. **"Safest-Path Planning Algorithm for Indoor Fire Evacuation"**  
   *International Journal of Disaster Risk Reduction*，2023，引用 22 次  
   → 即時路徑規劃演算法；結合感測器資料融合——與 Fab 廠房動線優化方法論相通。

### Fab Digital Twin 技術缺口評估

| 技術項目 | 蔡教授現有能力 | Fab 需求缺口 |
|---------|-------------|------------|
| Digital Twin 架構 | ✅ 有（Healthcare DT） | 需轉向製程 DT（製程參數、設備狀態） |
| 感測器融合 | ✅ 強（多模態、IoT） | 需加 SEMI E187/APC 介面理解 |
| 即時排程 | ✅ 明確列為專長 | 直接可用於 Fab Dispatch/Scheduling |
| 電腦視覺 SOP | ✅ 主力研究方向 | 直接對應 Fab 作業員稽核需求 |
| 製程模擬 | ❌ 無明確發表 | 需補強（PDK/TCAD 層不需要，但 DES 需要） |
| MES 整合 | ❌ 未見相關論文 | 關鍵缺口，需合作方補足 |

**綜合評分：7.5/10（技術遷移性高，製程深度待驗證）**

---

## 3. 學生工程素質評估

### Lab 規模（2026 年初狀態）

- **博士生**：1 名（王振民，AI 火災防護系統）
- **碩士生（在學）**：約 12 名（2023–2025 級）
- **Lab 助理**：1 名（黃元伶）
- **總規模**：約 13–15 人，中型 Lab

### 研究主題分布（碩士生）

| 方向 | 人數 |
|------|------|
| Digital Twin（醫療/個人健康） | 3 |
| 模型輕量化（蒸餾、剪枝、量化） | 3 |
| 多模態學習 | 2 |
| 製造系統最佳化 | 1（楊惠文） |
| 資料融合 | 1（盧子晴） |
| 其他（醫療排程、生成模型） | 2 |

**注意**：只有 1 名碩士生（楊惠文，2024 級）研究主題明確標示「製造系統最佳化」，其餘偏醫療或 AI 輕量化。

### 競賽成績

- 2021 年 ACM-ICPC 台北站**銀牌**，全國電腦程式競賽**第 4 名**（大學部學生）
- 2024 年 TSMC IMC DAY AI 應用競賽：**非本 Lab 學生**（金牌得主來自 Yang Chung-Ping Lab）

### 畢業生去向（2023–2024 屆，已確認）

| 畢業生 | 去向 |
|--------|------|
| 林映君（2024） | **TSMC** |
| 呂承翰（2024） | **TSMC** |
| 陳彧庭（2024） | **TSMC** |
| 陳冠廷（2024） | 中華電信研究院 |
| 陳冠霖（2023） | TSMC / ASML / MediaTek |
| 張俊彬（PhD） | 北京大學深圳研究生院（博士後） |
| 施冠融（PhD） | **群聯電子（Phison）** |

**發現：3 名 2024 屆直接進 TSMC，另有 ASML 及 Phison，南科走廊輸送效率高。**

---

## 4. 合作優缺點與建議

### 優點

1. **人才管道已打通**：每年有 2–3 名碩士生直接入職 TSMC，合作建立聯合培育機制成本低——學生已自然流向 Fab。
2. **Digital Twin 架構能力實貨**：2025 年 IEEE IoT Journal 論文展示多目標邊緣 DT 部署能力，與 Fab 的 Edge-Fog-Cloud 三層架構完全可對應。
3. **綁定風險最低**：無台積、日月光、聯電競爭性框架；Fulbright 在外，2025 年返台後立即可洽談。
4. **電腦視覺 SOP 驗證已有成品**：AI 影像分析人類行為之 SOP 驗證系統（科技部 2022 計畫），直接可改裝為 Fab 作業員稽核模組。
5. **即時排程是明確專長**：Job Scheduling and Dispatching 列為正式研究方向，對應 Fab Dispatch 優化 Use Case。

### 缺點 / 風險

1. **製程深度不足**：所有論文中**無一篇**涉及半導體製程模型、虛擬量測（Virtual Metrology）、或 FDC（Fault Detection & Classification）。需合作方（如 IMIS 其他教授或 TSMC 內部團隊）補足製程知識。
2. **Lab 製造研究單薄**：12 名碩士生中只有 1 名做「製造系統最佳化」，其餘聚焦醫療或 AI 輕量化。新 Fab Digital Twin 題目需要額外招募具製造興趣的學生。
3. **Fulbright 在外（至 2025 年中）**：2024 年 8 月起赴美一年，實質研究合作最快 2025 下半年啟動；需提前簽備忘錄。
4. **博士班能量薄**：只有 1 名 PhD 在學，長期深度 Fab Digital Twin 需博士生級別研究力，需先補強 PhD 招募。

### 3 個具體合作題目建議

**題目 A：Fab SOP 視覺驗證系統（6–12 個月，快速落地）**  
利用蔡教授已有的 AI 影像分析 SOP 驗證技術，移植至 Fab 潔淨室場景。針對作業員換藥、晶圓搬運、設備維保等標準流程進行合規性即時檢測。預期產出：POC 系統 + 1 篇 IEEE Transactions 論文。

**題目 B：2nm Fab 邊緣節點即時排程 Digital Twin（12–24 個月，核心題目）**  
結合蔡教授的多目標邊緣 DT 框架（Healthcare DT 論文）與 Fab Job Dispatching 專長，建構 2nm Fab Wet Station / Lithography Cluster 的 DT 排程模型，整合設備 OEE 數據實現自適應派工。需 TSMC 提供匿名化生產數據。

**題目 C：Fab 人機協作 CPS 平台（18–30 個月，長期合作）**  
在 AMR 物流與人員協作場景中，整合蔡教授的 Skeleton-based 動作辨識 + CPS 即時決策框架，建立 Fab 廠房人機安全協作的 Digital Twin 仿真環境。可與 NVIDIA Omniverse 接軌。

---

## 5. 總體評估

| 面向 | 評分 | 說明 |
|------|------|------|
| 技術契合度 | ★★★★☆ | DT 架構強，製程深度需補足 |
| 學生工程素質 | ★★★★☆ | TSMC 管道暢通，PhD 能量薄 |
| 合作潔淨度 | ★★★★★ | 無競爭性綁定，最安全 |
| 短期可啟動性 | ★★★☆☆ | Fulbright 2025 年中前在外 |
| 長期 Fab 潛力 | ★★★★☆ | 3 個具體題目均具可行性 |

**建議動作**：2025 年 Q3 蔡教授返台後，以「SOP 視覺驗證」為敲門磚接觸（題目 A 門檻最低、見效最快），同步簽訂碩士生聯合培育備忘錄，優先鎖定 2026 年入學的製造方向學生。

---

## 6. 資料來源

| 來源 | URL | 查閱日期 |
|------|-----|---------|
| NCKU CPS Lab 官網 | https://cps.imis.ncku.edu.tw/ | 2026-04-22 |
| CPS Lab 招生頁 | https://cps.imis.ncku.edu.tw/callforstudent | 2026-04-22 |
| CPS Lab People | https://cps.imis.ncku.edu.tw/people | 2026-04-22 |
| NCKU CSIE 教師頁 | https://www.csie.ncku.edu.tw/en/members/42 | 2026-04-22 |
| NCKU Research Output | https://researchoutput.ncku.edu.tw/en/persons/pei-hsuan-tsai/ | 2026-04-22 |
| Google Scholar | https://scholar.google.com/citations?user=Ou_rfJoAAAAJ&hl=en | 2026-04-22 |
| Fulbright Taiwan 期刊 | https://journal.fulbright.org.tw/author/pei-hsuan-tsai/ | 2026-04-22 |
| NCKU IMIS 所官網 | https://imis.ncku.edu.tw/ | 2026-04-22 |
| NCKU SDG – IMC DAY 2024 | https://sdg.ncku.edu.tw/product-787.html | 2026-04-22 |
| TSMC-NCKU Research Center | http://tsmccenter.ncku.edu.tw/ | 2026-04-22（憑證過期，無法訪問） |
