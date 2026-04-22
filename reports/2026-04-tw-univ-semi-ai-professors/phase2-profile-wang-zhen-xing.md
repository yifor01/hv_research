# Phase 2 深度 Profile — 王振興 Jeen-Shing Wang（NCKU 電機，AI數位轉型中心主任）

**研究日期**：2026-04-22
**Phase 1 評級**：T6 🟢 Open

---

## 一、基本資料確認

| 欄位 | 內容 |
|------|------|
| 中文姓名 | 王振興 |
| 英文姓名 | Jeen-Shing Wang（注意：非 Zhen-Xing，官方英文名為 Jeen-Shing） |
| 現職 | NCKU 電機工程學系 特聘教授（Distinguished Professor，since 2015） |
| 行政職 1 | AI 數位轉型研究中心（AI4DT）主任兼執行長（since 2019） |
| 行政職 2 | NCKU 心臟醫療器材科學研究中心主任（since 2013） |
| 學歷 | Ph.D. Electrical & Computer Engineering, Purdue University；M.S./B.S. University of Missouri-Columbia |
| 實驗室 | 計算型智慧與學習系統實驗室（Computational Intelligence and Learning Systems Laboratory，R92810） |
| 聯絡分機 | 62378 |
| 中心網站 | http://ai4dt.ee.ncku.edu.tw/ |

---

## 二、隱形綁定檢查 ⚠️

### AI數位轉型中心（AI4DT）vs. 廣達–成大聯合AI研究中心

**關鍵區分**：王振興主導的「AI4DT 人工智能數位轉型研究中心」與另一個「廣達–成大聯合AI研究中心（Quanta-NCKU Joint AI Research Center）」是**兩個不同單位**。

- **廣達–成大 Joint AI Research Center**：2021 年由 NCKU 校長蘇慧貞與廣達董事長林百里簽署 MOU，2023 年 12 月 15 日正式揭牌。現任主任為**林一平（Yi-Bing Lin）**教授。研究主軸：Smart Healthcare、Smart Campus、Smart Agriculture。王振興**不在**此中心領導層。
- **AI4DT 中心**：王振興自 2019 年起擔任主任兼執行長。屬 NCKU 電機系內設中心，**非廣達冠名**。聯絡電話 06-208-9602/9603，信箱 aisnd@incku.com。

**結論**：王振興的「AI數位轉型中心主任」頭銜**不是廣達冠名職**，為 NCKU 電機系自設中心，不存在廣達隱形綁定。

### TSMC 綁定檢查

NCKU 與台積電雖有「台積電–成大聯合研發中心（NCKU-TSMC R&D Center）」，主要聚焦前瞻半導體製程。公開資料未見王振興列名為該中心成員或顧問。其研究主線（生醫訊號、照明、AIoT）與半導體製程研發無直接交集。**無台積電隱形綁定跡象**。

### LinkedIn / 兼職

公開資料未查到王振興在任何企業掛職顧問或獨立董事。其 Facebook 帳號用於媒體聯繫，無 LinkedIn 掛職紀錄可見。

### 論文致謝

現有文獻未出現廣達、台積、工研院的致謝標記。近年論文致謝主要來自 NSTC（國科會）計畫補助，以及心臟醫療器材中心的醫院合作（如透析患者資料集）。**無企業隱形綁定**。

**隱形綁定風險評估：低**。AI4DT 中心是 NCKU 自設，非廣達或台積冠名。產學合作主要在醫療領域（腹膜透析、人工動靜脈廔管）。

---

## 三、技術契合度

### 研究關鍵字 Fingerprint（來自 NCKU Research Output 資料庫，137 篇著作）

| 技術 | 比重 |
|------|------|
| Neuro-fuzzy systems | 100%（核心） |
| Recurrent neural networks（LSTM/RNN） | 56% |
| Feature extraction | 48% |
| Clustering algorithms | 46% |
| Wearable devices & physiological signal | 主軸 |
| AIoT（邊緣推論、感測融合） | 成長中 |
| CNN（影像分類） | 應用層 |

### 2023–2026 代表論文（5 篇）

1. **"Smart Lighting and Mindfulness Interventions: Pathways to Better Health and Learning in High School Education"**（2026 accepted, *Journal of Sleep Research*）
   — 人因照明 + 身心健康，跨 AIoT 光控系統

2. **"AI literacy and gender equity in elementary education: A quasi-experimental study of a STEAM–PBL–AIoT course"**（2025, *International Journal of STEM Education*，3 citations）
   — AIoT 教育應用，強調 STEAM–PBL 整合

3. **"Smart lighting intervention on sleep quality and neurochemical markers in high school students"**（2025）
   — 智慧照明 × 神經化學指標，可穿戴感測 + 光照控制

4. **"AI-Based Multi-Objective Optimization Algorithm for Intelligent School Lunch Menu Planning System"**（2024）
   — AI 多目標最佳化，可見 RL/進化演算法思路

5. **"Automated Model Generation for Arteriovenous Shunt Stenosis Detection Using Machine Learning Algorithms"**（2024）
   — 醫療 ML：動靜脈廔管狹窄自動偵測，臨床 AI

### 應用領域比例估算

| 領域 | 比重估算 |
|------|---------|
| 醫療生醫（心腎、透析、ECG、睡眠） | ~50% |
| 照明 / 人因環境（AIoT 光控） | ~25% |
| 教育 AI（AI 素養、STEAM） | ~15% |
| 工業/半導體 | ~5%（邊緣） |
| 運動健康（智慧羽球、穿戴式） | ~5% |

**半導體應用比例極低**（約 5%，僅學習系統晶片設計方向有沾邊）。主要優勢在**生醫訊號 + AIoT 感測融合 + 人因環境控制**。

### CNN / RL 使用情況

- **CNN**：用於 ECG 情緒辨識、廔管影像偵測、生理訊號分類，屬應用層工具，非底層創新。
- **RL**：間接出現在多目標最佳化（演化計算 + 強化思路），無純 RL/DRL 論文可見。
- **邊緣推論（Edge Inference）**：AIoT 課程中提及，但技術深度不明確；Lab 無 FPGA / MCU 加速的論文。

---

## 四、學生工程素質

### Lab 規模

「計算型智慧與學習系統實驗室」規模：公開資料顯示碩博士生皆有，推估在籍 10–20 人（成大電機系中型 Lab 常見規模）。精確人數無公開資料。

### 學生競賽紀錄

- NCKU 教師個人頁面提及**多次 Microsoft Imagine Cup 勝出**及**嵌入式系統競賽獲獎**。
- **國科會未來科技獎（2023、2024 連續兩年）**：代表整體研究成熟度高，有轉化潛力。
- 2020 年中國工程師學會**傑出工程教授獎**：顯示教學與實作並重。
- 無 AICUP / Quanta Cup 的具體得獎紀錄出現在公開搜尋結果。

### GitHub / 開源

公開資料未見 GitHub 開源 repo 與 Lab 連結。專利方向（穿戴式運動分析、智慧手錶、情緒調節系統、羽球訓練設備）顯示技術傾向**內部轉化成專利/商品**而非開源。

### 畢業生去向

無公開 alumni tracking 資料。從研究主題推斷：
- 醫療 AI 方向 → 醫材公司、醫院資訊系統（如富邦、奇美醫）
- AIoT / 穿戴裝置 → 廣達（設備端 AI）、緯創、工研院電光所
- 教育 AI → EdTech 新創

**未見台積電相關畢業生去向記錄**。

---

## 五、合作優缺點 & 建議

### 優點

1. **中心主任 = 制度對接快**：AI4DT 中心有正式組織、電話、email、辦公空間。王振興身為主任，可直接代表 NCKU 電機簽署 MoU 或產學合約，**行政摩擦小**。
2. **雙中心主任（AI4DT + 心臟醫材中心）**：跨域連結能力強，若半導體公司有穿戴式健康監測需求（如 TSMC 廠區員工健康管理），可快速媒合。
3. **國科會未來科技獎連兩年（2023–2024）**：代表研究有商業化潛力，合作方資源較易進場。
4. **無隱形綁定**：與廣達、台積無冠名限制，合作空間開放。

### 缺點

1. **半導體製程直接相關度低**：研究主線在生醫 + 照明 + 教育，與前段製程（光刻、良率 AI）、後段封測（AOI、缺陷檢測）的對接需要「轉譯」工作。
2. **硬體深度有限**：Lab 著重演算法（neuro-fuzzy、LSTM、CNN），FPGA / ASIC 自設計比重不高；若需求在晶片端 AI 加速，需找其他合作教授補強。
3. **RL 能力待確認**：Phase 1 標記「RL」為強項，但近年論文以監督式學習為主；RL 應用在多目標最佳化屬間接使用，深度 RL 論文未見。
4. **AIoT scope general**：AIoT 應用場景廣但分散（校園、醫院、運動），對半導體廠的「垂直深入」需求（如 CMP 終點偵測、蝕刻異常 RL 控制）可能需要 6–12 個月爬坡。

### 3 個具體合作題目

**題目 A：AIoT 穿戴式生理感測 SoC 功耗最佳化**
- 背景：王振興在穿戴式裝置 + 生理訊號有深厚積累，但缺少晶片端設計合作。
- 合作模式：半導體公司提供低功耗 SoC 設計需求（ECG / PPG AFE），Lab 提供演算法壓縮（neuro-fuzzy edge inference）。
- 預期產出：IEEE ISSCC / JSSC 等級晶片論文 + 穿戴式原型。

**題目 B：半導體廠人因照明 AI 控制系統**
- 背景：王振興在「人因照明 × 睡眠 × 認知表現」有 2023–2026 連續論文，契合半導體廠三班制員工疲勞管理需求。
- 合作模式：台積電/聯電廠區作為場域，AI4DT 中心導入智慧光控系統，Lab 負責訊號監測 + RL 亮度調適。
- 預期產出：廠區 pilot 報告 + IEEE T-ITS 或 Journal of Sleep Research 論文。

**題目 C：AV Shunt / 透析患者 AI 預測模型 × 晶片邊緣部署**
- 背景：2024 年已有「廔管狹窄自動偵測 ML 模型」論文，臨床資料來自成大附設醫院。
- 合作模式：半導體公司（如聯發科、奇景）提供醫療邊緣 AI 晶片（e-Health SoC），Lab 負責模型 TinyML 化 + 臨床驗證。
- 預期產出：醫材 510(k)/TFDA 路徑可行性報告 + 邊緣部署論文。

---

## 六、綜合評分

| 維度 | 評分（1–5） | 說明 |
|------|------------|------|
| 技術契合度（半導體） | 2.5 | 需轉譯；生醫 AIoT 強，製程 AI 弱 |
| 學生工程素質 | 3.5 | 競賽得獎紀錄，演算法能力強，硬體一般 |
| 行政對接便利性 | 4.5 | 雙中心主任，制度成熟，無隱形綁定 |
| 隱形綁定風險 | 低 | AI4DT ≠ 廣達冠名；無台積電限制 |
| 整體合作建議 | **有條件推薦** | 適合生醫 AIoT 或廠區人因系統合作；純半導體製程 AI 非首選 |

---

## 七、資料來源清單

| 來源 | URL | 訪問日期 |
|------|-----|---------|
| NCKU EE 教師個人頁面 | https://www.ee.ncku.edu.tw/teacher/index2.php?teacher_id=36 | 2026-04-22 |
| NCKU Research Output（Jeen-Shing Wang） | https://researchoutput.ncku.edu.tw/zh/persons/jeen-shing-wang/ | 2026-04-22 |
| TechNice 專家介紹 | https://www.technice.com.tw/experts/173848/ | 2026-04-22 |
| AI4DT 成大人工智能數位轉型研究中心 | http://ai4dt.ee.ncku.edu.tw/ | 2026-04-22（timeout） |
| NCKU 廣達–成大聯合AI研究中心 揭牌新聞 | https://web.ncku.edu.tw/p/406-1000-262411,r3529.php?Lang=en | 2026-04-22 |
| NCKU 廣達–成大聯合AI研究中心 官方 | https://quantaai.web2.ncku.edu.tw/ | 2026-04-22（404） |
| IEEE Xplore Author Profile | https://ieeexplore.ieee.org/author/37336786900 | 2026-04-22（418 blocked） |
| Springer — AIoT STEM 論文 2025 | https://link.springer.com/article/10.1186/s40594-025-00574-y | 2026-04-22 |
