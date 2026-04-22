# Phase 2 深度 Profile：張耀文 Yao-Wen Chang（NTU EDA Lab）

**研究日期**：2026-04-22
**Tier 分類**：Tier-1 #6（NTU EDA Lab）
**Phase 1 初評**：🟡 Partial（業界多方整合）

---

## 1. 隱形綁定檢查 ⚠️（核心風險評估）

### 🔴 MediaTek 獨立董事（高度綁定，最重要發現）

**張耀文自 2024 年 5 月起擔任 MediaTek Inc. 獨立董事**，並加入 MediaTek 永續及 M&A 策略委員會。這是一個有法律義務、領取董酬的正式公司治理職位，**不只是顧問關係**。

風險評估：
- MediaTek 是台灣最大的 IC 設計公司，也是主要晶片採購方
- 若與任何競爭 MediaTek 業務的公司（Qualcomm、Intel 等）開展合作研究，可能觸及利益迴避條款
- MediaTek 作為 TSMC 最大客戶之一，間接影響 TSMC 方向的合作敏感度
- **建議**：合作前需確認 NTU 利益衝突揭露規定，任何涉及手機/AI 晶片設計自動化的題目需特別審慎

### 🟠 Synopsys 雙重技術移轉（中高度綁定）

張耀文與 Synopsys 有兩層深度技術連結：

1. **SpringSoft 收購鏈**：其 NTUplace3 技術轉移至 SpringSoft 的 Digital Custom Placer；2012 年 Synopsys 以 USD 4.06 億收購 SpringSoft，技術隨之歸屬 Synopsys。

2. **Maxeda 收購（2023 年）**：張耀文 2015 年共同創辦 Maxeda Technology，其 NTUplace4 為 Maxeda 旗艦產品 MaxPlace 核心引擎；2023 年 Synopsys 收購 Maxeda。

**技術上兩次核心演算法均歸入 Synopsys 產品線**，但由於 Maxeda 已完成收購（非在職），直接利益衝突已解除。然而研究方向若涉及 Placement 演算法的延伸改進，在智財歸屬上仍需釐清。

### 🟢 NVIDIA / TSMC / Cadence / Siemens EDA

未發現與上述公司有正式顧問、董事或技術授權關係。無隱形綁定跡象。

### 🟡 RealTek / Faraday（舊有，已結束）

舊有顧問關係（2004-2009 年），目前無活躍連結，風險低。

### IEEE CEDA 領導層

曾任 CEDA President（2020/2021），現任 IEEE CEDA Fellow Search Committee 主席，屬委員會行政職，不構成商業綁定。

---

## 2. 技術契合度分析

### 研究領域（2024-2025 年現況）

根據個人頁面與 DBLP 資料，當前五大研究主軸：

1. **AI for EDA**：Reinforcement Learning for Placement（ASP-DAC 2025）、ML IR Drop Prediction、AI-driven physical design
2. **3D IC / Heterogeneous Integration**：2.5D/3D 異質整合、Advanced Packaging、Chiplet 設計（DAC 2024、ICCAD 2024）
3. **VLSI Physical Design**：Routing、Floorplanning、Legalization、Timing Optimization
4. **Advanced Packaging**：Redistribution Layer（RDL）routing、PCB co-design、Warpage Modeling
5. **Quantum Computing（新興）**：Subgraph-based Qubit Mapping（ASP-DAC 2026）

### 2023-2026 代表論文（5 篇）

| 年份 | 題目 | 場次 |
|------|------|------|
| 2026 | Redistribution Layer Routing With Dynamic via Insertion Under Irregular via Structures | IEEE TCAD |
| 2025 | Mixed-Size Placement Prototyping Based on Reinforcement Learning with Semi-Concurrent Optimization | ASP-DAC 2025 |
| 2025 | Robust Technology-Transferable Static IR Drop Prediction Based on Image-to-Image Machine Learning | ASP-DAC 2025 |
| 2025 | From Classical Algorithms to AI: Evolving Trends in VLSI Physical Design Automation | IEEE Design & Test |
| 2024 | Mixed-Size 3D Analytical Placement with Heterogeneous Technology Nodes | DAC 2024 |

### CAD Contest 成績（核心競爭力指標）

張耀文實驗室被公認為全球 EDA Contest **最強稱霸團隊**：
- **全球 #1**：8 次一等獎，23 次三甲，橫跨 DAC / ICCAD / ISPD
- 2024 ICCAD CAD Contest：1st Place（Power and Timing Optimization Using Multibit Flip-Flop）
- 2023 ICCAD CAD Contest：1st Place（Problem B: 3D Placement with Macros）
- NTUplace4：連獲 DAC、ICCAD、ISPD 三大賽事冠軍

---

## 3. 學生工程素質評估

### 實驗室規模

NTU EDA Lab（BL-406）為台灣最大 EDA 實驗室之一，通常維持 20-30 名 PhD/MS 學生。確切人數需查閱最新實驗室頁面，但張耀文的博士生指導人數在台灣 EDA 領域首屈一指。

### 畢業生去向（工業界 Network）

根據個人頁及公開資訊，主要畢業去向：
- **EDA 廠**：Synopsys（含前 Maxeda）、Cadence、Siemens EDA
- **晶片設計**：MediaTek、RealTek（前顧問公司）
- **代工廠**：TSMC（Physical Design 部門）
- **創業**：Maxeda Technology（已被 Synopsys 收購，至少 1 位共同創辦人為前學生）

**特別強項**：在 EDA contest 勝出的學生，進入業界後往往快速晉升為 senior engineer，因為他們的演算法工程能力已在國際競賽中驗證。

### 工程素質特徵

- Contest 訓練體系嚴格，學生具備完整的演算法設計到實作能力
- 技術棧橫跨 C++、Python、ML（PyTorch/TensorFlow for EDA）
- 熟悉產業標準工具（LEF/DEF、OpenROAD 格式）
- 高壓競賽文化培養強健的 debugging 和優化能力

---

## 4. 合作優缺點 & 建議

### 優點

1. **全球頂尖 EDA 演算法能力**：NTUplace4 等技術已在產業界大規模應用，不是純學術
2. **Contest 人才輸送管道**：合作可吸引最優質的 EDA 工程人才
3. **廣泛業界人脈**：MediaTek 董事職位代表他理解產業需求，不只做象牙塔研究
4. **異質整合前瞻性**：3D IC / Chiplet 是台灣半導體未來 5 年核心戰場，他已提前布局
5. **論文質量穩定**：370+ 篇 ACM/IEEE，h-index 高，合作容易產出頂會論文

### 缺點 / 風險

1. **🔴 MediaTek 董事利益衝突**：涉及 IC Design 自動化、手機 SoC 相關題目時，需確認沒有資訊不對稱問題
2. **🟠 Synopsys 技術歷史**：若研究成果有商業化潛力，需事先談清楚智財歸屬
3. **競爭激烈，排隊等候**：他是台灣 EDA 最炙手可熱的教授，可能已有多個產學合作排隊
4. **院長後第一年**：2024 年卸任院長後回歸研究，可能仍在重新調整節奏

### 建議合作題目（3 個）

**題目 A：AI-EDA for Advanced Packaging（最推薦）**
- 子題：ML-based warpage prediction for CoWoS/SoIC
- 契合：他的 2024 ICCAD advanced packaging 方向
- MediaTek 風險：低（advanced packaging 非 IC design 核心）
- 產業出口：TSMC、ASE、日月光等先進封裝廠

**題目 B：DTCO-aware 3D Placement for Heterogeneous Nodes**
- 子題：Chiplet floorplanning with process-aware parasitics
- 契合：DAC 2024 的 3D Analytical Placement 直接延伸
- 產業出口：TSMC N2/N3 3D-IC ecosystem
- 注意：需確認非 MediaTek SoC 方向，避免利益衝突

**題目 C：Reinforcement Learning for Multi-Objective Physical Design**
- 子題：RL-based legalization with timing/power co-optimization
- 契合：ASP-DAC 2025 RL placement 的自然延伸
- 產業出口：所有 EDA 廠、自動化設計流程

---

## 5. 綜合評估

| 維度 | 評分 | 備註 |
|------|------|------|
| 技術頂尖性 | ★★★★★ | 全球 EDA 前 3，台灣 #1 |
| 學生工程素質 | ★★★★★ | Contest 冠軍工廠 |
| 產業連結深度 | ★★★★☆ | MediaTek 董事、前 Maxeda 創辦人 |
| 合作可行性 | ★★★☆☆ | 利益衝突需提前釐清 |
| 隱形綁定風險 | 🔴 中高 | MediaTek 董事為已知、公開綁定 |

**最終建議**：可合作，但**必須提前揭露 MediaTek 董事潛在利益衝突**，並選擇遠離 IC Design / SoC 核心的題目（advanced packaging、量子 EDA、FPGA EDA 方向最安全）。他的學生品質和技術深度在台灣無出其右，合作風險主要來自法律/治理層面而非技術層面。

### 備選教授（若決定迴避）

若以上利益衝突無法解決，同領域 EDA 替代選項：
- **NYCU 吳凱強（Kai-Chiang Wu）**：Constraint-driven routing，綁定較少
- **NSYSU 李書旻（Shu-Min Li）**：DFM 方向，南部廠商網路
- **NTHU 王廷基**：Timing closure，與 Synopsys 關係較直接但透明

---

## 6. 資料來源清單

| 來源 | URL | 訪問日期 |
|------|-----|----------|
| Yao-Wen Chang 個人頁 | https://cc.ee.ntu.edu.tw/~ywchang/yaowen.html | 2026-04-22 |
| Yao-Wen Chang CV（2024-10-18）| http://cc.ee.ntu.edu.tw/~ywchang/ywchang_CV_20241018.pdf | 2026-04-22 |
| IEEE CEDA 個人頁 | https://ieee-ceda.org/contact/yao-wen-chang | 2026-04-22 |
| DBLP 論文目錄 | https://dblp.org/pid/c/YaoWenChang.html | 2026-04-22 |
| Google Scholar | https://scholar.google.com/citations?user=qKJ_7jAAAAAJ&hl=en | 2026-04-22 |
| MediaTek 董事會 | https://corp.mediatek.com/investor-relations/corporate-governance/board-of-directors | 2026-04-22 |
| SEMICON Taiwan 講者頁 | https://www.semicontaiwan.org/en/node/10956 | 2026-04-22 |
| NTU EE 教授頁 | https://www.ee.ntu.edu.tw/bio1.php?teacher_id=69 | 2026-04-22 |
| NTU EDA Lab | https://eda.ee.ntu.edu.tw/ | 2026-04-22 |
| Maxeda Digitimes 報導 | https://www.digitimes.com/news/a20230913PR203/maxeda-technology-press-release.html | 2026-04-22 |
