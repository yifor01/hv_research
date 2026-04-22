# 宋振銘（Jenn-Ming Song）深度 Profile
**NCHU 材料系教授 / 研發長 — T4 先進封裝 × AI 量測**
*Phase 2 研究日期：2026-04-22*

---

## 基本身份確認

| 欄位 | 內容 |
|------|------|
| 全名 | 宋振銘（Jenn-Ming Song，又譯 Chen-Ming Sung） |
| 現職 | 國立中興大學材料科學與工程學系 教授 |
| 行政職務 | 中興大學研發長（Vice President for Research & Development） |
| 兼任中心 | 工學院「智慧封裝研究中心」主任；「前瞻理工科技中心」主任 |
| 研究室 | 先進導線實驗室（Advanced Wire Laboratory） |
| 信箱 | samsong@nchu.edu.tw |
| 辦公室電話 | 04-22840500 #406 |
| 學術資料庫 | [ScienceDirect Profile](https://www.sciencedirect.com/author/57154837200/jenn-ming-song)；[ResearchGate](https://www.researchgate.net/profile/Jenn-Ming-Song) |

---

## 1. 隱形綁定檢查 ⚠️

### 1.1 TSMC / 日月光直接綁定？
搜尋「宋振銘 TSMC」、「Jenn-Ming Song ASE」均**未發現**任何排他性合作條款、TSMC / 日月光聯名 Chair 職位、或合約保密協議（NDA）相關公開記載。

- 研究主題（Cu-Cu bonding、表面改質、warpage 量測）確實與台積電 SoIC / CoWoS 技術路線高度重疊，但目前屬於「技術方向接近」而非「有合約排他」。
- 無日月光封測委任研究之公開紀錄。

### 1.2 研發長角色的合作排他性？
- NCHU 的「研發長」（Vice President for Research）是校級行政職，**主要職能為統籌全校產學合作政策、學術規劃、設備管理**，並非企業委派或董事級職位。
- NCHU 產學合作架構中，智財歸屬分三類：歸學校、共有、委託研究——均無「教授不得與其他企業合作」之排他條款。
- 結論：研發長職務**本身不構成排他性綁定**，但行政負擔重（見第 4 節分析）。

### 1.3 專利歸屬
依 NCHU 產學合作規定，專利預設歸屬學校（合約 3.1 模板），可協商共有（3.2）或委託研究（3.3）。**沒有任何已知專利直接歸屬台積電或日月光**。其核心專利（波長光源誘導銅表面改質技術）以 NCHU 名義申請，後續技轉視個案談判。

### 1.4 CCNRIA 聯盟綁定？
宋振銘是「中彰投區域產學合作聯盟（CCNRIA）」成員，但 CCNRIA 是跨校跨廠商的廣泛聯盟框架，**無排他義務**，反而是擴大多方合作的機制。

**綜合判定：🟢 Open — 無隱形排他綁定，合作視窗暢通。**

---

## 2. 技術契合度

### 2.1 核心技術平台：3D 封裝接合與智慧量測

宋振銘研究室開發的「**3D 封裝接合技術暨智慧量測控制平台**」包含三層架構：

**層一：光誘導表面改質（Surface Modification）**
- 以特定波長光源（VUV/HCOOH 等預處理）在大氣壓下修飾銅表面氧化層
- 免真空製程，可直接導入產線
- 已獲專利；應用於 Cu-Cu 直接接合（Hybrid Bonding）與 Al-Al 超音波接合

**層二：微型電化學即時感測（Micro-Electrochemical Sensing）**
- 定電流庫侖法（Constant-Current Coulometry）可攜式模組
- 非破壞性偵測銅氧化層種類與厚度，解析度達量測等級
- 適合產線即時監控，填補現有設備無法做線上量測的空缺

**層三：AI 預測平台**
- 整合隨機森林、決策樹、神經網路、LSTM 四種算法
- 輸入：氧化層種類、厚度、環境因子、熱壓製程參數
- 輸出：Cu-Cu 接合強度預測 + 製程可行性判斷
- 提供決策支援，降低試誤成本

### 2.2 代表論文（2022–2026，精選 5 篇）

| 年份 | 題目 | 期刊 | 技術領域 |
|------|------|------|---------|
| 2026 | Study of solder joint reliability performance and component shear property of hybrid low temperature solder joints | *Materials Science in Semiconductor Processing* | 低溫焊接可靠度 |
| 2025 | Unidirectional cross-interface grain growth in Cu–Cu direct bonding | *Journal of Materials Research and Technology* | Cu-Cu 直接接合晶粒結構 |
| 2025 | VUV/HCOOH pre-treatment for Al-to-Al ultrasonic bonding | *Japanese Journal of Applied Physics* | 表面預處理 × 超音波接合 |
| 2025 | Surface Modification for PI-to-PI Direct Bonding | Conference paper | 聚醯亞胺基板接合 |
| 2024 | Magnetically-manipulatable and self-cleaning lab-on-a-bubble Ag@TiO2@Fe3O4 hollow spheres | *Applied Surface Science* | 奈米材料表面功能化 |

> **備注**：warpage 量測 × Deep Learning（DIC + Transformer）是平行研究方向；Nature Microsystems & Nanoengineering 2024 有同類論文但第一作者非宋，其研究室有技術跟進跡象。

### 2.3 技術就緒度評估

| 技術維度 | 評分（1-5） | 說明 |
|---------|-----------|------|
| Cu-Cu 直接接合（Hybrid Bonding）| ★★★★★ | 多篇頂刊 + 2026 年仍有產出 |
| 表面改質 + 電化學量測 | ★★★★★ | 專利核心，已技轉導向 |
| AI 預測平台（接合強度）| ★★★★☆ | 已展示但系統整合度還在精進 |
| Warpage / Stress AI 量測 | ★★★☆☆ | 技術方向確認，DL-DIC 尚在跟進 |
| X-ray + Deep Learning 封裝缺陷 | ★★☆☆☆ | 屬延伸方向，尚無代表性論文 |

---

## 3. 學生工程素質

### 3.1 研究室規模
- 先進導線實驗室（Advanced Wire Laboratory）設於 NCHU 工學院材料系
- 宋振銘同時統籌「工學院智慧封裝研究中心」，跨系合作包含電機、機械、化工
- 與彰化師範大學鐘冠榮教授（AI/ML 專長）建立跨校協作，負責 AI 演算法模組

### 3.2 重要競賽獲獎紀錄

| 獎項 | 屆次 / 年份 | 說明 |
|------|-----------|------|
| 國研盃 i-ONE 儀器科技創新獎 | 第16屆 / 2024 | 學生團隊指導，自製儀器競賽國家級獎項 |
| 2025 PCB 學生優秀論文獎（金獎）| 2025 | 封裝/電路板領域學生競賽頂獎 |
| 2025 未來科技獎（國科會）| 2025 | 技術整體，非單純學生獎但代表成熟度高 |
| 華力創新材料競賽獎 | 近年 | 材料創新類 |

### 3.3 畢業生去向（推估）
- 研究方向與日月光（ASE）、矽品（SPIL）後段封裝流程高度匹配
- 台積電先進封裝（AP 部門）：Cu-Cu bonding / Hybrid Bonding 人才需求大
- 設備商：KLA（量測）、Onto Innovation（warpage 量測）、TEL、SCREEN
- ITRI（工研院）：共同掛名研究員，部分學生走研究院路線
- 實際去向數據尚未有公開統計，需直接向研究室確認

---

## 4. 合作優缺點 & 建議

### 4.1 優點

**A. 研發長職務 = 制度對接快**
宋振銘身為全校研發長，熟悉 NCHU 產學合作流程（CCNRIA 聯盟、智財模板、行政通道），合約談判速度遠快於一般教授。

**B. 未來科技獎 = 技術產業可落地性認證**
國科會未來科技獎評審標準本身就要求「產業化潛力」，能得獎代表技術已從概念驗證進入近端應用。對外部企業合作方而言是重要信號：風險較低、成熟度已至 TRL 4-5。

**C. 跨層整合能力**
材料（表面科學）× 量測（電化學感測）× AI（預測平台）三層整合是本研究室的獨特競爭力。市場上多數團隊只做其中一層，宋的研究室可做端到端交付。

**D. 泛合作生態**
CCNRIA 成員；與 ITRI 有掛名合作；已有彰師大 AI 跨校協作；無單一企業排他鎖定。

### 4.2 缺點與風險

**A. 行政時間擠壓最大風險**
研發長是全校最繁重的行政職之一。按台灣大學常規，研發長每週行政會議、外部推廣活動、政府報告佔用時間保守估計 30-40%。**實質指導學生的 PI 時間相對壓縮**，需確認研究室有資深博士後或副教授接班人。

**B. 研究室 AI 模組仍依賴外部協作**
AI 平台算法由跨校合作（彰師大鐘冠榮）補足，若合作中斷或協作教授異動，AI 模組可能出現空窗。對需要 AI 深度客製的合作方是潛在風險。

**C. warpage / voids 偵測尚屬次要方向**
現有代表論文集中於接合製程（bonding）而非 post-bonding 缺陷偵測（void、delamination）。若合作需求是 X-ray + DL void detection，需評估是否技術匹配。

### 4.3 具體合作題目建議

**題目一：CoWoS Hybrid Bonding 接合強度線上量測 AI 系統**
- 對應技術：微電化學感測模組 + LSTM 預測平台
- 合作形式：共同申請科部產學合作計畫 / 委託研究
- 交付物：產線可用之即時監控模組 + 品質預測 dashboard
- 適合對象：台積電 AP 部門、ASE 先進封裝事業群

**題目二：SoIC 封裝 Warpage AI 量測補正系統**
- 對應技術：DIC（數位影像關聯法）+ Deep Learning 熱氣流擾動補正
- 合作形式：與 KLA / Onto Innovation 等量測設備商合作，NCHU 提供 AI 算法模組
- 交付物：DL-DIC 補正模型 + 工具軟體 API
- 近期可對標：Nature Microsystems & Nanoengineering 2024 同類研究

**題目三：3D 封裝界面材料表面改質量產製程轉移**
- 對應技術：VUV / HCOOH 大氣壓表面改質 + 電化學即時 QC
- 合作形式：技術授權 + 製程顧問
- 適合對象：封測廠（日月光、矽品）導入 Hybrid Bonding 生產線時的前處理模組採購
- 核心優勢：免真空、可常壓操作，設備投資門檻低

---

## 5. 資料來源清單

| 序號 | 來源 | URL | 訪問日期 |
|------|------|-----|---------|
| 1 | NCHU MSE 宋振銘中文教師頁面 | https://www.mse.nchu.edu.tw/zh_tw/members/teacher/-%E5%AE%8B%E6%8C%AF%E9%8A%98-69623319 | 2026-04-22 |
| 2 | NCHU MSE 宋振銘英文教師頁面 | https://www.mse.nchu.edu.tw/en/members/teacher/Jenn-Ming-Song-69623319 | 2026-04-22 |
| 3 | NCHU 新聞：AI賦能先進封裝智慧量測平台 | https://www2.nchu.edu.tw/news-detail/id/60924 | 2026-04-22 |
| 4 | NCHU 新聞：研發長媒體專訪（永續 DNA） | https://www2.nchu.edu.tw/news-detail/id/58021 | 2026-04-22 |
| 5 | ScienceDirect 作者頁面（論文列表） | https://www.sciencedirect.com/author/57154837200/jenn-ming-song | 2026-04-22 |
| 6 | NCHU MSE 2024 i-ONE 儀器獎公告 | https://www.mse.nchu.edu.tw/zh_tw/news/news109/2024%E5%B9%B4-%E7%AC%AC16%E5%B1%86%E5%9C%8B%E7%A0%94%E7%9B%83i-ONE%E5%84%80%E5%99%A8%E7%A7%91%E6%8A%80%E5%89%B5%E6%96%B0%E7%8D%8E-84016146 | 2026-04-22 |
| 7 | NCHU 產學合作流程（NCHUGLORIA） | https://nchugloria.com/index.php?id=257&index=4&lang=cht&option=module&task=pageinfo | 2026-04-22 |
| 8 | PMC：AI warpage 預測平台論文（Micromachines 2025） | https://pmc.ncbi.nlm.nih.gov/articles/PMC11945037/ | 2026-04-22 |
| 9 | CCNRIA 宋振銘成員頁面 | https://sites.google.com/email.nchu.edu.tw/ccnria（需登入）| 2026-04-22 |
| 10 | NCHU 中興大學官方新聞（2024台灣創新技術博覽會） | https://www.cna.com.tw/postwrite/chi/384626 | 2026-04-22 |

---

## 快速結論摘要

**隱形綁定：** 無。研發長職務本身不排他，NCHU 智財框架彈性，無 TSMC / ASE 排他合約跡象。

**技術成熟度：** Cu-Cu 直接接合 + 表面改質已達 TRL 4-5（未來科技獎認證），AI 量測平台功能完整但仍在精進整合。

**合作最大變數：** 行政時間（研發長）壓縮 PI 投入；AI 模組依賴跨校協作。

**最佳切入點：** 以「CoWoS Hybrid Bonding 線上量測 AI」或「表面改質製程技術授權」作為第一合作，明確分工 + 約定宋的指導時間比例。

**整體評定維持：🟢 Open — 值得優先接觸。**
