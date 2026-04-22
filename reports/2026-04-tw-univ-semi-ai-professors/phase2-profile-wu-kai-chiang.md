# 深度 Profile：吳凱強（Kai-Chiang Wu）— NYCU 資工 教授

**研究產出日期：** 2026-04-22  
**Tier 定位：** Tier-1 #7（NYCU 資工 EDA+AI 頂級）  
**主命中：** T2（EDA + Design-for-Testability）+ T7a（Edge AI / Efficient DL）

---

## 1. 基本資料

| 項目 | 內容 |
|------|------|
| 現職 | NYCU 資工系 教授（CS Director 職銜） |
| 學歷 | CMU ECE 博士（2006–2011，指導教授：Diana Marculescu）|
| 碩士 | 清華大學 CS（GPA 4.0，師從張世傑） |
| 工業經歷 | Intel Corp. Design Technology Solutions，Senior SWE（2011–2013）|
| Lab 名稱 | **邊緣實驗室**（原 CAD 實驗室；正式名：GREAT Systems Lab） |
| Lab 網站 | http://eda.cs.nycu.edu.tw/ |
| Email | kcw@cs.nycu.edu.tw |
| Scholar h-index | 16（all-time）；13（since 2021）；總引用 968 |

---

## 2. 隱形綁定檢查 ⚠️

### Intel（離職 10+ 年）
- 2011–2013 任職 Intel Design Technology Solutions，負責 CPU reliability verification
- **目前無任何跡象**顯示仍掛 Intel consultant 身分
- 離職後返台直接加入 NCTU/NYCU，Intel 標籤屬歷史資產而非現役綁定
- **結論：Intel 綁定風險低（🟢）**

### EDA 三大廠（Synopsys/Cadence/Siemens）
- Lab 歷屆畢業生流向：Synopsys 6 人、Cadence 5 人、Siemens EDA 1 人
- 以「人才供應商」角色與三大廠存在**非正式的關係網絡**
- 未見正式 joint lab 或 sponsored research 的公開紀錄
- 2025 ICCAD CAD Contest Problem A（Hardware Trojan Detection）由吳凱強共同命題，顯示在 ICCAD 社群具影響力
- **結論：EDA 廠綁定屬人才流向關係，非合約性質（🟡 低度注意）**

### MediaTek
- 畢業生流向 MediaTek 6 人（最多單一目的地）
- 2024 MediaTek MARC（MediaTek Advanced Research Center）計畫有 NYCU 參與機制
- 未確認吳凱強本人是否直接受 MediaTek 資助的具名計畫
- **結論：存在中度 MediaTek 人才輸送管道（🟡）**

### TSMC / NVIDIA
- 搜索未找到直接合作或個人顧問關係的公開資料
- NYCU-TSMC 整體學程合作（Elite Scholarship 等）屬學校層級，非個人綁定
- **結論：無明顯隱形綁定（🟢）**

---

## 3. 技術契合度

### 研究標籤演化（2020 → 2026）
吳凱強的研究在 2020–2022 年完成一次明顯轉型：
- **舊核心**（到 2022 年）：EDA、DfT、Design for Reliability、clock skew scheduling、IDDQ 測試
- **新核心**（2022 年起）：Edge AI、Efficient Deep Learning、LLM 壓縮、硬體 Trojan 偵測

這使他成為**「EDA × AI 雙棲」**研究者，而非純 EDA。

### 代表論文（2023–2026，5 篇精選）

| 年份 | 論文 | 會議 | 主題 | 引用 |
|------|------|------|------|------|
| 2025 | **Palu: KV-Cache Compression with Low-Rank Projection** | ICLR 2025 | LLM 推理記憶體壓縮（50% KV-Cache，1.89× 加速）| 29+ |
| 2025 | **Quamba: Post-Training Quantization for Selective State Space Models** | ICLR 2025 | SSM 量化框架 | 23+ |
| 2025 | **Systolic Sparse Tensor Slices: FPGA Building Blocks for Sparse/Dense AI** | FPGA 2025 | FPGA 上的 AI 加速器設計 | 13+ |
| 2024 | **Identifying Good-Dice-in-Bad-Neighborhoods Using ANN** | VTS 2024 | 晶圓測試 + ML 良率預測 | 25+ |
| 2023 | **CNN-Based Stochastic Regression for IDDQ Outlier Identification** | IEEE TCAD 2023 | 傳統 EDA/DfT 核心 | 15+ |

**備注：** 2025–2026 新增 AAAI 2026（SkipCat LLM 壓縮）、ICML 2025（Quamba2）、EMNLP 2025（FLRC），顯示研究發表場景已從 EDA 轉向 ML 頂級會議。

### Lab 規模（2024 估計）
- 1 名博士後研究員
- 2 名在職博士生（一在 Skymizer、一在旺宏/Macronix）
- 約 9–13 名碩士生（含新生）
- 規模：**中型 lab**，師生比合理，有足夠人力接大型合作計畫

### NYCU 內部 EDA/AI chip 整合中心參與
- 擔任 ICCAD 2025 CAD Contest Problem A 命題人，具社群影響力
- 與 Diana Marculescu（UT Austin，前 CMU）維持跨校持續合作（多篇 2024–2025 共著）
- 未見正式掛名 NYCU 半導體中心或特定 AI Chip 整合計畫的公開資料

---

## 4. 學生工程素質

### ICCAD/DAC Contest 表現
- 2025 ICCAD CAD Contest Problem A 由吳凱強 **共同命題**（Hardware Trojan Detection on Gate-Level Netlist），代表其在 EDA 競賽圈的地位已從「參賽者」晉升至「出題者」
- 直接搜索未找到其 lab 學生近年 ICCAD/DAC Contest 得獎的公開紀錄（相較同校黃俊達、劉建男的明確得獎紀錄）

### 畢業生流向（Lab 官方揭露資料）
| 目的地 | 人數 | 備注 |
|--------|------|------|
| MediaTek 聯發科 | 6 | 最多 |
| Synopsys | 6 | EDA 龍頭 |
| Cadence | 5 | EDA 龍頭 |
| NEUCHIPS | 3 | AI 加速器新創 |
| Novatek 聯詠 | 2 | |
| Realtek 瑞昱 | 2 | |
| Siemens EDA | 1 | |
| Google | 1 | |
| Phison 群聯 | 1 | |
| Macronix 旺宏 | 1（在職博士生）| |

**關鍵觀察：** 無 Intel 、AMD、NVIDIA 的直接流向紀錄。學生主要進入台系供應鏈（MediaTek、Synopsys/Cadence 台灣辦公室）。

### 與 NTU 張耀文 lab 的關係
- 兩者同為台灣頂級 EDA 研究者，但**領域定位有差異**：
  - 張耀文（NTU EE）：Physical Design、Place & Route、DfM — 側重**佈局繞線前端**
  - 吳凱強（NYCU CS）：DfT/DfR、Hardware Security、Edge AI — 側重**後端測試與 AI 應用**
- 未找到正式合作論文或對抗競爭關係的文件
- **結論：互補多於競爭，可同時合作**

---

## 5. 合作優缺點分析 & 建議

### 優勢

**A. CMU 博士 × Diana Marculescu 門下 = 世界級 AI-Hardware 訓練**
- Marculescu 是能耗感知計算（energy-aware computing）領域的奠基人之一
- 吳凱強繼承其研究基因：硬體效率 × AI 模型設計
- 適合本公司若有 **Intel/AMD 風格的 CPU reliability 或硬體驗證研發需求**

**B. 雙棲優勢：EDA 根基 + LLM 前沿**
- 同時在 ICLR/ICCAD 發表，跨域稀缺
- 可對接「ML for EDA」和「EDA for AI」兩個方向，是少數能做**雙向連結**的台灣教授

**C. 畢業生網絡覆蓋 EDA 生態**
- Synopsys + Cadence = 11 人，意味著若本公司有 EDA 工具開發需求，這個 lab 的畢業生是優質人才庫

### 弱點

**A. 近年發表重心飄移出 EDA 核心**
- 2023 年後多數頂級論文（ICLR × 2、ICML、AAAI）屬 LLM/SSM 量化壓縮，非傳統 EDA
- 若本公司需要的是 P&R、timing closure、DRC 等傳統 EDA，此 lab 的前沿性不足

**B. ICCAD/DAC 出題人角色而非近年競賽得主**
- 說明影響力已轉向 mentor/evaluator，而非 cutting-edge EDA 解題者

**C. Intel 離職已逾 10 年，CMU 訓練雖扎實但非近年美系大廠現役人脈**

### 3 個具體合作題目

**題目 1：ML for EDA — 硬體 Trojan 自動偵測**
- 根基：2025 ICCAD Contest 命題人，深入理解 gate-level netlist 的 Trojan 模式
- 具體形式：joint research 或委託研究，開發用於 IC 設計安全驗證的 ML 模型
- 適用場景：有 IC 設計安全需求的公司（軍用、車用、AI chip）

**題目 2：GPU/FPGA-accelerated Verification（硬體加速驗證）**
- 根基：FPGA 2025 稀疏張量加速 + EDA 背景
- 具體形式：共同開發 FPGA 上的 formal/simulation verification 加速器
- 適用場景：需縮短 tape-out 時間的設計公司

**題目 3：DfT × AI — 量產測試成本最佳化**
- 根基：VTS 2024 Good-Dice 識別 + IDDQ outlier 偵測（IEEE TCAD 2023）
- 具體形式：用 AI 模型替換傳統測試 pattern，降低 ATPG 生成成本
- 適用場景：有自研晶片且在乎量產測試成本的 fabless 或 IDM 公司
- **注意：MediaTek 已在此方向有人才輸送關係，需確認是否存在利益衝突**

---

## 6. 綜合評分

| 維度 | 評分（1–5）| 備注 |
|------|-----------|------|
| 技術深度 | ⭐⭐⭐⭐ | EDA+AI 雙棲，LLM 壓縮達 ICLR 水準 |
| 合作潛力 | ⭐⭐⭐⭐ | 中型 lab，反應靈活，無重大隱形綁定 |
| 學生工程素質 | ⭐⭐⭐ | 台系供應鏈導向，無美系 NVIDIA/AMD 流向 |
| 隱形綁定風險 | 🟢 低 | Intel 歷史綁定；EDA 廠屬人才管道非合約 |
| 近年 EDA 核心 | ⭐⭐⭐ | 2023+ 重心移向 ML，EDA 傳統深度稍降 |

**整體推薦：🟢 積極接觸**——特別適合有 AI × 硬體安全、Edge AI 加速、或 DfT+ML 需求的合作場景。

---

## 7. 資料來源

| 來源 | 內容 | 訪問日期 |
|------|------|----------|
| [NYCU CS 系教師頁](https://www.cs.nycu.edu.tw/members/detail/kcw?locale=en) | 職稱、Lab 名、聯絡資訊 | 2026-04-22 |
| [個人主頁（NCTU）](https://people.cs.nycu.edu.tw/~kcw/) | 學歷、Intel 經歷、研究方向 | 2026-04-22 |
| [Google Scholar](https://scholar.google.com/citations?user=TrWPWaIAAAAJ&hl=en) | 引用數、h-index、2023–2026 論文 | 2026-04-22 |
| [DBLP](https://dblp.org/pid/28/6933.html) | 完整出版品列表 2020–2026 | 2026-04-22 |
| [NYCU Academic Hub](https://scholar.nycu.edu.tw/en/persons/kai-chiang-wu/) | 研究方向、教育背景 | 2026-04-22 |
| [Dcard 研究所版（邊緣實驗室招生貼）](https://www.dcard.tw/f/graduate_school/p/255156522) | Lab 規模、畢業生流向 | 2026-04-22 |
| [Dcard 研究所版（嚴正澄清貼）](https://www.dcard.tw/f/graduate_school/p/260214616) | 學生評價背景 | 2026-04-22 |
| [arXiv Palu 2407.21118](https://arxiv.org/abs/2407.21118) | ICLR 2025 代表作詳情 | 2026-04-22 |
| [ICCAD 2025 Contest Problem A（IEEE Xplore）](https://ieeexplore.ieee.org/document/11240658/) | HW Trojan 命題人確認 | 2026-04-22 |
| [ICCAD CAD Contest 2024 Results](https://www.iccad-contest.org/2024/tw/05_results.html) | NYCU 得獎隊確認（非吳凱強 lab）| 2026-04-22 |
