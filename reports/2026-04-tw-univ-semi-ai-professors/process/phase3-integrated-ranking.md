# Phase 3 整合：Top 15 候選 PI 最終排名（含 Batch A/B 補強）

- **報告日期**：2026-04-22
- **整合來源**：Phase 2 Top 7 投資分析 + Phase 2 ⚠️ 5 位重評 + Phase 3 Batch A（LLM/RAG）+ Phase 3 Batch B（CoWoS/封裝）
- **目的**：補足 Phase 2 兩個題目的單兵作戰缺口，產出完整 Top 15 總表供主管決策

---

## §0 重大變動摘要

### 本次新增 6 位 PI
| 新增 | 教授 | 校系 | 分數 | 補強題目 | 來源 |
|---|---|---|---|---|---|
| 🆕 | **陳冠能** Kuan-Neng Chen | NYCU ICST Dean | **8.7** | 系統整合 Hybrid Bonding / 3D IC | Batch B |
| 🆕 | **陳智** Chih Chen | NYCU 材料系主任 | **8.3** | 奈米雙晶銅 nt-Cu（Science 2012 發現人）| Batch B |
| 🆕 | **江國寧** Kuo-Ning Chiang | NTHU PME 講座 | **8.1** | AI × 封裝 FEA 疲勞壽命預測（題目原主力）| Batch B |
| 🆕 | **黃瀚萱** Hen-Hsen Huang | AS 資訊所副研究員 | **7.2** | WWW 2025 CAG（Cache-Augmented Generation）| Batch A |
| 🆕 | **彭文志** Wen-Chih Peng | NYCU 資工正教授 | **7.0** | SIGIR 2025 Agentic Decomposed IR | Batch A |
| 🆕 | **高宏宇** Hung-Yu Kao | NTHU 資工（2024/8 轉入）| **6.4** | EMNLP 2023 Retrieval Domain Adaptation | Batch A |

### 對主管「只推薦一位」疑慮的完整防禦
- **CoWoS/封裝題目**：從 **1 位（宋振銘）** → **4 位**（宋振銘 + 陳冠能 + 陳智 + 江國寧），形成「材料 → 系統 → AI 方法論」三段互補鏈
- **人員工作效率題目**：從 **1 位（蔡銘峰）** → **4 位**（蔡銘峰 + 黃瀚萱 + 彭文志 + 高宏宇），覆蓋「傳統 RAG / CAG 新範式 / Agentic Decomposed IR / Retrieval Domain Adaptation」完整研發圖譜

---

## §1 更新後 Top 15 完整排序（TSMC 視角）

| 排名 | 教授 | 校/系 | 領域 | 分數 | 題目群 | 狀態 |
|---|---|---|---|---|---|---|
| 🥇 1* | **王俊明** Chun-Ming Wang | NSYSU SAT ISMID 所長 | AI 光刻 / OPC / RET | **9.0** | 前段製程（2nm）| ⚠️ 法務 check 後定案 |
| 🥇 2 | **馬誠佑** Cheng-Yu Ma | NSYSU 電機 + SAT | FeFET / TFT / Neuromorphic | **8.9** | Device / 2nm NVM | Wave 1 |
| 🥈 3 | **胡璧合** Vita Pi-Ho Hu | NTU 電機 | FeFET × M3D × CIM × CFET SRAM | **8.7** | Device / N2/A16 BEOL | Wave 1 |
| 🥈 3 | **陳冠能** Kuan-Neng Chen | NYCU ICST Dean + 電子所講座 | Hybrid Bonding / 3D IC / Layer Transfer | **8.7** 🆕 | 封裝（系統整合）| **Wave 1 新增** |
| 🏅 5 | **銀慶剛** Ching-Kang Ing | NTHU 統計講座 | Time Series Knockoffs / SPC | **8.5** | fab VM / SPC 方法論 | Wave 1 |
| 6 | **陳智** Chih Chen | NYCU 材料系主任 + 特聘 | nt-Cu 奈米雙晶銅 / Science 2012 | **8.3** 🆕 | 封裝（材料層）| **Wave 2 新增** |
| 6 | **詹寶珠** Pau-Choo Chung | NCKU 電機特聘 + 電資院長 | Domain Adaptation / 醫學影像 → AOI | **8.3** | 後段 AOI 跨製程 adaptation | Wave 2 |
| 8 | **江國寧** Kuo-Ning Chiang | NTHU PME 講座 + 先進封裝中心主任 | AI × FEA / 封裝可靠度 | **8.1** 🆕 | 封裝（AI 方法論，題目主力）| **Wave 1 新增** |
| 9 | **宋振銘** Jenn-Ming Song | NCHU 材料研發長 | Cu-Cu Bonding × 表面改質 × AI | **8.0** | 封裝（線上量測）| Wave 2 |
| 9 | **李家岩** Chia-Yen Lee | NTU 資管副院長 | DRL / MARL / 製造 OR | **8.0** | fab 排程 / 異常偵測 | Wave 2 |
| 9 | **鄭桂忠** Kea-Tiong Tang | NTHU 電機 | Neuromorphic IC / CIM | **8.0** | CIM 22→7nm 延伸 | Wave 2 |
| 12 | **蔡佩璇** Pei-Hsuan Tsai | NCKU IMIS | Digital Twin / SOP 視覺驗證 | **7.7** | fab Digital Twin / SOP | Wave 2 |
| 13 | **林嘉文** Chia-Wen Lin | NTHU 電機 + 半導體學院 | Vision Transformer → 光刻 EDA | **7.5** | 光刻 EDA 原型 | Wave 3 |
| 14 | **蔡銘峰** Ming-Feng Tsai | NCCU 資科 | LTR / RAG / Conversational Search | **7.2** | 人員效率（製程 RAG）| Wave 2 |
| 14 | **黃瀚萱** Hen-Hsen Huang | AS 資訊所副研究員 | CAG / RAG / LLM | **7.2** 🆕 | 人員效率（CAG 新範式）| **Wave 2 新增** |
| 16 | **彭文志** Wen-Chih Peng | NYCU 資工正教授 + 前系主任 | Agentic Decomposed IR / Data Mining | **7.0** 🆕 | 人員效率（Agentic 報告生成）| **Wave 3 新增** |

\* 王俊明排名暫列 #1 但需法務確認：(a) TSMC 離職年數 (b) 商秘獎/專利綁定。若無綁定則實升 Tie #1；若有綁定則降至 Wave 2 由馬誠佑獨佔 #1。

### Wave 1-3 分配（**更新後**）

**Wave 1（5 位，最優先 3-6 個月啟動）**：
- 馬誠佑 / 胡璧合 / 銀慶剛（Phase 2 原 Top 3）
- **王俊明**（法務 clear 後加入）
- ⭐ **陳冠能 NEW**（系統封裝話語權級選手，國際頂會 IEDM/VLSI 每年命中 + ICST Dean 制度對接快）
- ⭐ **江國寧 NEW**（AI × 封裝 FEA 直接命中原題目，零 TSMC 綁定 = first mover）

**Wave 2（6 位，Wave 1 啟動後 6-12 月補上）**：
- 詹寶珠 / 李家岩 / 鄭桂忠 / 宋振銘 / 蔡佩璇
- **陳智 NEW**（Science 2012 nt-Cu 發明人，AMAT/SRC/TSMC 多方合作過 = 成熟 PI）
- **蔡銘峰 + 黃瀚萱 NEW**（人員效率 RAG 雙軌：傳統 vs CAG 新範式，平行啟動對照實驗）

**Wave 3（3 位，補位/長線觀察）**：
- 林嘉文（光刻 EDA 原型，需 12 月 PoC）
- **彭文志 NEW**（Agentic IR 範式成熟但與蔡銘峰/黃瀚萱有方法論重疊，排後）
- **高宏宇 NEW**（2024/8 剛轉 NTHU，Lab 重組中，待觀察）

**排除**：李祈均（NVIDIA Deputy 深度綁定）、16 位未入選 AI 名人（U1-U16）。

---

## §2 題目群完整盤點（主管最常問 3 問）

### Q1：為什麼 CoWoS/封裝題目只推薦 1 位？（已解決）

**答**：Phase 3 補強後，CoWoS/封裝 AI 題目共 **4 位 PI 互補**：

| PI | 定位 | 貢獻 |
|---|---|---|
| 陳冠能（8.7）| 系統整合層 | Hybrid Bonding / 3D IC / Layer Transfer 國際頂會話語權 |
| 陳智（8.3）| 材料層 | nt-Cu 奈米雙晶銅 Science 2012 首發 + Chemleader 量產 |
| 江國寧（8.1）| AI 方法論層 | 唯一台灣本土「ML × 封裝 FEA 疲勞壽命」連續發表 PI |
| 宋振銘（8.0）| 線上量測落地 | Cu-Cu 接合強度預測 + 電化學感測 + 未來科技獎 TRL 4-5 |

建議 TSMC **4 人一組推動**：江國寧主持 AI 方法論、陳冠能主持系統整合、陳智主持材料、宋振銘主持量測落地。

### Q2：為什麼人員工作效率題目只推薦 1 位？（已解決）

**答**：Phase 3 補強後，RAG / 工程師助手題目共 **4 位 PI 互補**：

| PI | 方法論路線 | 差異化價值 |
|---|---|---|
| 蔡銘峰（7.2）| 傳統 Dense Retrieval + LTR | SIGIR 2025 DMCL + TREC iKAT 2025 LLM Query Reformulation，方法論深度最強 |
| 黃瀚萱（7.2）| Cache-Augmented Generation（WWW 2025）| 2025 RAG 新範式提出者 + TAIDE 顧問同陣營 + 特別適合「封閉 SOP 語料」場景 |
| 彭文志（7.0）| Agentic Decomposed IR（SIGIR 2025）| 財報生成範式 → 可直接改裝「製程月報/良率週報自動生成」 |
| 高宏宇（6.4）| Retrieval Domain Adaptation（EMNLP 2023）| 「一般 RAG → 製程 RAG」跨 domain 搬遷方法論 |

建議 TSMC 在 Wave 2 啟動「蔡銘峰 + 黃瀚萱」**雙軌 PoC 對照**（傳統 RAG vs CAG），6 個月後再決定 Wave 3 是否納入彭文志 / 高宏宇。

### Q3：如果這 15 位都不願合作，替代選項有哪些？（Phase 4 待辦）

- 目前 Phase 1-3 只掃描了 37 位主候選（21 主選 + 16 未入選 AI 名人）+ 新增 Batch A/B 6 位 = 43 位
- 台灣全職 AI / 半導體 PI 估算 150-200 位，還有 100+ 位未深度盤點
- **Phase 4 建議**：若 Wave 1 任一位婉拒，立即啟動該題目群的「替代候選快速 scan」（例如王俊明被拒 → 掃林勇志 / 廖建能 / 劉致為等 13 年前 TSMC 背景但學界資深者）
- 現階段不建議盲目擴大，避免主管過載

---

## §3 對 Phase 2 原文件的變動點

本次整合後，Phase 2 原文件以下地方需補註（或在 PDF 版本直接取代）：

1. **`phase2-top7-investment-analysis.md` §1 投資總表**：原為 Top 7 + #8-21 + 16 未入選 = 37 位；**新版應為 Top 15 + #16-21 + 16 未入選 = 43 位**
2. **`phase2-top7-investment-analysis.md` §1.2**：宋振銘從 #8 排序被陳冠能/陳智/江國寧插入後，變成 #9；蔡銘峰從 #13 變成 #14（與黃瀚萱並列）
3. **Wave 1 名單**：原 3-4 位（馬誠佑 / 胡璧合 / 銀慶剛 / 王俊明）→ 擴展為 5-6 位（加入陳冠能 / 江國寧）
4. **Wave 2**：新增陳智 / 黃瀚萱

---

## §4 下一步建議動作

1. **[P0] 產新版 PDF**：整合 Phase 2 主文件 + Phase 3 Batch A/B profile + 本整合文件 → `TSMC_Top15_長期投資分析_v2.pdf`
2. **[P1] 主管圈選 Wave 1（5-6 位）**：等 PDF v2 交付後
3. **[P2] 法務 check**：王俊明 TSMC 離職年數 / 商秘獎 / 專利
4. **[P2] 陳冠能 / 江國寧 / 陳智 **先簽 MOU 接觸試水**（零大廠綁定，風險最低）
5. **[P3] 方法論 template**：把 5 維度 TSMC 視角框架抽成 `templates/pi-due-diligence-framework.md`

---

*整合完成時間：2026-04-22。本文件為 Phase 2 Top 7 投資分析的補充更新，兩份應合併交付主管。*
