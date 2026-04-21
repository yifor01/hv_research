# 研究計畫書 — 台灣大學 AI × 半導體先進製程教授盤點

- **發起日期**：2026-04-21
- **研究主題**：台灣 11 所頂尖大學在 AI × 半導體先進製程（≤2nm）領域可長期投資的教授
- **發起人背景**：某領先半導體製造公司 AI 部門主管
- **研究目的**：
  1. 尋找能合作提升 2nm 以下量產速度、良率、工程師工作效率的教授
  2. 尋找有潛力的研究生做未來招募

---

## 範圍

### 學校（11 所）
國立台灣大學、國立清華大學、陽明交通大學、國立成功大學、國立中央大學、國立台灣科技大學、國立中山大學、國立政治大學、國立中興大學、國立台灣師範大學、國立台北科技大學

### 系所焦點
- 電機、電子、資訊工程、光電、材料、化工、機械、物理
- 工業工程與管理（智慧製造相關）
- 數據科學 / 統計（AI 方法）
- 各校 AI 研究中心 / 半導體研究中心 / 奈米製程實驗室

### 技術領域（原 100+ 條目群聚為 6 大主題 + 1 個跨群標籤層）

| # | 主題群 | 涵蓋的原始專長 |
|---|---|---|
| T1 | 製程控制 / 設備智能 | APC, AI-driven APC, R2R, FDC, Virtual Metrology, PINN, Predictive Process Modeling, PdM, Equipment Health Monitoring, Plasma Etch Endpoint Detection, Sensor Fusion, RUL, Process Control |
| T2 | AI-EDA / DTCO / DFM | AI-assisted EDA, Generative Layout Synthesis, DRC, TCAD, ML for EDA, AI for EDA, EDA for AI, IR Drop Analysis, Timing Optimization, DFM, Manufacturability-Driven Design, DTCO, Cell Library Synthesis, TCAD Device Simulation |
| T3 | 良率 / 缺陷 / 量測 | Wafer Defect Inspection, ADC, Yield Prediction, RCA (incl. Autonomous), Causal AI, Anomaly Detection, Semiconductor Yield Management, Digital Twin for Yield, AI-powered AOI, AOI, CD-SEM Image Analysis, SEM Automated Analysis, TEM Analysis, Scatterometry, OCD, In-line Metrology, Hybrid Metrology, 3D Profile Inversion, Yield Optimization |
| T4 | 先進封裝 / 異質整合 | Chiplet Integration, 3D-IC, Hybrid Bonding, CoWoS, SoIC, EMIB, D2W Bonding, Warpage Prediction, Thermal Management Optimization, TSV, Advanced Packaging Process Control, SiP, Heterogeneous Integration |
| T5 | 元件 / 新材料 | GAA FET, Gate-All-Around, 2D Materials, FinFET, SiGe/GeSn Device, FeRAM/FeFET, 3D NAND, ALD, NNPs, MLFF, PFP, Molecular Dynamics Simulation, Virtual 2D Materials, Recipe Optimization |
| T6 | 智慧製造 / IIoT / 供應鏈 | Fab Digital Twin, Smart Manufacturing, RL for Scheduling, Dispatching Optimization, Supply Chain Optimization, AMHS, OEE, IIoT, SECS/GEM, Digital Twins |
| T7a | AI 方法論標籤（疊加於 T1–T6） | CNN, GNN, Transformer, LSTM, Diffusion, RL, Transfer/Few-shot/Federated/Continual/Autotelic Learning, Synthetic Data, Data Augmentation, Sim-to-Real, XAI, SHAP, Causal Inference, MLOps, Edge AI, TinyML, CV, ViT, RelGAT, GANs, Deep/Machine Learning |
| **T7b** | **LLM / Agentic AI / Generative AI 獨立候選軌** | **LLM fine-tuning / RLHF / LoRA / instruction tuning, Agentic AI (multi-agent, tool use, planning), Generative AI, Physical AI, Foundation Models — 即使與半導體 domain 無直接交集也納入候選** |

**使用方式**：
- **T7a** 只作為方法論標籤，疊加於主群 T1–T6 上（例：主攻 T3 良率預測、方法上用 GNN + Causal Inference）
- **T7b** 為**獨立候選軌**：即使教授目前研究與半導體無明顯交集，只要在 LLM fine-tuning 或 Agentic AI 有紮實成果，仍納入候選 — 因為這類能力對「工程師工作效率」目標（copilot、recipe knowledge LLM、agentic RCA 助手）有高遷移性，疊加半導體 domain 會大幅縮小候選池

---

## 方法論（兩階段橫縱分析）

### Phase 1 — 廣度篩選（候選清單，60–100 位）

**目標**：產出可快速篩選的候選池，讓客戶圈選 Phase 2 對象。

**資料源**：
- 各校系所師資網頁
- Google Scholar（發表年限：2020–2026）
- 國科會（NSTC）計畫查詢系統
- 產學合作公告、技轉公告
- 國際研討會參與紀錄（ISSCC, VLSI Symp, IEDM, DAC, ICCAD, DATE, ASP-DAC, ISCA, MICRO, IEEE IRPS, IEEE Trans. on Semi. Manuf.）
- 新聞媒體（聯合報、商業周刊、數位時代、iThome、科技新報、DIGITIMES）

**篩選規則**：教授需至少命中以下條件之一
1. 2020+ 發表過命中任一主題群（T1–T6）的論文 ≥1 篇
2. 2020+ 主持過相關國科會計畫或產學合作案
3. 曾受台積電/聯電/力積電/美光/ASML/英特爾/應材等廠商委託研究或贊助
4. 指導過在上述公司就職或實習的研究生
5. **T7b 獨立軌**：在 LLM fine-tuning / Agentic AI / Generative AI 有 2020+ 頂會論文、開源 release、或國科會旗艦計畫，即使無半導體交集亦納入（會加註「純 AI 軌」）

**⚠️ 綁定過濾（Corporate Entanglement Flag）**：
每位候選教授要額外評估與**其他半導體/AI 巨頭**的綁定程度，並以欄位 `binding_status` 明確標示：
- 🟢 **Open**：無顯著綁定，可自由合作
- 🟡 **Partial**：有部分合作（1–2 家公司贊助 / 學生實習 / 計畫），仍有合作空間
- 🔴 **Deep Bound**：已與特定公司深度綁定（長期冠名實驗室、唯一贊助商、大量博士生系統性進同一家公司、Chief Scientist / Advisor 正式頭銜），**投資價值低，建議降級或排除**

**判斷訊號**：
- 冠名實驗室或冠名講座（e.g., NVIDIA AI Lab @ XX University、MediaTek Chair Professor）
- 連續 3+ 年主要贊助來自同一家公司
- 公開的 Chief Scientist / Technical Advisor 頭銜
- 近 3 年 5+ 位博士生 / 博後進入同一家公司
- 公司新聞稿中明確點名「合作教授」且高頻出現
- 教授個人網頁 / LinkedIn 明確標示企業顧問身份

**已知範例**（研究開始前的先驗）：王鈺強（NTU）→ NVIDIA（深度綁定，🔴）。研究過程若發現類似案例會一併標示並加註出處。

**Phase 1 處理策略**：🔴 仍列入候選總表但明確加註綁定對象 + 評論「投資價值偏低」；🟡 列入並註明合作對象；🟢 優先推薦進 Phase 2。

**Phase 1 輸出**：
- `phase1-candidates.md`
  - **A. 可貼上的頓號教授名單**（依校分段）
  - **B. 候選總表**（欄位如下）

| 校 | 系所 | 姓名 | 職級 | 主命中群 (T1-T6 / T7b) | AI 標籤 (T7a) | 2020+ 代表計畫/論文 | 產學合作徵兆 | **綁定狀態 🟢🟡🔴** | **綁定對象/備註** | 簡短摘要（1–2 行）| 建議是否進 Phase 2 |

### Phase 2 — 深度 Profile（15–25 位，客戶圈選）

**每位教授產出三維度剖析**：

**維度 1：技術契合度**
- AI 架構訓練/微調能力的實證
- 半導體 AI 相關計畫參與紀錄（國科會、業界委託）
- 具體落地成果（技轉、專利、產品內使用）
- 學界/業界肯定（傑出研究獎、IEEE Fellow、Best Paper 等）
- **每項事證附年份與引用來源**

**維度 2：學生工程素養與實驗室文化**
- Lab GitHub / 開源專案狀態（活躍度、README 品質、CI/CD、Star 數）
- 2020+ 研究生競賽成績（IC/CAD Contest、ICCAD CAD Competition、Kaggle、AICUP、AI-BIT、IEDM Student Papers）
- 畢業生 LinkedIn 去向（台積電、聯發科、NVIDIA、Google、AMD、Intel、Synopsys、Cadence 等比例）
- 協同發表中的學生作者生呈度（學生一作/共一比例，反映 lab 是否把光環讓給學生）

**維度 3：合作優缺點與建議方式**
- 與該教授合作的優點（技術、人脈、學生、場域）
- 潛在缺點/風險（太 junior、過度產學綁約、方向偏離、溝通負荷）
- **🔴 綁定狀態詳述**：若已被其他公司深度綁定，具體指出綁定方、綁定形式、綁定年限、可否部分解綁，並給出「可合作程度百分比」估計
- **建議合作模式**：產學計畫、博士生聯合培育、設備試跑場域、演算法 POC、長期顧問、併購/投資、技轉

**比較總表**（跨 Phase 2 教授）：五等第評分
- 技術契合度（★★★★★）
- 學生品質（★★★★★）
- 落地能力（★★★★★）
- 合作意願訊號（★★★★★）
- **獨立性 / 可合作性**（★★★★★ — 🔴 綁定者自動扣分）
- 優先級建議（Tier 1 / 2 / 3 — 🔴 除非技術絕無可替代，否則最高只給 Tier 3）

### 最終 PDF 報告

用 `hv-analysis` skill 產出 `tw-univ-semi-ai-professors_橫縱分析報告.pdf`，含：
- 封面、執行摘要、研究方法
- 縱軸敘事（台灣學界半導體 AI 近五年脈絡）
- 橫軸比較（11 校重點實驗室橫向對比）
- 逐位教授 profile
- 總表、引用來源、建議行動清單

---

## 資料夾結構

```
reports/2026-04-tw-univ-semi-ai-professors/
├── RESEARCH_PLAN.md                            # 本檔（研究計畫）
├── phase1-candidates.md                        # Phase 1 候選清單 + 頓號名單
├── phase2-profiles/                            # 每位教授一檔
│   ├── <校簡碼>-<教授姓名>.md
│   └── ...
├── comparison-table.md                         # Phase 2 交叉比較總表
├── sources.md                                  # 引用 URL + 訪問日期 + 備援存檔
└── tw-univ-semi-ai-professors_橫縱分析報告.pdf # 最終 PDF

raw-materials/2026-04-tw-univ-semi-ai-professors/
└── （研究過程中抓下來的原始 PDF、截圖、爬取資料）
```

---

## 交付順序與時程預估

| 階段 | 內容 | 預估工時 |
|---|---|---|
| Phase 1-A | 平行派 Explore agents 分片搜尋 11 校 × 6 主題 | 2–3 小時 |
| Phase 1-B | 彙整成頓號名單 + Markdown 總表 | 30 分鐘 |
| **⏸️ 客戶圈選 Phase 2 對象** | | — |
| Phase 2-A | 15–25 位教授深度 profile | 3–5 小時 |
| Phase 2-B | 比較總表、交叉分析 | 1 小時 |
| Phase 2-C | hv-analysis 產出 PDF | 1 小時 |
| **總計** | | **約 8–11 小時**（可拆多 session） |

---

## 風險與免責

- **時效性**：教授的研究方向會演化，本報告以 2020–2026-04 為主要資料窗口
- **公開資料限制**：無法評估個性契合度、實際溝通風格、實驗室內部矛盾；建議 Phase 2 圈選後，客戶親自拜訪前幾位
- **LinkedIn 資料**：部分教授實驗室的畢業生未更新 LinkedIn，樣本偏差可能高估或低估 lab 輸出
- **競賽成績**：並非所有強 lab 都投入競賽，缺席競賽不等於弱
- **引用規範**：所有 fact 附 URL + 訪問日期；無法驗證的訊號（如業界傳聞）會明確標示「未能驗證」

---

## 客戶確認項

- [ ] 方法論同意
- [ ] 主題群聚 T1–T7 同意
- [ ] 交付格式（Markdown 總表 + PDF）同意
- [ ] 啟動 Phase 1 — 綠燈

---

*設計完成日期：2026-04-21*
