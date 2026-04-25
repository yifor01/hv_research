# 深度 Profile：張孟凡（Meng-Fan Chang）

**撰寫日期：** 2026-04-22
**研究員層級：** Tier-S #4（Phase 1 評定）
**現職：** 國立清華大學電機系 特聘教授 / TSMC Corporate Research Director（兼任）

---

## 1. 基本資料

| 欄位 | 內容 |
|------|------|
| 英文姓名 | Meng-Fan (Marvin) Chang |
| 機構 | 國立清華大學（NTHU）電機工程學系 |
| 職稱 | 特聘教授（Distinguished Professor）、IEEE Fellow（2026 年 Class，IEEE SSCS 認定方向：low-power SRAM design & compute-in-memory） |
| 實驗室 | Memory Circuit Design Laboratory（記憶體電路設計實驗室，簡稱 Memory Design Lab） |
| 辦公室 | Delta Building, Room 861 |
| 兼職 | TSMC Corporate Research Director（Director of Corporate Research）；清華大學半導體研究學院 教授 |
| 電子郵件 | mfchang@ee.nthu.edu.tw |

### 學術統計（截至 2025）

- 論文引用次數：20,000+（h-index 41）
- 總發表量：321 篇（含期刊 + 會議）
- 美國專利：40+ 件
- 期刊：40+ 篇 IEEE journal
- 頂級會議：ISSCC 18+ 篇、VLSI Symposia 15+ 篇、IEDM 8+ 篇、DAC 5+ 篇

---

## 2. 技術契合度

### 2.1 核心研究主軸

張孟凡教授的研究圍繞三大支柱：

1. **存內計算（Compute-in-Memory, CIM）AI 晶片**：在 RRAM（ReRAM）、STT-MRAM、SRAM 儲存媒介上實現 in-situ 乘累加（MAC）運算，大幅降低 AI 邊緣推論的能耗。
2. **記憶體電路設計**：非揮發性記憶體（Flash、MRAM、PCRAM）電路架構優化；多位元/混精度 CIM macro 設計。
3. **神經形態計算**：Memristor 神經網路硬體實作；噪聲容忍貝葉斯神經網路（Bayesian NN）。

### 2.2 代表論文（2022–2026）

| 年份 | 標題（縮要） | 期刊/會議 | 關鍵技術 |
|------|------------|-----------|---------|
| 2025 | "A mixed-precision memristor and SRAM compute-in-memory AI processor"（Nature v.639, pp.617–623） | **Nature** | Memristor-CIM + SRAM-CIM 混精度；40.91 TFLOPS/W（ResNet-20/CIFAR-100）；373.52 μs wakeup latency |
| 2024 | "Fusion of memristor and digital compute-in-memory processing for energy-efficient edge computing"（Science v.384, pp.325–332） | **Science** | RRAM-CIM fusion；77.64 TOPS/W；<0.5% accuracy loss；392 μs wakeup |
| 2024 | "A 22nm 16Mb Floating-Point ReRAM Compute-in-Memory Macro with 31.2 TFLOPS/W for AI Edge Devices"（ISSCC 2024, Paper 34.8） | **ISSCC 2024** | FP16/BFloat16 ReRAM CIM；22nm TSMC process |
| 2025 | "A 22nm 104.5 TOPS/W μ-NMC-Δ-IMC Heterogeneous STT-MRAM CIM Macro for Noise-Tolerant Bayesian Neural Networks" | **ISSCC 2025** | STT-MRAM CIM；抗噪貝葉斯 NN；22nm |
| 2024 | "Hardware implementation of memristor-based artificial neural networks" | **Nature Communications** | Memristor 神經網路硬體實作（473 引用） |
| 2025 | "A 16nm 216kb, 188.4 TOPS/W and 133.5 TFLOPS/W Microscaling Multi-Mode Gain-Cell CIM Macro for Edge-AI Devices" | **ISSCC 2025** | TSMC 16nm Gain-Cell；INT/FP dual-mode；163.3 TOPS/W INT-MAC |
| 2022 | "Memristive technologies for data storage, computation, encryption, and RF communication" | **Science** | Memristor 多功能綜述（695 引用） |

> 說明：Science 2024 為全球驗證 RRAM CIM 量產可行性的里程碑，Nature 2025 將混精度架構推進到同一晶片上分層最佳化——為當前 CIM 領域最高規格學術成果之一。

### 2.3 TSMC 製程合作紀錄（明確文件）

- **TSMC-NTHU Joint Development Project (JDP)**：NTHU-TSMC 聯合研發中心每年執行 10+ 個 JDP，計算方向為核心之一；每個 JDP 有 TSMC 內部 coordinator 接口，贊助期最長 3 年。
- **Science 2024**：晶片在 TSMC 流片（tape-out），論文致謝 TSMC Corporate Research（TSMC-CR）。
- **Nature 2025**：論文致謝 TSMC-CR、TSMC Design Technology Platform（TSMC-DTP）、TSMC More-than-Moore Technologies（TSMC-MtM）、以及 TSMC-NTHU JDP 計畫——四個 TSMC 部門同時掛名，合作深度罕見。
- **ISSCC 2024（ReRAM macro）**：在 TSMC 22nm 製程上 tape-out 的 16Mb ReRAM CIM macro。
- **ISSCC 2025（STT-MRAM/Gain-Cell）**：TSMC 22nm、16nm 製程各一篇。

### 2.4 主要命中領域

| 技術向量 | 評分（1-5） | 說明 |
|---------|-----------|------|
| T5 Device（Advanced Memory Device + NVM） | ⭐⭐⭐⭐⭐ | RRAM、STT-MRAM、MRAM CIM macro；全球頂尖 |
| T2 AI-EDA / AI Chip Architecture | ⭐⭐⭐⭐⭐ | CIM AI 加速器架構；非傳統 Von Neumann 架構先驅 |
| T3 Process Integration（DTCO for CIM） | ⭐⭐⭐⭐ | TSMC 22nm/16nm 流片；Device-Circuit co-design |
| T6 Edge AI Inference | ⭐⭐⭐⭐ | 已在 Science/Nature 驗證 edge 推論效能 |

---

## 3. 學生工程素質 & Lab 文化

### 3.1 實驗室規模（依公開資料推估）

- **已知博士生**（依人員頁面及論文作者）：Feng-Ji Tsai、Tommy Chen（SRAM, TSMC 資助）、Chi-Chang Shuai、Hsin-Chi Lai、Chih-Sheng Lin、Heng-Kai Liu、Tai-Hao Wen（Science 2024、Nature 2025 第一作者）、陳韋豪（ISSCC 2025）等——名單顯示博士生約 10-15 人同時在組。
- **碩士生**：15 人以上，涵蓋 SRAM、MRAM、RRAM、Flash、DRAM、3D/2.5D 架構多個次領域。
- **Postdoc / 訪問研究員**：資料未公開，但 TSMC 有指派的 industry coordinator。

### 3.2 學生 Tape-out 與競賽紀錄

- **實際 tape-out 頻率高**：ISSCC 每年有 1-3 篇流片晶片，製程橫跨 TSMC 22nm、16nm、65nm；博士生自第一年起即參與 tape-out 準備。
- **ISSCC 學生貢獻**：Science 2024 與 Nature 2025 兩篇頂刊的第一作者 Tai-Hao Wen 為博士生，顯示學生被允許主導旗艦成果。
- **NTHU 整體 ISSCC 排名**：2018 年 4 篇入選，台灣第一、全球並列第 6（同 UC Berkeley）；2025 年再度 4 篇入選，清華電機學界排名台灣第一。

### 3.3 畢業生去向（依人員頁面 alumni 欄位）

依舊版人員頁面標記，畢業博士生/碩士生流向包括：
- **TSMC**（IC 設計、製程研發）—— 最多去向
- **聯發科（MediaTek）**
- **旺宏（Macronix, MXIC）**
- **聯電（UMC）**
- **工研院電光所（ITRI）**

> 海外（如 NVIDIA、三星、應用材料）去向未見於現有公開文件，但作為全球頂尖 CIM 實驗室，畢業生有相當比例具備直接進入 Fabless/IDM IC 設計職位的硬體工程能力。

---

## 4. 合作優缺點分析

### 4.1 優點

1. **全球 CIM AI 晶片首席 PI**：Science 2024 + Nature 2025 雙頂刊驗證 RRAM CIM 量產可行性，是此方向全球少數已在先進製程完成完整 tape-out→論文閉環的實驗室。
2. **TSMC 多部門深度綁定**：TSMC-CR、TSMC-DTP、TSMC-MtM、TSMC-NTHU JDP 四條線並行，製程資源直連，不需解釋「為什麼要找 TSMC」。
3. **IEEE Fellow 2026 + TSMC Director 雙重身份**：在業界和學界同時具備影響力，合作成果容易找到實際應用出口。
4. **學生有豐富 tape-out 實戰**：每位博士生的研究幾乎都有實際晶片，工程素質高於純模擬組。
5. **多精度、多材料 CIM 技術棧完整**：從 SRAM、RRAM、STT-MRAM 到 Gain-Cell，已具備從元件到系統的完整 know-how。

### 4.2 缺點與風險

1. **Tape-out 週期長、成本高**：一個 CIM macro 晶片從設計到成果通常需 2-3 年，IP 管理與排他條款需要提前釐清（尤其涉及 TSMC-NTHU JDP 成果歸屬）。
2. **IP 歸屬複雜**：TSMC 同時資助多個 NTHU JDP，若合作題目與現有 JDP 計畫重疊，IP 所有權需特別協商。
3. **時間稀缺性**：Nature/ISSCC 級 PI 同時兼任 TSMC Director，行事曆競爭激烈；學生日常指導可能需要透過資深博士生 relay。
4. **硬體合作週期與商業節奏不匹配**：如果合作方期望 6-12 個月看到成果，硬體 tape-out 路徑通常難以配合，需設計「軟/硬並行」的交付架構。

### 4.3 建議合作型態

**推薦：聯合研究計畫（Joint Research Program）+ 學生交流**

理由：張教授已有成熟的 TSMC JDP 框架，最自然的切入是以類似 JDP 模式在旗下實驗室設置「共同研究員（Joint Researcher）」名額，或以學術合作方式共同申請 NSTC 計畫，同時安排 1-2 名博士生做短期訪問（3-6 個月）以建立互信。純 IP 授權或技術移轉方式**不建議**作為首要切入，因為 TSMC 已是主要下游；建議以「研究成果→共同論文→後期技術轉移」為路徑。

---

## 5. 三大具體可切入合作題目

### 題目一：Advanced Process DTCO for CIM Macro（先進製程 CIM Design-Technology Co-Optimization）

**背景**：現有 ISSCC 成果已驗證 22nm/16nm CIM macro；2nm N2 製程帶來新的 Cell 結構，需要 device-circuit co-design 重新 calibrate。
**合作形式**：提供 2nm PDK 存取 + CIM simulation model；張教授團隊負責 macro 設計 + tape-out。
**產出目標**：1-2 年內完成 2nm CIM macro tape-out，共同發表 IEDM 或 VLSI 論文。

### 題目二：Edge Inference CIM Chip for Multimodal Small Models（邊緣 LM 推論 CIM SoC）

**背景**：LLaMA-3B 等 Small Language Model 開始部署在手機/穿戴裝置，現有 SRAM-only 推論效率不足；RRAM-CIM 可提供 10× 能效提升。
**合作形式**：合作方定義應用場景（模型大小、精度需求）；張教授設計 CIM macro；合作方協助 AI framework mapping（量化、校準）。
**產出目標**：3 年內完成 end-to-end edge LM 推論系統展示，申請 NSTC 旗艦計畫。

### 題目三：Noise-Robust CIM Macro Verification Platform（抗噪 CIM 測試與可靠性平台）

**背景**：ISSCC 2025 STT-MRAM CIM macro 已有 noise-robust Bayesian NN 成果，但現場可靠性（溫度飄移、老化）的系統性驗證是業界痛點。
**合作形式**：合作方提供可靠性測試設備或工廠數據；張教授團隊提供 macro + 模型。
**產出目標**：建立 CIM macro reliability verification methodology，對接 JEDEC 等標準流程。

---

## 6. 風險評估

| 風險類型 | 等級 | 說明 |
|---------|------|------|
| 綁定風險 | 🟢 低 | 已有多方合作（TSMC 多部門 + NSTC），習慣並行合作；非獨家 |
| IP 風險 | 🟡 中 | TSMC-NTHU JDP 成果歸屬需明訂；建議在 MOU 中設「共同 IP 清單」 |
| 執行風險 | 🟡 中 | Tape-out 週期 2-3 年；PI 時間稀缺；建議指定資深博士生為技術窗口 |
| 技術風險 | 🟢 低 | 核心 RRAM/MRAM CIM 技術已有多篇頂刊驗證，成熟度高 |
| 商業化風險 | 🟡 中 | TSMC 為主要合作方，新合作方需避免與 TSMC 現有 JDP 產生直接競爭 |

---

## 7. 資料來源清單

| 編號 | URL | 說明 | 訪問日期 |
|-----|-----|------|---------|
| 1 | https://www.ee.nthu.edu.tw/~mfchang/ | 個人首頁（NTHU EE） | 2026-04-22 |
| 2 | https://khub.nthu.edu.tw/researcherProfile?uuid=EB9DFDA7-8599-46B8-99E4-A34B79A58498 | NTHU Knowledge Hub 研究員頁 | 2026-04-22 |
| 3 | https://scholar.google.com/citations?user=7rcOEiIAAAAJ&hl=zh-TW | Google Scholar 個人頁 | 2026-04-22 |
| 4 | https://www.nature.com/articles/s41586-025-08639-2 | Nature 2025：mixed-precision memristor+SRAM CIM processor | 2026-04-22 |
| 5 | https://www.science.org/doi/10.1126/science.adf5538 | Science 2024：Fusion of memristor and digital CIM | 2026-04-22 |
| 6 | https://pubmed.ncbi.nlm.nih.gov/38669568/ | PubMed 版本（Science 2024） | 2026-04-22 |
| 7 | https://dee.site.nthu.edu.tw/p/406-1175-267813,r2471.php?Lang=en | NTHU EE Science 論文公告（含 TSMC 合作說明） | 2026-04-22 |
| 8 | https://dee.site.nthu.edu.tw/p/406-1175-279260,r2471.php?Lang=zh-tw | NTHU EE ISSCC 2025 入選公告 | 2026-04-22 |
| 9 | https://www.semiconchina.org/en/824 | SEMICON China 演講者介紹（含出版紀錄） | 2026-04-22 |
| 10 | https://www.ee.nthu.edu.tw/~mfchang/i_people2017.htm | Lab 人員頁（含博士生名單及 alumni 去向） | 2026-04-22 |
| 11 | https://research.tsmc.com/english/collaborations/academic/jdp-paper-up-1.html | TSMC JDP 學術合作計畫頁 | 2026-04-22 |
| 12 | https://www.linkedin.com/in/meng-fan-marvin-chang-a98baa42/ | LinkedIn（TSMC Director + NTHU 雙掛） | 2026-04-22 |
| 13 | https://www.researchgate.net/publication/378953740_348_A_22nm_16Mb_Floating-Point_ReRAM_Compute-in-Memory_Macro_with_312TFLOPSW_for_AI_Edge_Devices | ISSCC 2024 Paper 34.8 ResearchGate 頁面 | 2026-04-22 |
| 14 | https://pubmed.ncbi.nlm.nih.gov/40044859/ | PubMed 版本（Nature 2025） | 2026-04-22 |

---

## 8. 綜合評分（對應 Phase 1 架構）

| 評分維度 | 分數（/10） | 備註 |
|---------|-----------|------|
| 技術深度 | 10 | 全球 CIM AI 晶片頂級 PI；Science + Nature 雙頂刊 |
| TSMC 製程連結 | 10 | TSMC Director + JDP 四部門；直接 tape-out |
| 學生工程素質 | 9 | 每年 1-3 顆晶片流片；博士生為論文第一作者 |
| 合作可行性 | 8 | Open 態度；JDP 框架成熟；但週期長需預期 |
| 商業化潛力 | 9 | Edge AI CIM 市場明確；已有 Fabless 量產路徑 |
| **加權總分** | **9.2 / 10** | Tier-S 確認無誤 |

---

*本報告由 Phase 2 深度 profile 研究員產出，資料截止 2026-04-22。所有技術數字以原始論文為準。*
