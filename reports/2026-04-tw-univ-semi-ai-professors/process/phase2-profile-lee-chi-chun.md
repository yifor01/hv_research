# Phase 2 Deep Profile: 李祈均 (Chi-Chun Lee / Jeremy Lee)

**研究日期**：2026-04-22
**建檔類型**：Phase 1 盲點補強（Speech/Affective Computing 與半導體製造 AI 的隱性橋接）
**隱形綁定風險評估**：🟡 黃燈（NVIDIA 聯合中心、京元電子顧問角色需澄清）
**校/系/職級**：NTHU 電機系 副教授；NTHU-NVIDIA Joint Innovation Center 副主任；京元電子技術顧問（2025-2026）
**對應 T 類別**：T2c(製程控制/SPC)、T4a(AI 基礎)、T4b(類神經晶片) —— **間接且弱相關**

---

## ⚡ 結論先行

| 項目 | 評估 |
|------|------|
| **隱形綁定等級** | 🟡 中等風險（NVIDIA、京元雙重角色） |
| **T 類別覆蓋** | T2c(製程 SPC)、T4a(AI 框架)、T4b(Neuromorphic) —— 弱相關 |
| **半導體契合度** | 35% —— 基於 NVIDIA 聯合中心副主任身份，實質研究內容距離遠 |
| **技術星級** | ⭐⭐⭐⭐ 國際優秀（h=36，10.9k 引用，Speech/Affective 頂尖） |
| **學生工程素養星級** | ⭐⭐⭐⭐ 優秀（Interspeech 冠軍、應用導向） |
| **合作可行性** | 🟡 中等可行（時間競爭、企業身份衝突） |
| **建議 Tier** | **Tier-2（條件式）** —— 若以健康分析/多模型 AI 系統為主軸 |

---

## §1 隱形綁定檢查

### 1.1 企業綁定

**NVIDIA 聯合中心副主任身份** ⚠️：
- 正式角色：NTHU-NVIDIA Joint Innovation Center Deputy Director
- 設立時間：2023 年底
- 實際影響：不確定是否涉及排他協議或高度時間承諾
- 搜尋結果未見 NVIDIA 全職合約，推測為兼任
- 風險等級：**🟡 中等**（需直接詢問合約範圍）

**京元電子(KYEC)技術顧問** ⚠️：
- 任期：2025-2026（最近才上任）
- 身份：Technical Advisor（顧問，非董事/獨佔關係）
- 京元電子：全球最大純測試服務商（Probing & Final Test），非設計/製造廠
- 與 TSMC/MTK 關係：下游客戶，無直接競爭
- 風險等級：**🟡 低-中等**（時間承諾不明）

**TSMC / MTK / UMC**：
- 論文中無這些廠商 acknowledgments
- Affective Computing/Speech 與晶片設計無直接合作需求
- 風險等級：✓ 綠燈

### 1.2 政府/學術綁定

**2024 NSTC 傑出研究獎** ✓：
- 確認獲獎
- 研究主題：「Humans as Intricate Systems」—— Multimodal signal processing + Affective computing
- 無排他性

**2025 NTHU-Novatek Distinguished Talent Chair** ✓：
- 正式身份確認
- 由 NTHU 內部獲得，無外部企業獨佔

**2025 CIEE Outstanding EE Professor** ✓：
- 確認獲獎（根據搜尋結果提及「114 年度」= 2025）
- 教學/研究卓越認可

### 1.3 論文 Acknowledgments 資金來源（近 3 年）

**主要研究基金**（推測）：
- NSTC 基礎研究計畫（確認）
- NVIDIA 聯合中心資金？（未見明確提及）
- 美國 NIH/NSF（基於國際合作者 Shrikanth Narayanan 之 USC 背景，可能涉及）
- NTHU 內部經費

**未見獨佔條款風險**，但 NVIDIA 資金占比不明 ⚠️

### 1.4 結論

**🟡 黃燈 —— 中等風險**

主要隱憂：
1. **NVIDIA 聯合中心副主任身份** —— 需澄清是否有時間/IP 歸屬限制
2. **京元電子新上任顧問** —— 時間承諾與利益衝突評估不足
3. 若兩角色時間占用超過 20-30%，可用於聯合研究的時間受限

**建議**：初期合作前，應簽署利益衝突聲明(COI Disclosure)，確認：
- NVIDIA 聯合中心是否排斥與其他半導體廠的合作
- 京元電子顧問工作預期工時
- IP 歸屬權（NTHU vs. 企業）

---

## §2 技術契合度

### 2.1 現任職務與實驗室

**職位**：
- 國立清華大學電機工程學系 副教授 (Associate Professor)
- NTHU-NVIDIA Joint Innovation Center 副主任 (Deputy Director)
- 京元電子股份有限公司 技術顧問 (Technical Advisor, 2025-2026)

**Lab 名稱與規模**：
- **BIIC Lab** = Behavioral Informatics & Interaction Computation Lab
- **暱稱**：人本訊號運算研究室（中文官方名稱）
- **規模**：約 12-18 人（基於官網「多位博士生、碩士生、博後」描述）
- **位置**：NTHU 電機系（確切樓棟未見公開）

### 2.2 研究主題 × 半導體 T 類別命中度

| T 類別 | 研究主題 | 命中度 | 說明 |
|--------|---------|--------|------|
| T1 - 晶片設計 | 無相關 | ❌ 0% | — |
| T2a - 製程工藝 | 無相關 | ❌ 0% | — |
| T2b - 視覺檢測 | 無相關 | ❌ 0% | Speech/Affective 非視覺領域 |
| T2c - 製程控制 | **(弱相關)** 健康監測 → 製程異常偵測？ | ⚠️ 15% | 極牽強，無具體應用 |
| T3a - 材料/物理 | 無相關 | ❌ 0% | — |
| T3b - 製程模擬 | 無相關 | ❌ 0% | — |
| T3c - 工藝控制 | 無相關 | ❌ 0% | — |
| T3d - 電路設計 | 無相關 | ❌ 0% | — |
| T4a - AI 基礎框架 | **Multimodal ML、Deep Learning、Signal Processing** | ✅ 65% | 核心強項，但應用領域外 |
| T4b - 類神經晶片 | **(推測)** 邊緣 AI 晶片上的情感計算 | ⚠️ 25% | 無明確論文記錄，純推測 |

**綜合評估**：**35% 半導體契合度** —— 主要依靠 T4a (AI 基礎框架)，T4b 純粹推測，無 T2/T3 直接相關

### 2.3 Google Scholar 指標

| 指標 | 數值 |
|------|------|
| **h-index（全量）** | 36 |
| **h-index（近 5 年）** | 28 |
| **總引用數** | 10,958 |
| **近 5 年引用數** | 7,514 |
| **i10-index** | 111 |
| **驗證時間** | 2026-04-22 |

**評價**：國際優秀水準（Speech/Affective 領域 h=36 為一流），近年保持高速引用成長

**關鍵論文**（累計引用排序）：
1. 「IEMOCAP: Interactive Emotional Dyadic Motion Capture Database」—— **5,526 引用**（感情識別領域標準數據集）
2. 「Emotion Recognition from Speech」(sentiment/affective) —— **608 引用**
3. 「Autism Spectrum Disorder 診斷應用」—— **339 引用**

### 2.4 2024-2026 代表論文

基於 Interspeech 2025、ICASSP 2024-2025 論文清單統整：

| 年份 | 標題 | 期刊/會議 | 半導體關聯 | 說明 |
|------|------|----------|----------|------|
| 2025 | ZSDEVC: Zero-Shot Diffusion-based Emotional Voice Conversion | Interspeech 2025 | ❌ 無 | 語音情感合成 |
| 2025 | Defend for Self-Vocoding: Enhanced Decoder for Watermark Recovery | Interspeech 2025 | ❌ 無 | 音頻防偽 |
| 2025 | Lessons Learnt: Revisit Key Training Strategies for Speech Emotion Recognition in the Wild | Interspeech 2025 | ❌ 無 | 情感識別最佳實踐 |
| 2025 | Mask Augmentation For Tumor Classification In Medical Images | ICASSP 2025 | ⚠️ 弱 | 醫療影像 AI（可能涉及邊緣計算） |
| 2024 | Balancing Speaker-Rater Fairness for Gender-Neutral Speech Emotion Recognition | ICASSP 2024 | ❌ 無 | 性別公平性 |
| 2025+ | (多篇) Zero-shot SER using LLM、Noise-robust SER、Cross-corpus SER | ICASSP 2025 | ❌ 無 | 語音情感識別應用 |

**評價**：論文全數在 Speech/Affective/Health 領域，**零直接半導體應用**

### 2.5 產業合作紀錄

**NVIDIA 聯合中心（正式）**：
- 角色：Deputy Director
- 專案內容：未見具體論文或技術產出公告
- 推測方向：邊緣 AI、多模態深度學習在實時應用中的優化

**京元電子（新任）**：
- 角色：Technical Advisor (2025-2026)
- 潛在應用場景：
  - 晶圓測試流程最佳化（製程控制 SPC？）
  - 測試機台異常偵測（時間序列 anomaly detection）
  - 良率預測模型
- **實際貢獻**：未見論文或公開案例

**其他產業合作**：
- 無明確 TSMC/MTK/UMC/Micron 合作論文
- 與海外大廠（Google、Meta、Apple）的語音/情感 AI 合作未見公開

---

## §3 學生工程素質 & Lab 文化

### 3.1 Lab 規模與結構

**BIIC Lab 規模**：
- 約 12-18 人（官網描述「多位博士/碩士生」）
- 明確組織：
  - 博士生組（Speech Processing 主軸）
  - 碩士生組（應用導向：Autism、Health）
  - 博後/訪問學者（國際合作）

**內部結構**：
- PI (Principal Investigator)：李祈均
- Research Focus：Speech、Affective、Health Analytics、Multimodal Learning
- 協作單位：NTHU 其他系院（心理系、音樂系等）

### 3.2 GitHub / 開源 / 工程實踐

**未找到官方 GitHub 組織**。  
**推論**：
- 學術論文為主（Interspeech/ICASSP）
- 可能有閉源工具（情感識別模型、IEMOCAP 擴展版）
- 開源貢獻度低

### 3.3 學生競賽與論文獎項

**Interspeech Emotion Challenge**：
- **2009 年冠軍**（最早期）
- **2019 年冠軍**（近期）
- 說明：BIIC Lab 在語音情感識別領域有長期領先地位

**Best Paper / Oral Nominations**：
- ICASSP 2024/2025 多篇論文入選（根據搜尋結果）
- Interspeech 2025 多篇接受（5+ 篇論文）

**評價**：學生論文產出質量高，國際競爭力強

### 3.4 畢業生流向（LinkedIn 推估）

**未直接搜尋**，但推測：
- Speech/Affective 背景 → Google、Amazon Alexa、Apple Siri、Meta (Llama) 語音團隊
- Health Analytics → 醫療科技新創、NHS 等公衛機構
- 台灣：鴻海、廣達、緯創等語音 AI 相關部門

**NVIDIA 聯合中心關係** → 部分畢業生可能進入 NVIDIA 台灣辦公室

### 3.5 業界實習紀錄

**未在搜尋中明確發現具體實習計畫**。  
**推論**：
- 與 NVIDIA 聯合中心可能有聯合實習機會
- 與京元電子（新任顧問）可能啟動實習計畫（待觀察）
- 建議直接詢問教授

---

## §4 合作優缺點 & 建議

### 4.1 優點（3 點）

1. **AI 基礎框架能力超強（Multimodal ML、Deep Learning）**
   - 近期論文涵蓋：Diffusion Model (ZSDEVC)、LLM + Speech (Zero-shot SER)、Medical Imaging AI
   - T4a (AI 基礎框架) 與半導體 AI 工具、邊緣計算高度相關
   - 可為製程監控 SPC、異常檢測等系統提供演算法基礎

2. **NVIDIA 聯合中心副主任身份 —— 近距離台積電/半導體關係**
   - 與 NVIDIA 深度學習框架(CUDA、TensorRT) 生態同步
   - 可引入 NVIDIA 的製程 AI 解決方案經驗
   - 易於組織 NTHU-NVIDIA 聯合研發

3. **Interspeech 冠軍級研究水準 + 應用導向**
   - 不只論文，還有「可部署模型」(IEMOCAP 資料集)
   - Autism 診斷、健康監測等實際應用經驗
   - 易於轉化為製程監控應用案例

### 4.2 缺點 / 潛在風險（3 點）

1. **半導體 domain knowledge 完全缺失**
   - 論文 0% 涉及晶片設計、製程、工藝
   - 從 Speech → 製程控制的跨越極大（需 6-12 個月培訓）
   - 風險：時間投資高，效率損耗大

2. **企業身份衝突 —— NVIDIA vs. 京元電子**
   - NVIDIA 重視 AI 軟體、晶片設計（與製造無關）
   - 京元電子重視後段測試製程（與 NVIDIA 重心差異大）
   - 風險：若同時服務兩方，易陷入利益衝突或時間競爭
   - 建議：需明確 COI Disclosure

3. **Lab 方向與半導體距離遠，人才轉向困難**
   - 12-18 位學生多數背景為訊號處理、語言學、心理學
   - 轉向半導體 SPC/異常檢測需完整再訓練
   - 風險：無法直接利用現有 Lab 人才，需外招

### 4.3 建議合作型態

**A. AI 框架層級（推薦）**
- 題目：「邊緣 AI 與多模態感測在智慧製程控制中的應用」
- 合作方：NTHU (李祈均) + NVIDIA Taipei + 京元電子
- 合作方式：
  - NVIDIA 提供硬體平台 (Jetson, CUDA)
  - 李祈均 Lab 負責深度學習模型（遷移學習：Speech SER → Anomaly Detection）
  - 京元電子提供測試製程數據、驗證場景
- 期程：12-18 個月
- 預期產出：邊緣 AI 製程監控系統 v1.0
- 經費：3-5 百萬台幣

**B. 健康分析延伸（次選）**
- 利用李祈均的「健康監測」領域優勢
- 題目：「設備健康度預測與故障預警」(Equipment PHM = Prognostics & Health Management)
- 合作方：京元電子（專門化應用）
- 風險：話題度不如 AI 框架

**C. NVIDIA 聯合中心正式項目（長期視野）**
- 利用 Deputy Director 身份
- 與 NVIDIA Research 共同設計邊緣 AI 製程應用
- 發表聯合論文（NVIDIA + NTHU）
- 吸引後續業界投資

**D. 不推薦：純顧問角色**
- 京元電子顧問身份已足，不需再增加無酬承諾

### 4.4 首次破冰建議

**破冰切入點**：聯合中心副主任身份 + 新任京元顧問身份的協同

**具體郵件草稿**：

```
Subject: 合作機會探討——邊緣 AI 與製程控制的應用

親愛的李教授：

我注意到您最近獲得 NTHU-Novatek Distinguished Talent Chair、NSTC 傑出研究獎，
以及擔任 NTHU-NVIDIA 聯合中心副主任一職。尤其是您在多模態深度學習與邊緣計算的專長，
結合 NVIDIA 的硬體生態，我認為存在一個極具潛力的應用場景。

根據京元電子（您新任技術顧問）的業務特性，晶圓測試流程中存在大量時間序列數據：
- 機台運行參數（溫度、電流、時序）
- 良率波動、異常失效模式
- 這些數據的實時異常偵測與預測目前仍依賴傳統統計方法

您的 BIIC Lab 在「多模態訊號分析與異常檢測」領域（如 Autism 診斷、Health Analytics）
具有業界領先的演算法能力。這些方法可直接遷移到製程監控（SPC/Anomaly Detection）。

我們初步規劃一項聯合研究計畫：
- **題目**：「邊緣 AI 與多模態感測在智慧晶圓測試製程中的應用」
- **合作方**：NTHU (您 + BIIC Lab) + NVIDIA Taipei + 京元電子
- **期程**：2026-2027 (18 個月)
- **預期產出**：
  1. 製程異常偵測模型（基於 LSTM/Transformer）
  2. 邊緣部署版本（NVIDIA Jetson）
  3. 聯合論文 (ICML/IJCAI/NeurIPS 多模態/邊緣 AI track)

我們認為此計畫符合您的研究方向（多模態深度學習）、機構身份（NVIDIA 聯合中心）、
以及新興顧問角色（京元電子），且無利益衝突。

近期是否方便線上或面對面討論？我們亦可提供京元電子的製程數據樣本（含適當保密協議）供評估。

敬祝安康
[Your Name]
```

**破冰重點**：
- 突出「多模態訊號分析 → 製程監控」的概念遷移（他會認可）
- 強調 NVIDIA 聯合中心的整合機會（他樂見）
- 與京元新顧問角色的協同（自然、無衝突）
- 保證聯合論文機會（符合教授身份）

---

## §5 最終評估

| 維度 | 分數 | 說明 |
|------|------|------|
| 技術深度 | ⭐⭐⭐⭐ | h=36、10.9k 引用，Speech/Affective 領域國際一流 |
| 半導體契合度 | ⭐⭐ | 主要依靠 T4a，無 T2/T3 直接經驗，需完整轉向 |
| 學生工程素養 | ⭐⭐⭐⭐ | Interspeech 冠軍、應用導向、多篇 ICASSP 論文 |
| 可用時間 | ⭐⭐⭐ | 副教授 + NVIDIA deputy + 京元顧問，時間承諾不明 |
| 綁定風險 | ⭐⭐⭐ | NVIDIA/京元雙重角色，需 COI Disclosure |
| **總評** | **Tier-2（條件式）** | **若專注於 AI 基礎框架 + 邊緣計算應用，可行** |

### 總結評語

李祈均是 NTHU 電機系的新星教授，在多模態深度學習、訊號處理、情感/健康分析領域國際領先（h=36）。
其最大優勢是 NVIDIA 聯合中心副主任身份與京元電子新任顧問角色，**但核心研究內容與半導體製造 AI 的距離最遠**。

**Tier-2 評級根據**：
- ✅ AI 框架能力強（T4a），可支撐邊緣 AI 應用
- ✅ NVIDIA 聯合中心副主任提供協調優勢
- ✅ 與京元電子的顧問身份無衝突（反而可協同）
- ❌ 無 T2/T3（製程、工藝）經驗，跨域成本高
- ❌ Lab 人才背景與半導體距離遠

**合作可行**，但必須：
1. ✅ 明確簽署利益衝突聲明（COI Disclosure）確認 NVIDIA/京元時間承諾
2. ✅ 合作內容鎖定在「AI 框架層級」（多模態異常檢測）而非「製程深度優化」
3. ✅ 與京元電子建立聯合研究框架，提供實際製程數據與驗證場景

若專注於「邊緣 AI + 製程監控」而非「晶片設計」，李祈均可成為 T4a 層級的合作夥伴，
但不應期待他在 T1-T3 領域有深度貢獻。

---

## §6 資料來源

- [李祈均 Google Scholar Profile](https://scholar.google.com/citations?user=MGqWqOAAAAAJ&hl=en)
- [BIIC Lab - NTHU 官方網站](https://biic.ee.nthu.edu.tw/)
- [BIIC Lab 成員頁面](https://biic.ee.nthu.edu.tw/biicers.php)
- [NTHU 研究者 Hub — 李祈均](https://khub.nthu.edu.tw/researcherProfile?uuid=82D26611-203C-41C4-8287-123E52C6DBAA)
- [2024 NSTC 傑出研究獎 — 李祈均](https://web.nstc.gov.tw/cen/oaa/award_112/Chi-Chun-Lee.html)
- [NTHU-NVIDIA Joint Innovation Center](https://nvidia.site.nthu.edu.tw/)
- [NTHU Tsing Hua Talent Development Fund 2025](https://nthu-en.site.nthu.edu.tw/p/406-1003-285385,r4806.php)
- [Interspeech 2025 接受論文清單](https://www.isca-archive.org/interspeech_2025/)
- [DBLP — Chi-Chun Lee](https://dblp.org/pid/99/8062.html)
- [APSIPA — Introduction to Chi-Chun Lee and BIIC Lab](https://apsipa-us.org/2021/10/22/introduction-to-professor-chi-chun-jeremy-lee-and-his-lab-at-university-of-national-tsing-hua/)
