# Phase 2 深度 Profile：連震杰 Jenn-Jier James Lien

**撰寫日期：** 2026-04-22
**資料狀態：** 基於網路公開資料；部分欄位（NSTC 計畫細節、學生人數、專利清單）受限於資料可及性，標注「查無直接來源」

> **Phase 1 名稱備注：** Phase 1 紀錄為「連仁傑」，實際正確全名為 **連震杰（Jenn-Jier James Lien）**，英文慣用名 James Lien。資料驗證確認為同一人。

---

## 基本資訊

| 欄位 | 內容 |
|------|------|
| 姓名 | 連震杰（Jenn-Jier James Lien） |
| 現職 | 國立成功大學（NCKU）資訊工程學系 教授 |
| 行政職 | 電機資訊學院副院長（Vice Dean）；成功大學 AI 機器人學位學程主任（2020 起） |
| 辦公室 | 新工館 11F 65B12；機器人實驗室 9F 65904 |
| Email | jjlien@csie.ncku.edu.tw |
| 電話 | 06-2757575 ext 62540 |
| 學歷 | Ph.D. 電機工程，University of Pittsburgh（1993-1998）；M.S. 電機工程，Washington University（1991-1993）；B.S. 生醫工程，中原大學（1985-1989） |
| 實驗室 | [Robotics Laboratory](http://robotics.csie.ncku.edu.tw/) |

---

## 1. 隱形綁定檢查 ⚠️

### 1.1 與半導體龍頭企業的直接綁定

| 查詢對象 | 搜尋結果 | 判斷 |
|---------|---------|------|
| TSMC / 台積電 | 查無 Lien 個人與台積電直接合作記錄；NCKU 整體有 TSMC JDP 計畫，但無法確認 Lien 個人參與 | 無直接證據 |
| 日月光（ASE） | 2024 年一篇 NCKU AOI 論文（OANet）由 Institute of Data Science 發表，ASE 贊助，但主要作者為 Chih-Chung Hsu 等人，**Lien 並非作者** | 無直接綁定 |
| LinkedIn 兼職 | 查無公開記錄 | 無直接證據 |
| Applied Materials / Camtek / KLA 等設備商 | 查無明確論文致謝或合作案 | 無直接證據 |

**已知非半導體設備商合作：**
- **Intel** + **Qisda（廣達）**：2021 年起，5G 場館 AI 應用、AR 擴增實境（IEEE Systems Journal 2022 論文）
- **JORJIN Technologies / Light Matrix Inc.**：5G 視覺深度學習與 AR 應用
- **成大醫學影像中心**：肺結節偵測（與 Chunghwa Telecom 合作）

**結論：隱形綁定風險低（🟢）**。無證據顯示 Lien 對特定半導體設備商有排他性顧問或股權關係。合作對象以 ICT 製造（Intel、Qisda）與醫療影像為主，不與 2nm 晶圓 AOI 直接衝突。

---

## 2. 技術契合度分析

### 2.1 研究指標（截至 2026-04）

| 指標 | 全期 | 近 5 年（2021 起） |
|------|------|-----------------|
| 總引用（Google Scholar） | 3,048 | 607 |
| H-index | 20 | 12 |
| i10-index | 35 | 13 |
| 總論文輸出（NCKU PURE） | 107 篇（56 會議 + 39 期刊 + 5 專利 + 30 完成計畫） | — |

*備注：Scholar profile 標示 Deep Learning & Computer Vision；NCKU 系統統計略有差異（h-index 16）*

### 2.2 核心研究方向

Lien 的機器人實驗室（Robotics Lab）自 2014 年起聚焦五大主軸：

1. **Deep Learning 演算法**（CNN、目標偵測、分類）
2. **視覺引導機器手臂**（Visual Servo、Grasping）
3. **自動光學檢測（AOI）**：2D + **3D AOI** 是顯著標誌
4. **立體視覺 + 結構光 3D 重建與量測**
5. **嵌入式電腦視覺系統**（CUDA、ARM 平台）

### 2.3 代表論文（2020-2026，AOI/3D 視覺相關）

| 年份 | 論文 | 期刊/會議 | 關聯度 |
|-----|------|-----------|--------|
| 2023 | 多篇 Sensors 論文：品質評估、幾何量測、缺陷偵測 | IEEE Sensors | ★★★★★ |
| 2023 | 肺結節分割（3D nnUNet）— 3D 視覺應用延伸 | ICECET 2023 | ★★★ |
| 2022 | PCB 對齊系統（RST Template Matching, CUDA 嵌入式 GPU） | IEEE Embedded Systems Letters | ★★★★ |
| 2022 | 5G 場館 AI（Intel + Qisda 合作） | IEEE Systems Journal | ★★ |
| 2020 | PCB 對齊系統，CUDA 嵌入式 GPU | Sensors | ★★★★ |

**關鍵洞察：** Lien 在 2023 Sensors 期刊上有多篇涵蓋幾何量測與缺陷偵測的論文，與半導體 AOI 的核心需求高度相符；PCB 對齊 + CUDA 嵌入式實作顯示其對量產環境的工程化能力。

### 2.4 3D AOI 技術具體細節

- **結構光（Structured Light）+ 立體視覺**：用於 3D 量測與重建，可擴展至晶圓翹曲（Warpage）、凸塊高度（Bump Height）、封裝基板缺陷等場景
- **深度學習缺陷分類**：CNN-based 偵測器（YOLO 衍生架構），搭配 False Positive 抑制模型（3D Channel-Spatial Attention）
- **嵌入式部署**：CUDA + ARM 邊緣運算，適合產線即時需求
- **視覺機器手臂整合**：多角度視角控制，自動翻轉取像，降低重新對焦需求（類 GMOC AOI 架構）

### 2.5 與 Phase 1 評定的驗證

Phase 1 標注 T3（3D AOI / 自動光學檢測）命中 ✅，驗證成立：
- 實驗室官網明列「Automatic Optical inspection」為核心研究方向
- 5 項專利中可能包含 AOI 相關專利（具體清單查無直接來源）
- 課程「電腦視覺及深度學習」與「機器學習及圖形識別」直接訓練相關工程師

---

## 3. 學生工程素質 & Lab 文化

### 3.1 Lab 規模
- **查無直接來源**的精確人數；根據 NCKU 機器人實驗室網站結構推測為中型規模（10-20 名研究生 + 若干大專生）
- Lien 同時掌管 AI Robotics 學位學程（碩士），招收 AI + 機器人跨域學生

### 3.2 課程與訓練深度
- 開設研究所課程「Computer Vision and Deep Learning」（2023 Fall 可查）
- 另開「Machine Learning and Pattern Recognition」（大學部）
- 學生接受完整的 CNN → YOLO → 嵌入式部署 pipeline 訓練

### 3.3 已知競賽與開源活動
- GitHub 可查：`JiaChangGit/CVDL-NCKU`（連震杰的電腦視覺深度學習課程作業存儲庫）
- `Xenorock/Imgprocessing-Deeplearning`（NCKU 影像處理與深度學習）
- **查無** AICUP、Kaggle 或工業檢測賽的直接得獎記錄（不代表無參與）
- YouTube 頻道「連震杰 成大機器人實驗室，NCKU Robotics Lab」有研究展示影片

### 3.4 畢業生去向（推測）
- 學術脈絡 + 產業合作：工研院機械所、精密機械產業有一定比例
- Intel / Qisda 合作管道：ICT 製造端 CV 工程師
- 南科地緣效應：Fab 相鄰，部分學生畢業直接進入台積電南科廠、聯電、日月光 AOI/設備部門（查無直接 LinkedIn 樣本確認）

---

## 4. 合作優缺點分析

### 4.1 優點

**T3 直接命中：**
連震杰的研究 100% 對準「視覺 + 3D + 缺陷偵測」，是台灣學術界少數同時具備：
- 3D 結構光量測
- CNN/YOLO 缺陷分類
- 嵌入式 CUDA 產線部署能力

的 PI，與 2nm+ 先進封裝良率檢測需求高度吻合。

**南科地緣優勢（南台灣 Fab 集群）：**
NCKU 位於台南，距台積電南科廠（Fab 14, Fab 18）車程 20 分鐘，物流樣本運輸成本極低，適合快速迭代缺陷樣品測試。

**行政職加分：**
身為電資學院副院長，合作案在校內審查流程有潛在便利性；AI 機器人學位學程主任確保有持續的高素質碩博士生供應。

**歷史產學合作積累：**
30 個完成計畫（NCKU PURE），Intel/Qisda 合作案顯示有成功執行產業合約的能力，非純學術 PI。

### 4.2 潛在風險

| 風險 | 評估 |
|------|------|
| 近 5 年論文引用動能（607 引用，h5=12）偏保守 | 中等，相較頂 AI lab 偏保守，但 AOI 非熱門 AI 領域，標準不同 |
| 近期論文較偏醫療影像（肺結節、肝腫瘤）| 需確認 AOI 仍為活躍研究主軸或已轉向 |
| AOI 論文未見頂刊（CVPR/ICCV/ECCV）| 應用導向 PI，學術聲望在 CV 頂會較低；但對產業合作影響不大 |
| 學生直接競賽成績查無 | 難以快速評估工程實作水準 |

### 4.3 三個具體合題題目

**題目一：先進封裝 3D 缺陷全自動 AOI 系統**
- 針對 CoWoS / SoIC 結構的基板翹曲（Warpage）、凸塊缺失（Missing Bump）、焊錫橋接（Bridge）
- 採用結構光 3D 重建 + Attention-based CNN 缺陷分類器
- 目標：生產線 takt time 內完成單片掃描（< 10s）

**題目二：少樣本缺陷學習（Few-Shot Defect Detection）用於新節點 AOI 上線**
- 2nm 節點量產初期，缺陷樣本稀少（< 50 張）
- 採用 Meta-Learning / Data Augmentation + 半監督自學習框架
- 直接對應 Lien lab 在嵌入式平台輕量模型的既有研究方向

**題目三：視覺引導機器手臂 + AOI 一體化自動取樣平台**
- 整合 Lien 的 Visual Servo 手臂控制 + 3D AOI 量測
- 針對封裝廠微觀瑕疵多角度自動取像（替代人工翻轉定位）
- 直接複用 lab 現有 AGV + Robot Arm 研究基礎設施

### 4.4 與本公司需求匹配度評估

若本公司業務聚焦於以下任一方向，連震杰為 **Top-2 match PI**：

- 2nm+ **晶圓級或封裝級 AOI 設備開發**
- 先進封裝（CoWoS、HBM、SoIC）**良率提升解決方案**
- **視覺 + 機械整合**的自動化設備（取樣、搬送、量測）

若業務偏向前端晶圓製程缺陷（光罩對準、蝕刻均勻性），則 Tang Kea-Tiong（製程控制）或 Chen Argon（統計製程）可能更直接；但 AOI 視覺系統開發，Lien 是最強選項。

---

## 5. 資料來源清單

| 來源 | URL | 訪問日期 |
|------|-----|---------|
| NCKU CSIE 系所成員頁 | https://www.csie.ncku.edu.tw/zh-hant/members/25 | 2026-04-22 |
| NCKU AI 機器人學位學程師資 | https://aim.ncku.edu.tw/p/426-1179-13.php?Lang=en | 2026-04-22 |
| NCKU PURE 研究輸出系統 | https://researchoutput.ncku.edu.tw/en/persons/james-jenn-jier-lien/ | 2026-04-22 |
| Google Scholar | https://scholar.google.com/citations?user=C6Ic16IAAAAJ | 2026-04-22 |
| DBLP 論文清單 | https://dblp.org/pid/l/JennJierJamesLien.html | 2026-04-22 |
| Robotics Lab 官網 | http://robotics.csie.ncku.edu.tw/ | 2026-04-22 |
| NCKU Undergraduate Research Lab 頁 | https://en.ur.ncku.edu.tw/laboratory/Robotics+Lab/ | 2026-04-22 |
| CV 原始 PDF（2018 版） | http://robotics.csie.ncku.edu.tw/Cv_LienJames_NckuCsie_20180901_V2Beta8_En.pdf | 2026-04-22 |
| GitHub – CVDL 課程作業 | https://github.com/JiaChangGit/CVDL-NCKU | 2026-04-22 |
| GitHub – 影像處理深度學習 | https://github.com/Xenorock/Imgprocessing-Deeplearning | 2026-04-22 |
| NCKU 機器人 YouTube | https://www.youtube.com/channel/UC1aPU1qzxAXmfhOSpBEIuJA | 2026-04-22 |
| ResearchGate profile | https://www.researchgate.net/profile/James-Lien-2 | 2026-04-22 |

---

## 總結評分

| 維度 | 評分（1-5） | 說明 |
|------|------------|------|
| 技術契合度（T3 AOI） | ★★★★★ | 完全直接命中，3D AOI + 結構光 + CNN |
| 隱形綁定風險 | 🟢 低 | 無半導體龍頭排他綁定證據 |
| 地緣優勢 | ★★★★★ | 台南 NCKU，距南科 Fab 最近 |
| 學術影響力 | ★★★☆☆ | h-index 20，近 5 年動能中等，非頂會 |
| 產業合作能力 | ★★★★☆ | Intel/Qisda 合作案 + 30 完成計畫 |
| 行政資源 | ★★★★☆ | 副院長 + 學位學程主任，資源調動能力強 |

**Phase 2 建議：維持 🟢 Open。優先接觸。建議直接發信請求「AI for Advanced Packaging AOI」研討，並詢問近期 2nm 相關 NSTC 計畫。**
