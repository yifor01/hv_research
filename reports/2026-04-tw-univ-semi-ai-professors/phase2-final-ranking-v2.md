# Phase 2 最終排名 v2 — 三維度量化評估

- **評估日期**：2026-04-22
- **評估方法**：5 組 Haiku agent 平行讀取 21 份 phase2-profile + phase2-tier1-verification.md，依三維度量化評分
- **公式**：綜合分數 = 維度1（技術契合度）× 0.5 + 維度2（學生工程素養 & Lab 文化）× 0.3 − 綁定折扣
- **綁定折扣**：🟢 = 0；🟡 = −1；🔴 = −2
- **資料來源**：以 2020+ 為優先（2019 前可引用但加註年份）
- **與 v1 差異**：v1 用「Tier 主觀分類 + 編號」，v2 用「三維度量化分數 + 統一序號 1-21」

---

## §1 綜合排名（21 位，依新分數遞減）

| 新排名 | PI | 校系 | 綁定 | 技術 | 學生 | 折扣 | 綜合 | v1 Tier |
|---|---|---|---|---|---|---|---|---|
| 1 | 胡璧合 | NTU 電機 | 🟢 | 8 | 9 | 0 | **6.7** | Tier-S |
| 2 | 銀慶剛 | NTHU 統計 | 🟢 | 9 | 7 | 0 | **6.6** | Tier-S |
| 3= | 李家岩 | NTU 資管 | 🟢 | 8 | 8 | 0 | **6.4** | Tier-S |
| 3= | 林嘉文 🆕 | NTHU 電機+半導體 | 🟢 | 8 | 8 | 0 | **6.4** | Tier-1 漏網 |
| 3= | 詹寶珠 🆕 | NCKU 電機+電資院長 | 🟢 | 8 | 8 | 0 | **6.4** | Tier-1 漏網 |
| 6 | 馬誠佑 🆕 | NSYSU 電機/SAT | 🟡 | 9 | 9 | −1 | **6.2** | Tier-1 漏網 |
| 7 | 宋振銘 | NCHU 材料 | 🟢 | 8 | 7 | 0 | **6.1** | Tier-1 |
| 8 | 蔡佩璇 | NCKU IMIS | 🟢 | 7 | 8 | 0 | **5.9** | Tier-1 |
| 9 | 連震杰 | NCKU 資工 | 🟢 | 8 | 6 | 0 | **5.8** | Tier-1 |
| 10= | 鄭桂忠 | NTHU 電機 | 🟡 | 8 | 8 | −1 | **5.4** | Tier-S |
| 10= | 楊佳玲 | NTU 資工（借調）| 🟡 | 8 | 8 | −1 | **5.4** | Tier-1 條件式 |
| 12 | 簡禎富 | NTHU 工工（CEO 兼任）| 🟡 | 9 | 6 | −1 | **5.3** | Tier-S 降條件式 |
| 13= | 王俊明 | NSYSU SAT | 🟡 | 8 | 6 | −1 | **4.8** | 條件式 |
| 13= | 蔡銘峰 | NCCU 資科 | 🟢 | 6 | 6 | 0 | **4.8** | 條件式 |
| 15= | Jakey Blue 藍啓航 | NTU 工工 | 🟡 | 7 | 6 | −1 | **4.3** | Tier-S |
| 15= | 吳凱強 | NYCU 資工 | 🟡 | 7 | 6 | −1 | **4.3** | Tier-1 |
| 17 | 楊素芬 | NCCU 統計 | 🟢 | 5 | 5 | 0 | **4.0** | Tier-1 |
| 18 | 柏林 | NTNU 資工 | 🟢 | 4 | 6 | 0 | **3.8** | 條件式 |
| 19 | 王振興 | NCKU 電機 | 🟢 | 3 | 5 | 0 | **3.0** | 條件式 |
| 20 | 鄭少為 | NTHU 統計 | 🟢 | 4 | 3 | 0 | **2.9** | 條件式 |
| 21 | 李祈均 🆕 | NTHU 電機 | 🟡 | 3 | 7 | −1 | **2.6** | 條件式 漏網 |

---

## §2 重大重排訊號（v1 → v2）

### 🚀 上升

- **胡璧合 → #1**：學生工程素養 9/10（連續 3 屆 TSMC PhD Scholarship + IEDM 學生入選率高 + L'ORÉAL UNESCO 2023）+ 🟢 純自由身，超車原 Tier-S 簡禎富、銀慶剛
- **林嘉文 / 詹寶珠（原漏網）→ #3=**：兩位 IEEE Fellow 的方法論深度與 🟢 加成下勝過 Jakey Blue / 鄭桂忠（兩位均 🟡）
- **馬誠佑（原漏網）→ #6**：技術 9 + 學生 9 全場最高並列，僅因 🟡 SAT 折扣排第 6；FeFET/TFT cycling endurance 是台灣稀缺領域

### 🔻 下降

- **鄭桂忠 #3 → #10**：JDP 教授 🟡 折扣 −1；Lab 規模小（2-4 人）拉低學生分
- **Jakey Blue #5 → #15**：技術 7 + 學生 6 + 🟡，半導體核心產量近 5 年偏少
- **吳凱強 → #15**：近年研究漂出 EDA 核心，2023+ 主力為 LLM 量化（ICLR），半導體 domain 退坡 + Neuchips 顧問 🟡
- **楊素芬 → #17**：純統計方法論（無 DL），技術契合僅 5/10
- **王振興 → #19**：半導體契合僅 5%（AI4DT 主軸是生醫/照明/教育）
- **鄭少為 → #20**：近 5 年無頂期刊論文 + 副教授 17 年未升等
- **李祈均 → #21**：半導體契合 35% + 京元/NVIDIA 雙顧問利益衝突

### ⚖️ 持平
- **銀慶剛 #2、李家岩 #3=**：v1 Tier-S 評估與 v2 量化分數一致，是「最沒有爭議的」第一批

---

## §3 v2 推薦分批（依新分數）

### 🥇 第一批（立即接觸）— Top 6（綜合 ≥ 6.0；建議優先聯絡）
| 排名 | PI | 為何 Top 6 |
|---|---|---|
| 1 | 胡璧合 | 學生指標全面亮眼，FeFET×M3D×CIM 三方交集，對手 fab 適合 device-circuit 切入 |
| 2 | 銀慶剛 | 方法論直接落地 fab 資料，2014 TSMC 先例可破，IMS Fellow 國際視野 |
| 3 | 李家岩 | T1/T3/T6 全棧、Profet AI 顧問熟悉商業化 path、GitHub 開源活躍 |
| 3 | 林嘉文 | 光刻 EDA 原型已存在，IEEE Fellow + 2024 NSTC 傑出 + h=69 |
| 3 | 詹寶珠 | DL 跨域遷移直接對接 AOI，IEEE Fellow + 完全自由身 |
| 6 | 馬誠佑 | 技術 9 + 學生 9 全場並列最高；FeFET/TFT 純 device 與 #1 胡璧合北南互補 |

### 🥈 第二批（短期接觸）— 7-12 名（綜合 5.3-6.1）
| 排名 | PI | 注意點 |
|---|---|---|
| 7 | 宋振銘 | Cu-Cu 接合 AI + 2025 未來科技獎；研發長行政負擔 30-40% |
| 8 | 蔡佩璇 | 學生流向 TSMC/ASML 暢通；Fulbright 至 2025-Q3，最快 Q3 啟動 |
| 9 | 連震杰 | T3 AOI 南科地緣；2025 論文方向漂向醫療影像需注意 |
| 10 | 鄭桂忠 | JDP 教授；Lab 精品但人力小；建議避開 JDP 重疊題目 |
| 10 | 楊佳玲 | 政務次長借調至 ~2027；建議顧問模式由學生主導 |
| 12 | 簡禎富 | CEO 轉任後時間 30-40%；T1/T3/T6 全棧仍頂尖；建議 NSTC 槓桿 |

### 🥉 第三批（條件式 / 需確認）— 13-17 名（綜合 4.0-4.8）
13-13. 王俊明（TSMC 年數待確認）/ 蔡銘峰（無半導體先例需 onboarding）
15-15. Jakey Blue（半導體核心產量偏少）/ 吳凱強（已轉 LLM 壓縮，EDA 退坡）
17. 楊素芬（純統計方法論，非 DL）

### 🟥 不建議入主名單 — 18-21 名（綜合 ≤ 3.8）
| 排名 | PI | 不建議原因 |
|---|---|---|
| 18 | 柏林 | 實為 ASR 專家而非 LLM，半導體應用需 6-12 月橋接 |
| 19 | 王振興 | 半導體契合僅 5%，AI4DT 主軸非製程 |
| 20 | 鄭少為 | 近 5 年無頂期刊；副教授 17 年未升等，研究動能存疑 |
| 21 | 李祈均 | 半導體契合 35%；NVIDIA + 京元電子雙顧問需先排除 COI |

> 18-21 名建議：可改列為「方法論顧問池」或「待觀察人選」，不進入 Top 名單；若真要合作，建議題目與本業距離較遠的「邊緣應用」（廠區人因照明、語音助手、健康監測）

---

## §4 三維度評估明細（依新排名 1-21）

### #1 胡璧合 Vita Pi-Ho Hu — NTU 電機（綜合 6.7｜技 8｜學 9｜🟢）

**維度 1 技術契合度: 8/10**
- AI 架構：FeFET 記憶體電路設計、Monolithic 3D IC、CFET SRAM、2D 材料奈米電子；Nature Nanotechnology 2024
- 半導體 AI 計畫：IEDM 2024×2、IEDM 2025×2；2020 IEEE TED TSMC 製程合作；M3D-FACT BEOL FeFET + FEOL CMOS 堆疊 + CIM macro
- 落地實績：連續 3 屆 TSMC PhD Scholarship（2022/23/24）；Lam Research Paper Award 2023；2025 Nature Sci Reports 3-Tier CFET 6T-SRAM
- 獎項肯定：L'ORÉAL-UNESCO Award 2023；Micron Foundation Chair Professor 2024；IEDM TC 2022-2026；ISSCC TC 2026；VLSI TC 2026；h≈55
- 評分理由：FeFET×M3D×CIM 三方完整交集，業界最前沿；Nature Nanotech+IEDM 常駐產出

**維度 2 學生工程素養: 9/10**
- 系統包裝：DTCO 導向，每篇論文均含 layout/area 估算與系統效能連結
- 競賽/實習：IEDM 學生入選率高；連續 TSMC PhD Scholarship × 3 屆；Lam Research Paper Award；Nature Nanotech 博士第一作者
- 畢業生流向：TSMC 認可度高；晶片下線 tape-out 經驗豐富
- Lab 規模：5 博 + 17 碩；女性 PI 代表性
- 評分理由：學生指標全面亮眼，DTCO 工程文化紮實

**維度 3 合作建議**
- 優：1. FeFET 是 2nm+ Post-SRAM 核心器件，技術契合度極高 2. L'ORÉAL-UNESCO 對 DEI KPI 加分 3. Micron Chair（非 TSMC 冠名）自由度高
- 缺：1. 無自有 fab/PDK 直接存取，依賴 TSMC tape-out 2. Lab 規模中等承接大型合作有壓力 3. Material 廣度 vs 深度需事先聚焦
- 型態：B（實習）+ C（人才直挖）；以「M3D CIM Macro 功耗-精度協同」切入，聯合張孟凡形成 device-circuit 完整鏈
- 破冰：邀請參加女性科學家論壇，討論 L'ORÉAL-UNESCO 影響；建議聚焦 FeFET BEOL 可靠性模型標準化（SPICE-compatible）

---

### #2 銀慶剛 Ching-Kang Ing — NTHU 統計（綜合 6.6｜技 9｜學 7｜🟢）

**維度 1 技術契合度: 9/10**
- AI 架構：高維變數選擇、Time Series Knockoffs（JASA 2025、JCGS 2025 直接以「識別半導體製程缺陷機台」為應用）
- 半導體 AI 計畫：2014 TSMC 合作（不良率降 11-14%）；2022 IEEE TASE + 美國專利 US12354122B2（與成大鄭芳田 Golden Path Search）；2025 JCGS 持續半導體聚焦
- 落地實績：2014 TSMC 統計模型實作；2022 IEEE TASE 專利（NCKU 申請人）；2025 JCGS 直接半導體應用驗證
- 獎項肯定：IMS Fellow 2025（台灣唯一）；教育部學術獎 2024；NSTC 傑出研究獎 2008/2013；Statistica Sinica AE
- 評分理由：方法論完全直接可落地 fab 資料，無需翻譯；2025 新作持續對齐半導體缺陷識別

**維度 2 學生工程素養: 7/10**
- 系統包裝：2014-2022 業界合作驗證跨機構協作；論文無企業綁定（NSTC、Simons Foundation 為主）
- 競賽/實習：統計所學生多進學術或政府機構；無公開 AICUP/Kaggle 紀錄（領域慣例）
- 畢業生流向：證據不足；推估中研院、成大、清華等學術為主；TSMC 統計工程師職缺有 2014 管道
- Lab 規模：所長任期 2018-2021 結束；推估博士生 3-6 人；跨校合作模式已驗證（與成大鄭芳田）
- 評分理由：統計所小但專精度高；跨校跨界合作經驗豐富

**維度 3 合作建議**
- 優：1. 方法論直接可用於 VM 特徵選擇與 SPC 異常追因 2. 2014 TSMC 落地先例 + 2025 對齐方向，合作脈絡完整 3. 無正式綁定，IMS Fellow 國際視野
- 缺：1. 博士生數量需確認 2. 方法論學者傾向論文>工程 3. 成大鄭芳田與 TSMC 關係密切，需確認 IYM channel 排他條款
- 型態：A（產學）+ B（實習）；題目「高維 In-line SPC 變數選擇」、「Time Series Knockoffs Sensor 異常監控」
- 破冰：邀請參加技術論壇分享 JCGS 半導體應用，引用 2014 TSMC 成果（「不良率降 11-14%」）切入；強調「真實 fab 資料 × 頂期刊發表」雙贏框架

---

### #3 李家岩 Chia-Yen Lee — NTU 資管副院長（綜合 6.4｜技 8｜學 8｜🟢）

**維度 1 技術契合度: 8/10**
- AI 架構：DRL（2024 Annals OR）、MARL（2025 IJPE）、BMB-LIME XAI（2024 KBS, 42 引用）；多目標 MILP × RL；autoencoder 異常偵測（2024 IJPR）
- 半導體 AI 計畫：Wafer Fab 排程；MARL chiller（2025）；日月光 wafer bin map autoencoder；NSTC 工工管理學門召集人（NSTC112-2221-E-002-003）
- 落地實績：2022《製造數據科學》專書（市面唯一）；Profet AI（杰倫智能）顧問（2023-）；CIIE2024 Best Paper（TFT-LCD T/C balance RL scheduling）
- 獎項肯定：IEEE Senior Member 2021；IEEE TSM 副編輯 2024；IEEE TASE 副編輯 2020-2022
- 評分理由：T1+T3+T6 三維度全覆蓋且各有 2024-2025 高品質論文支撐

**維度 2 學生工程素養: 8/10**
- 系統包裝：GitHub po-lab 10+ repo；Manufacturing-Data-Science ⭐93（2025-02 更新）；Operations-Research-Applications ⭐46
- 競賽/實習：CIIE2024 Best Paper（學生共著）；IEEE CASE 2024 Real Options
- 畢業生流向：台積電、友達、化工業；李教授曾任職台積電；無 LinkedIn 量化
- Lab 規模：推估 12-18 人；副院長 + EiMBA Director 雙重行政
- 評分理由：開源與教學並重，SWE 證據清晰；多業態合作非綁定

**維度 3 合作建議**
- 優：1. 方法論完整（OR×統計×DRL 三軌）各有 2024-2025 新作 2. 書作者降低開場溝通成本 3. 多業態合作無單一廠商排他風險
- 缺：1. 副院長 + EiMBA Director 行政負擔 2. 排程偏向既有 NSTC 計畫 3. Foundation Model 尚未見論文，LLM-for-fab 不最適
- 型態：A（產學）+ D（顧問）；聯合 NSTC 計畫共主持人
- 破冰：透過中工會 channel 寄信，具體提及對 MARL chiller paper 的技術問題，附 1 頁研究提案合寫 NSTC 計畫；不走 EiMBA 高管班

---

### #3 林嘉文 Chia-Wen Lin — NTHU 電機+半導體學院（綜合 6.4｜技 8｜學 8｜🟢）

**維度 1 技術契合度: 8/10**
- AI 架構：Vision Transformer + Mamba 遙感超解析度（h=69、17.4k 引用）；CNN 視覺基礎；TTST Token 選擇機制
- 半導體 AI 計畫：2024 NSTC 傑出研究獎明確提及「光刻失散失預測與光罩自動修正 EDA 工具」開發
- 落地實績：太赫茲光譜 CT 重建；EDA 光刻工具原型完成（無商業版本上線）；無專利授權案例
- 獎項肯定：IEEE Fellow 2018；NSTC 傑出研究獎 2024；K.T. Li Breakthrough Award 2021
- 評分理由：T3b（光刻 EDA）直接命中且已有原型，但產業化停留概念驗證階段

**維度 2 學生工程素養: 8/10**
- 系統包裝：GitHub 搜索未見官方開源組織（推論因 EDA 工具涉及 IP）；證據不足
- 競賽/實習：CVPR/ICCV 多篇論文發表代表國際會議競爭力；無 ICCAD CAD Contest 得獎記錄
- 畢業生流向：推論 NVIDIA、Google、Meta、TSMC、MediaTek，無公開統計
- Lab 規模：推估 8-12 人；NTHU AI Research Center 副主任；半導體學院合聘特聘
- 評分理由：國際學術競爭力強，但工程競賽記錄與產業實習證據不足

**維度 3 合作建議**
- 優：1. T3b 光刻 EDA 工具已有原型 2. 國際頂尖深度學習（h=69）最新涵蓋 ViT、Mamba 3. NTHU AI Research Center 副主任 + 半導體學院合聘，跨校協調力強
- 缺：1. 多媒體→製造業 AI 跨域門檻（95%+ 論文聚焦圖像） 2. EDA 應用仍停留原型，未見量產 3. 若投入 T3b EDA 需從多媒體 Lab 抽調 1-2 人
- 型態：A（NSTC 聯合計畫）；題目「視覺深度學習在半導體光刻工藝最佳化中的應用」；TSMC/ASML + NTHU + 交大光子；2-3 年 5-8 百萬
- 破冰：強調「EDA 工具已有原型」、突出「產業化」機會、明確提及「TSMC/ASML」合作可能；郵件強調 2024 NSTC 傑出研究獎

---

### #3 詹寶珠 Pau-Choo Chung — NCKU 電機+電資院長（綜合 6.4｜技 8｜學 8｜🟢）

**維度 1 技術契合度: 8/10**
- AI 架構：U-Net/SegNet 病理影像分割；CycleGAN-based domain adaptation；特徵解糾纏；無標籤/弱標籤自監督學習
- 半導體 AI 計畫：零公開記錄；研究完全位於醫療/病理；機會窗口而非風險
- 落地實績：跨掃描器魯棒性（CT/MRI 差異）、跨製程模型泛化技術；無半導體應用案例但方法論直接可遷移
- 獎項肯定：IEEE Fellow；前教育部資科司司長；NCKU 電資院長 2021-至今；h=54、8280+ 引用、2024 持續活躍
- 評分理由：方法論（GAN 域適應、特徵解糾纏）直接對應 AOI 跨製程/設備魯棒性需求；核心風險為「零半導體先例」

**維度 2 學生工程素養: 8/10**
- 系統包裝：無公開 GitHub（醫療領域涉及隱私）；若轉向半導體可建立開源生態
- 競賽/實習：無 AICUP/Kaggle/ICCAD 記錄；定位醫療 AI 應用
- 畢業生流向：推測 Google/Microsoft Research、Meta、Apple、國內醫療 AI；無半導體廠流向
- Lab 規模：8-12 人中型；院長身份具大型協作管理經驗
- 評分理由：論文競爭力強（MICCAI、IEEE JBHI），但半導體業界實習與競賽記錄缺乏

**維度 3 合作建議**
- 優：1. 方法論完全吻合（GAN、特徵解糾纏 → AOI 跨製程） 2. IEEE Fellow 學術信譽 3. 零企業獨佔綁定，完全自由身
- 缺：1. 零半導體先例需 PoC 驗證 2. Domain gap 風險（醫學 RGB vs AOI 多光譜）需 6-12 月適應 3. 院長行政負擔重（推估 30-40% 科研時間）
- 型態：A（聯合研究中心）；詹 Lab 方法論 + TSMC 應用專家 + 數據；12-18 個月 PoC
- 破冰：先從「域適應工作坊」開始降低初期投入；TSMC 工程師分享 1-2 個缺陷檢測 case；不強調「醫學遷移」而是「方法論通用性」

---

### #6 馬誠佑 Cheng-Yu Ma — NSYSU 電機/SAT（綜合 6.2｜技 9｜學 9｜🟡）

**維度 1 技術契合度: 9/10**
- AI 架構：可靠性物理模型、TCAD/SPICE 模擬、統計可靠性分析；無深度學習論文（缺 AI 訓練方法論）
- 半導體 AI 計畫：聯電 UMC 經驗（2008-2013，28nm/20nm）；SAT 合聘（2023-）帶來隱形計畫可能性
- 落地實績：FeFET cycling endurance + TFT reliability 直接對應業界痛點；68 期刊論文 + 9 專利；2024-2025 連續 IEEE TED
- 獎項肯定：連續 5 次傑出教學獎（2017-2024）；無 IEEE Fellow/NSTC 傑出研究獎
- 評分理由：T5 Device 純度 92% — FeFET/TFT 是核心；可靠性研究稀缺領地

**維度 2 學生工程素養: 9/10**
- 系統包裝：fabrication + characterization 訓練有素；TCAD/HSPICE 工具確認
- 競賽/實習：無 AICUP/Kaggle/ICCAD（Lab 定位物理特性而非競賽）；南科 40 分鐘地緣
- 畢業生流向：TSMC、MediaTek、UMC、日月光；南科地緣便利
- Lab 規模：50-60 人中等偏小；ADDA Lab 組織完善；Master 70%、PhD 20-30%
- 評分理由：工程實踐深度無敵，連續教學獎證明人才培育穩定

**維度 3 合作建議**
- 優：1. FeFET cycling endurance 全球稀缺 2. 與胡璧合形成南北 T5 完整覆蓋 3. 南科地緣 40 分鐘 vs NTU 3+ 小時
- 缺：1. SAT 合聘 🟡 隱形綁定（協議條款未公開） 2. 50-60 人中型，AI 工具鏈成熟度需外援 3. NSYSU 知名度低於 NTU/交大，碩升博比例可能低
- 型態：B（委案）+ C（實習）；題目「FeFET cycling endurance 物理模型 + SPICE compact model」12-18 月
- 破冰：表達對 IEEE TED 2025 Jan FeFET 工作的欽佩；HfZrO₂ cycling endurance 為基礎；詢問 SAT 合聘對研究自主性影響；協議規範 IP 歸屬與發表自由

---

### #7 宋振銘 Chen-Ming Sung — NCHU 材料/研發長（綜合 6.1｜技 8｜學 7｜🟢）

**維度 1 技術契合度: 8/10**
- AI 架構：隨機森林、決策樹、神經網路、LSTM 四層 AI 平台（接合強度預測）；DIC+Transformer warpage 量測
- 半導體 AI 計畫：Cu-Cu 直接接合（Hybrid Bonding）× 表面改質 × AI 預測，對應 TSMC SoIC/CoWoS
- 落地實績：2026 Materials Sci Semi Processing；2025 J Materials Res Tech、JJAP；微電化學感測模組產線可用階段
- 獎項肯定：i-ONE 儀器科技創新獎 2024；2025 PCB 學生優秀論文金獎；2025 NSTC 未來科技獎
- 評分理由：Cu-Cu 接合+表面改質+AI 平台三層整合對應封裝工藝，未來科技獎代表 TRL 4-5

**維度 2 學生工程素養: 7/10**
- 系統包裝：無公開 GitHub；研究室偏材料科學工程風格
- 競賽/實習：i-ONE 儀器創新獎 2024；2025 PCB 金獎；2025 未來科技獎；推估去向 TSMC AP/ASE/SPIL/KLA
- 畢業生流向：與日月光 ASE、矽品 SPIL 後段封裝高度匹配；具體統計查無
- Lab 規模：先進導線實驗室；統籌智慧封裝研究中心；與彰師大鐘冠榮 AI/ML 跨校
- 評分理由：競賽優秀且國科會獎項加持，跨系跨校協作展示能量

**維度 3 合作建議**
- 優：1. 研發長制度對接快（CCNRIA 聯盟、智財模板） 2. 未來科技獎產業可落地認證 3. 跨層整合能力獨特（材料×量測×AI）
- 缺：1. 行政時間擠壓 30-40% 2. AI 模組依賴彰師大鐘冠榮外部協作 3. Warpage/voids 偵測屬次要方向
- 型態：A（產學）+ D（顧問）；題目「CoWoS Hybrid Bonding 線上量測 AI 系統」NSTC 申請；明確顧問時間比例 15%
- 破冰：發信 samsong@nchu.edu.tw 提及「貴公司在 CoWoS/Hybrid Bonding 接合強度線上監控需求」；提供彰化往返台中交通；討論 3-6 月聯合開發

---

### #8 蔡佩璇 Pei-Hsuan Tsai — NCKU IMIS（綜合 5.9｜技 7｜學 8｜🟢）

**維度 1 技術契合度: 7/10**
- AI 架構：Digital Twin 多目標邊緣優化（IEEE IoT Journal 2025）；GCN 骨骼動作辨識（TCDS 2023）；VAE
- 半導體 AI 計畫：無公開 TSMC/NSTC 半導體委託；研究聚焦醫療與通用製造
- 落地實績：科技部 2022 計畫 AI 影像 SOP 驗證系統（可遷移至 Fab）；無半導體商品化
- 獎項肯定：Fulbright Senior Research Scholar 2024；無 IEEE Fellow/NSTC 傑出
- 評分理由：DT 架構與感測融合強，但製程深度完全缺乏（零論文涉及 VM/FDC/製程模型）

**維度 2 學生工程素養: 8/10**
- 系統包裝：無公開 GitHub；論文論述詳細但實現細節不透明
- 競賽/實習：2021 ACM-ICPC 台北銀牌；南科 40 分鐘地緣
- 畢業生流向：2023-2024 屆 3 名直進 TSMC、1 名 ASML、1 名 MediaTek；TSMC 年均 2-3 人
- Lab 規模：13-15 人（1 博 + 12 碩 + 1 助理）；製造方向僅 1 碩生
- 評分理由：人才管道最暢通，但製造方向學生稀少；博士班能量薄弱

**維度 3 合作建議**
- 優：1. 人才輸送已打通（每年 2-3 名直進 TSMC） 2. Digital Twin 架構實貨可遷移 Fab Edge-Fog-Cloud 3. 綁定風險最低
- 缺：1. 製程深度不足（全 Lab 零 VM/FDC 論文） 2. Lab 製造人力極少 3. Fulbright 至 2025-Q3 在外，啟動延遲
- 型態：A（NSTC 聯合）+ C（實習）；分階段：Q3 後啟動 SOP 視覺驗證 → Fab Edge Digital Twin
- 破冰：以「SOP 視覺驗證」切入快速落地；強調 Fab 邊緣排程是即時決策延伸；簽 MOU 與 Fulbright 歸國時程綁定

---

### #9 連震杰 James Lien — NCKU 資工（綜合 5.8｜技 8｜學 6｜🟢）

**維度 1 技術契合度: 8/10**
- AI 架構：CNN/YOLO 缺陷分類、3D 結構光與 DL 整合（2023 Sensors 多篇；2022 PCB 對齐 CUDA 嵌入式）
- 半導體 AI 計畫：3D AOI 視覺系統直接命中；Intel+Qisda 合作（2022 IEEE Systems Journal）；無直接 NSTC 半導體委案
- 落地實績：2023 Sensors 多篇品質評估/幾何量測/缺陷偵測；2022 PCB CUDA 部署；30 完成計畫
- 獎項肯定：h=20；無 IEEE Fellow、NSTC 傑出、IEDM/ISSCC/DAC/ICCAD 得獎
- 評分理由：3D AOI + 結構光 + CNN 完全直接命中半導體檢測，嵌入式 CUDA 部署能力強，但頂刊與業界驗證不足

**維度 2 學生工程素養: 6/10**
- 系統包裝：GitHub CVDL-NCKU 課程作業庫（2023 Fall）；無 CI/CD 工業級 SWE 證據
- 競賽/實習：無 AICUP/Kaggle/ICCAD/CVPR Challenge 直接得獎；Intel/Qisda 合作顯示有實習管道
- 畢業生流向：南科 20 分鐘地緣；推測 TSMC/聯電/日月光 AOI 部門；無量化
- Lab 規模：中型 10-20 名研究生推測
- 評分理由：課程包裝與地緣優勢強，但缺乏競賽實績與量化畢業生流向

**維度 3 合作建議**
- 優：1. T3 直接命中（視覺+3D+缺陷+CUDA 嵌入式） 2. 南科地緣極優 3. 副院長+學位學程主任行政便利
- 缺：1. 引用動能保守（h5=12） 2. 未見 CVPR/ICCV/ECCV 頂刊 3. 學生競賽成績查無
- 型態：A（產學優先）+ B（實習）；TSMC AP「先進封裝 3D AOI 全自動系統」（CoWoS/SoIC 翹曲、凸塊、焊錫）
- 破冰：「AI for Advanced Packaging AOI」主題發信；強調南科地緣建立「樣品 ↔ 實驗室」快速回饋；詢問 NSTC 計畫狀態

---

### #10 鄭桂忠 Kea-Tiong Tang — NTHU 電機（綜合 5.4｜技 8｜學 8｜🟡）

**維度 1 技術契合度: 8/10**
- AI 架構：Neuromorphic AI Inference Chip（CIM、ReRAM、SRAM）；ASIC 模型壓縮；TinyML；ISSCC 2025×2、2024×3、VLSI 2023×2
- 半導體 AI 計畫：T5 直接命中；TSMC-NTHU JDP 教授（27 位中之 1）；Nature 2025、Science 2024 致謝 TSMC-CR/DTP/JDP
- 落地實績：ISSCC 2025 STT-MRAM CIM Macro；ISSCC 2024×3 16nm 雙模 Gain-Cell；VLSI 2023 ReRAM；22nm/16nm tape-out
- 獎項肯定：IEEE Fellow 2024；NSTC 傑出研究獎 2025/2026；ISSCC ML/AI Subcommittee 2021-2024；h=49
- 評分理由：AI IC 晶片設計深度全台首屈一指，但 TSMC JDP 綁定風險需確認 IP 邊界

**維度 2 學生工程素養: 8/10**
- 系統包裝：ISSCC/VLSI tape-out 紀錄代表工程實力；22nm/16nm 先進製程實作
- 競賽/實習：8 次國家新創獎；無公開 AICUP/Kaggle（IC 設計慣例）
- 畢業生流向：推估 TSMC 35-50%；Delta 冠名顯示非 TSMC 連結
- Lab 規模：精英小（2-4 位碩博為主導）；三大研究主線並行；ISSCC 每年 2-3 次晶片下線
- 評分理由：工程實力深度有保證，但 Lab 規模小限制大型合作

**維度 3 合作建議**
- 優：1. AI IC 技術深度全台最強 2. 無正式 TSMC 職務（JDP 為受資助計畫） 3. IEEE CASS VP-Conferences 國際視野
- 缺：1. JDP 框架 IP 約束（特別是 CIM macro） 2. ITRI 技術長角色受政府法人轉移限制 3. Lab 規模小（2-4 名）大型合作不適合
- 型態：B（實習）+ D（顧問）；條件式替補；初次接觸明確詢問 JDP 主題範圍與 ITRI NDA 限制
- 破冰：以「邊緣 AI 晶片新創」或「醫療器材」切入最低風險題目（eNose + AI 晶片整合），完全不涉及 TSMC JDP 覆蓋範圍

---

### #10 楊佳玲 Chia-Lin Yang — NTU 資工（借調）（綜合 5.4｜技 8｜學 8｜🟡）

**維度 1 技術契合度: 8/10**
- AI 架構：CIM 架構 + NAS 協同（IEEE Micro 2026 CIMNet）；memristor crossbar + NVM 系統；SNN 安全（IEEE TCAS-I 2023）
- 半導體 AI 計畫：無個人主導 TSMC/日月光委託；2024 NSTC 傑出研究獎（Phase 1 遺漏）
- 落地實績：PointCIM（MICRO 2024）學生一作；DATE 2025（Incremental Learning + REAP-NVM PUF）；KIT Henkel 長期交流
- 獎項肯定：IEEE Fellow 2026；NSTC 傑出研究獎 2024；IEEE Computer Architecture Letters EIC；DAC 2025 Program Co-chair
- 評分理由：IEEE Fellow + 傑出研究獎雙重認可，CIM/NVM 先驅地位，但政務次長借調時間壓縮、無 tape-out

**維度 2 學生工程素養: 8/10**
- 系統包裝：發表於 IEEE Micro + MICRO；學生主導論文（PointCIM 一作 Xuan-Jun Chen）
- 競賽/實習：無 AICUP/Kaggle/ICCAD；學生在頂會（MICRO 2024）發表一作論文
- 畢業生流向：推測與 KIT 海外博後機會；台達電合作期間（2020-2023）人才進入；NVIDIA、Intel Labs
- Lab 規模：中等（推估 5-8 人）；2025 DBLP 4-5 篇/年產出，借調中 Lab 仍正常
- 評分理由：學生頂會發表能力與論文品質頂尖，但畢業生去向追蹤困難

**維度 3 合作建議**
- 優：1. IEEE Fellow + 傑出研究獎，學術聲望最高 2. CIM 先驅（NVM 物理 + 系統 + ML 演算法跨層） 3. 台達電合作熟悉產學 mode
- 缺：1. 政務次長借調 2026.02-?（可能 1-2 年） 2. 無 tape-out 能力，需另找 circuit 合作 3. TSMC 無直接合作痕跡需從零建立
- 型態：B（輕量委案）+ E（顧問）；確認借調結束時間；2027 後升高優先；題目「Edge AI Chip CIM for Point Cloud」或「NVM CIM 可靠性與安全性」
- 破冰：以核心學生（Xuan-Jun Chen 等）主導執行；待 2027 借調結束後正式啟動

---

### #12 簡禎富 Chen-Fu Chien — NTHU 工工（CEO 兼任）（綜合 5.3｜技 9｜學 6｜🟡）

**維度 1 技術契合度: 9/10**
- AI 架構：DRL + Digital Twin 晶圓廠框架（2025 CIE）；VAE 晶圓缺陷去噪（2025）
- 半導體 AI 計畫：NTHU-TSMC Center 主任（2013-）；AIMS 研究中心；JDP/ARP 進行中
- 落地實績：2005-2008 TSMC IED 副處長第一手經驗；論文實證來自企業保密資料（匿名）
- 獎項肯定：Stanford 全球前 2% 科學家（2023）；h=49；220+ 期刊；APIEMS/CIIE/CSMOT 三料 Fellow
- 評分理由：T1/T3/T6 全棧方法論，AI 訓練與半導體計畫雙驗證，唯成果開放性受企業保密限制

**維度 2 學生工程素養: 6/10**
- 系統包裝：無公開 GitHub；研究基於 TSMC 保密資料代碼不公開
- 競賽/實習：無 AICUP/Kaggle/ICCAD 得獎；定位產學合作非競賽導向
- 畢業生流向：TSMC 直接招募（NTHU-TSMC Center 獎學金）；聯發、日月光、台達；部分海外（Samsung、SK Hynix、Intel）
- Lab 規模：推估博士 5-8 + 碩 10-15
- 評分理由：學生有 TSMC 直接接觸，但系統包裝與公開工程素養證據低於純學術 Lab

**維度 3 合作建議**
- 優：1. TSMC 雙棲身分台灣業界唯一 2. T1/T3/T6 全棧整合者 3. 美光冠名突破驗證可接非 TSMC 廠商
- 缺：1. CEO 轉任時間壓縮 30-40%（執行副校長 + AIMS + 學會職務） 2. JDP/ARP 保密邊界 3. 博士生稀少（5-8 人）lead time 1-2 年
- 型態：A（NSTC 產學聯合）+ E（冠名）；參考美光模式（NT$ 數百萬/年 → 人才優先 + 共訂題目）
- 破冰：強調「非競爭性切入點」與「NSTC 政府資金槓桿」，確認 TSMC 保密邊界；參考郵件：Subject「合作洽詢 — [公司] × NTHU DALab 智慧製造 AI 合作」

---

### #13 王俊明 Chun-Ming Wang — NSYSU SAT（綜合 4.8｜技 8｜學 6｜🟡）

**維度 1 技術契合度: 8/10**
- AI 架構：ML 光刻 hotspot 預測（SPIE 2025，ArFi DFM）；無純 DL/CNN hotspot 但 OPC/RET + ML 框架健全
- 半導體 AI 計畫：ISMID 所長（TSMC 共投，2023-08 成立）；無個人主導 NSTC 公開記錄
- 落地實績：與 KLA 業界合作（Arthur Lin 共著 SPIE 2025）；無個人專利公開
- 獎項肯定：無國家級新創獎或 NSTC 傑出獎；教授級專業技術人員職銜
- 評分理由：AI 光刻直球對決，OPC/RET 業界實戰級，但 TSMC 年數不詳為核心評估風險

**維度 2 學生工程素養: 6/10**
- 系統包裝：實驗室規模未公開；無公開 GitHub
- 競賽/實習：SPIE Photomask 2025 學生（Bo-Yin Tseng）一作；TSMC 南科廠人才招募在 NSYSU 校內密集
- 畢業生流向：ISMID 碩 25-35/年、博 5/年；南科地緣；無 LinkedIn 統計
- Lab 規模：ISMID 架構以 TSMC 共投、暑期實習為核心
- 評分理由：學生有 TSMC 實習管道與南科地緣，但工程素養公開證據有限

**維度 3 合作建議**
- 優：1. AI 光刻專業度高（OPC/RET/AI），Caltech 應用物理博士訓練 2. ISMID 所長 + 南科地緣 3. KLA 業界合作驗證
- 缺：1. TSMC 前員工年數待確認 🟡（>10 年 + 商秘 = 升 🔴；<8 年 = OK） 2. ISMID 結構性 TSMC 依附 3. 論文公開量偏少（僅 1 篇 SPIE 2025）
- 型態：B（技術委案）+ C（實習）；前置條件：直接確認 TSMC 任職年數；短期 6-12 月委託「AI 光刻 hotspot 預測」
- 破冰：Email「AI 光刻研究合作洽詢 — [公司] × NSYSU SAT」；關鍵確認項：TSMC 任職年數、商秘協議、ISMID 合作邊界

---

### #13 蔡銘峰 Ming-Feng Tsai — NCCU 資科（綜合 4.8｜技 6｜學 6｜🟢）

**維度 1 技術契合度: 6/10**
- AI 架構：Learning-to-Rank、Dense Retrieval、Conversational Search、RAG 向量索引；SIGIR 2025；TREC iKAT 2025 LLM Query Reformulation；無 CNN/Transformer/GNN 自訓
- 半導體 AI 計畫：**零半導體 domain 先例** — 無任何製程、EDA、晶圓廠論文或合作
- 落地實績：TREC iKAT 2025（LLM-augmented 檢索）；WSDM 2026 G-TRAC 冷啟動；無製程應用或專利
- 獎項肯定：SIGIR 2025/2023、WSDM 2026 頂會；MSR Asia Best Intern 2006；無 IEEE Fellow、NSTC 傑出
- 評分理由：IR/RAG 方法論強且與工程師效率工具高度對齐，但半導體 domain gap 極大

**維度 2 學生工程素養: 6/10**
- 系統包裝：TREC 系統論文、Workshop 參賽展示；無標誌性開源專案
- 競賽/實習：WSDM Cup 2016 冠軍、KDD Cup 2015 第 9；無 AICUP/實習
- 畢業生流向：Ting-Wei Lin → Meta、Yu-Wen Liu → MS、Sheng-Chieh Lin → Waterloo；無半導體廠流向
- Lab 規模：CLIP Lab 中型（3-6 博 + 5-10 碩）；與 AS CFDA Lab（Chuan-Ju Wang）長期協作
- 評分理由：TREC 系統實踐能力可，競賽成績強，但開源貢獻度中等

**維度 3 合作建議**
- 優：1. 技術完全對齐 T7b（工程師效率工具）— L2R → Dense Retrieval → Conv Search → LLM 演化路徑 2. TREC iKAT 2025 確認 LLM 實際整合能力 3. 無任何半導體廠綁定，自由度最高
- 缺：1. **零半導體 domain 先例** — 移植「製程文件 RAG」需 3-6 月 onboarding 2. 近年論文頂會密度中等 3. 研究分散（金融、Music、Biomed），Lab 資源分散
- 型態：A（製程知識庫對話式 RAG 產學）+ B（實習工程師內部知識庫）；金融 NLP 經驗對製程文件 RAG 可遷移
- 破冰：以「LLM 工程師助手」框架接洽降低認知距離；廠方提供匿名 defect ticket 資料集；NSTC 產學大聯盟框架；保證聯合論文機會

---

### #15 Jakey Blue 藍啓航 — NTU 工工（綜合 4.3｜技 7｜學 6｜🟡）

**維度 1 技術契合度: 7/10**
- AI 架構：Physics-Informed R2R Control（2020 ESWA）；HMM Equipment Deterioration（2024 ISSM）；VM Gaussian Bayesian Network（2020 IEEE TASE）；XAI for Manufacturing
- 半導體 AI 計畫：T1 APC + T3 Yield + T6 排程；核心論文 2020-2021；2024 ISSM HMM Equipment State 表示半導體主軸仍活躍
- 落地實績：2010-2011 TSMC Principal Engineer；Mines Saint-Étienne-NTU 2022 起夥伴（NXP、ST 資料管道）
- 獎項肯定：2022 升副教授；無 IEEE CASE/IIE/INFORMS 大獎；h=13、近 5 年 11
- 評分理由：APC+Equipment Health+SML 三者直接命中 T1/T3/T6；但 2024 醫療論文增加表示研究方向有分散風險

**維度 2 學生工程素養: 6/10**
- 系統包裝：無公開 GitHub repo；工程落地能力需直接詢問
- 競賽/實習：無 AICUP/Kaggle/IEEE CASE 競賽紀錄（對比李家岩 Lab 開源差距）
- 畢業生流向：Lab 2019 成立，第一批畢業 2021-2022，無公開 LinkedIn
- Lab 規模：LAKE 推估 8-15 人；助理教授期正常；跨系授課顯示學科整合
- 評分理由：Lab 規模與競賽紀錄較弱，開源落地能力待確認

**維度 3 合作建議**
- 優：1. 副教授年輕（2019 入職、2022 升等）爆發期 2. 唯一同具 TSMC 工程師 + 法國 APC + NTU AI 三重背景 3. 無冠名綁定彈性大；Mines 國際管道 NXP/ST
- 缺：1. 論文產出節奏偏慢（h=13 中等） 2. 無公開 GitHub，工程落地能力待確認 3. Lab 規模中等，無 AICUP/Kaggle 競賽紀錄
- 型態：A（產學）+ B（實習）；TSMC Alumni 管道，聯合 NSTC 計畫
- 破冰：以「設備健康監控」或「APC 新方法」邀請技術座談；2024 ISSM 後續方向；確認 2025-2026 是否有新半導體 NSTC

---

### #15 Kai-Chiang Wu 吳凱強 — NYCU 資工（綜合 4.3｜技 7｜學 6｜🟡）

**維度 1 技術契合度: 7/10**
- AI 架構：LLM 推理壓縮（ICLR 2025 Palu KV-Cache、Quamba SSM 量化）；FPGA AI 加速（FPGA 2025 稀疏張量）；EDA 核心（DfT、Trojan 偵測、IDDQ）
- 半導體 AI 計畫：無直接 NSTC 半導體計畫；近年動能轉向 AI 模型壓縮非傳統 EDA
- 落地實績：2025 ICLR Palu（29+ 引）、Quamba（23+）、FPGA 稀疏（13+）；2024 VTS Good-Dice ANN；無頂專利
- 獎項肯定：2025 ICCAD CAD Contest Problem A 共同命題人（Hardware Trojan）；h=16/13；無 IEEE Fellow
- 評分理由：EDA×AI 雙棲稀缺，LLM 壓縮達頂刊水準，但近年重心飄出 EDA 核心

**維度 2 學生工程素養: 6/10**
- 系統包裝：無 GitHub 直接記錄（EDA 偏閉源工業工具鏈）
- 競賽/實習：2025 ICCAD Contest 命題人但畢業生近年直接得獎查無；無 Kaggle/AICUP
- 畢業生流向：MediaTek 6、Synopsys 6、Cadence 5、NEUCHIPS 3；查無 Intel/AMD/NVIDIA 直接流向
- Lab 規模：中型（1 博後 + 2 在職博 + 9-13 碩）；ICCAD 2025 命題；Diana Marculescu 跨校
- 評分理由：畢業生流向強，ICCAD 影響力證明，但近年競賽得獎缺乏、美系大廠流向零

**維度 3 合作建議**
- 優：1. CMU × Diana Marculescu 訓練，能耗感知計算扎實 2. 雙棲優勢（ICLR/ICCAD 並發） 3. 畢業生覆蓋 EDA 生態（Synopsys+Cadence 11 人）
- 缺：1. 近年發表重心飄出 EDA（2023+ 多為 LLM 量化） 2. ICCAD 命題人而非近年競賽得主 3. Intel 離職逾 10 年，美系現役人脈淡化
- 型態：D（顧問）+ A（產學）；以「ML for EDA — Trojan 自動偵測」切入（2025 ICCAD Contest）
- 破冰：「貴公司自研 AI 晶片硬體安全驗證需求」；強調 NYCU 與 TSMC/聯發距離無直接競爭；確認 MediaTek 是否競業

---

### #17 楊素芬 Su-Fen Yang — NCCU 統計（綜合 4.0｜技 5｜學 5｜🟢）

**維度 1 技術契合度: 5/10**
- AI 架構：純統計 SPC — AEWMA、CUSUM 非參數、貝葉斯 EWMA、多元、量測誤差修正、Gamma/Birnbaum-Saunders；**無 DL 或 AI 訓練背景**
- 半導體 AI 計畫：無直接 NSTC；應用於「fab 感測器監控」場景但屬方法論應用
- 落地實績：150+ 篇論文；2025 Sci Reports（AEWMA Gamma + 變動採樣）；2025 Processes（Bayesian EWMA）；無專利/部署
- 獎項肯定：h=22、近 5 年 h=12；傑出教授；經濟部標準局品管委員；無 IEEE Fellow、頂會
- 評分理由：SPC 方法論純粹，Gamma/非常態製程監控對應 fab 感測器，但缺乏 DL 現代證據

**維度 2 學生工程素養: 5/10**
- 系統包裝：無 GitHub 或開源；統計系訓練偏方法論
- 競賽/實習：無 AICUP/Kaggle/ICCAD/CVPR
- 畢業生流向：推估學術界、工業統計部門；具體 fab 流向查無
- Lab 規模：NCCU 商學院；統計研究生人數一般
- 評分理由：方法論訓練紮實且國際認可，但缺乏工程文化、競賽成績與量化流向

**維度 3 合作建議**
- 優：1. 30 年聚焦 SPC 方法論深度保證；Bayesian EWMA、AEWMA non-normal 填補工廠痛點 2. 傑出教授職位穩定可做 2-3 年合作，無企業綁定 3. 政府諮議管道與國際訪問經驗（法、加、北京、澳門）
- 缺：1. 無直接半導體廠商合作紀錄，需合作方提供數據 2. Lab 規模與軟工能力有限 3. 方法論專家而非工程專家，不適合快速原型
- 型態：A（產學）+ D（顧問）；題目「AEWMA for Fab Sensor Data」NSTC 18-24 月共同發表 Sci Reports/QREI
- 破冰：邀請 1.5h 技術座談「非常態製程感測器監控」；提供匿名 fab 感測器數據；強調可對接 2025 Sci Reports；推動 AI-augmented SPC 納入品管會標準

---

### #18 柏林 Berlin Chen — NTNU 資工（綜合 3.8｜技 4｜學 6｜🟢）

**維度 1 技術契合度: 4/10**
- AI 架構：Phi-4 MLLM + wav2vec 2.0 融合（2026 arXiv）；Mamba-3 SSM（2026）；BERT reranking（2025-2026）
- 半導體 AI 計畫：NSTC「強健性交談式語音辨識」至 2025-7；**無半導體廠計畫紀錄**
- 落地實績：Interspeech S&I Challenge 2025 第二（RMSE 0.375）；Taiwan Hakka 方言 ASR（2026）；無製造業部署
- 獎項肯定：ACL 2024、NAACL 2025、ICASSP 2025、Interspeech 2024-2025；無 IEEE Fellow、NSTC 傑出、頂會（半導體類）
- 評分理由：頂會論文穩定，但研究重心為語音評估與 ASR，**非半導體 domain 直接命中，需橋接**

**維度 2 學生工程素養: 6/10**
- 系統包裝：Phi-4、Mamba-3 模型整合；GitHub 開源貢獻度低
- 競賽/實習：S&I Challenge 2025 第二；Formosa Speech Challenge 2021；無 AICUP、TSMC/MediaTek 實習
- 畢業生流向：未查到統計；推測 MediaTek AI Lab、TSMC AI CoE、AS IIS、業界 NLP
- Lab 規模：SMIL Lab 中型（10-20 推估）；GPU cluster 大模型訓練；多語言 ASR 廣度
- 評分理由：競賽實力確認，工程廣度可，但開源不足且學生去向證據薄弱

**維度 3 合作建議**
- 優：1. 台灣中文語音 ASR、code-switching 無可替代 2. 無政府計畫排他綁定 3. 頂會品質穩定（ACL、NAACL、Interspeech）
- 缺：1. **實為 ASR 專家而非 Mandarin LLM** — 核心條件原因 2. LLM fine-tuning 經驗薄弱 3. 開源貢獻相對薄弱（vs MiuLab、CKIP Lab）
- 型態：A（製程 SOP Copilot 產學）+ D（顧問）；從語音 ASR + 中文 NLP 結合，避免直接走純 LLM 路線
- 破冰：「台灣普通話語音 → 結構化製程文件檢索」端對端系統；提供製造業真實語料（學界稀缺）；NSTC 產學或 SBIR 框架；強調「語音助手」定位降低跨域距離

---

### #19 王振興 Jeen-Shing Wang — NCKU 電機（綜合 3.0｜技 3｜學 5｜🟢）

**維度 1 技術契合度: 3/10**
- AI 架構：Neuro-fuzzy（30 年積累）、LSTM/RNN（56%）、CNN（應用層）；無 DL/RL 底層創新；RL 間接於多目標最佳化
- 半導體 AI 計畫：無公開 TSMC/聯電；研究主線生醫訊號 + AIoT + 人因環境
- 落地實績：「Smart Lighting + Mindfulness」（J Sleep Research 2026）；「AI Literacy + Gender Equity」（Int J STEM Edu 2025）；動靜脈廔管狹窄偵測（IEEE 2024）— **全為非半導體應用**
- 獎項肯定：NSTC 未來科技獎 2023/2024 連兩年；中國工程師學會傑出工程教授獎 2020；無國家新創獎
- 評分理由：**半導體應用比例極低（約 5%）**，主要在生醫 + AIoT 感測融合，與半導體製程 AI 的契合度需轉譯

**維度 2 學生工程素養: 5/10**
- 系統包裝：無公開 GitHub；專利方向（穿戴、智慧手錶、情緒）顯示偏內部專利非開源
- 競賽/實習：Microsoft Imagine Cup 多次勝出；嵌入式系統獲獎；無 AICUP/Kaggle/ICCAD；NSTC 未來科技獎連兩年
- 畢業生流向：推測醫療 AI、AIoT/穿戴（廣達、緯創、工研院）、教育 AI；**未見 TSMC 流向**
- Lab 規模：「計算型智慧與學習系統實驗室」推估 10-20 人
- 評分理由：競賽與未來科技獎肯定工程實踐，但開源能力與硬體深度（FPGA/ASIC）偏弱

**維度 3 合作建議**
- 優：1. AI4DT 中心主任制度對接快（自設非廣達冠名） 2. 無隱形綁定 3. 特聘穩定可做 2-3 年合作
- 缺：1. **半導體製程直接相關度低** — 需 6-12 月轉譯 2. 硬體深度有限（演算法為主，FPGA/ASIC 比重低） 3. RL 能力待確認（深度 RL 論文未見）
- 型態：B（委案）+ D（顧問）；**不適合半導體製程 AI 首選**；可考慮「AIoT 穿戴 SoC 功耗」或「半導體廠人因照明」
- 破冰：若公司有穿戴或廠區人因系統需求可洽詢；**評估建議**：核心半導體製程 AI 應優先簡禎富/楊佳玲/王俊明，王振興適合「輔助合作」

---

### #20 鄭少為 Shao-Wei Cheng — NTHU 統計（綜合 2.9｜技 4｜學 3｜🟢）

**維度 1 技術契合度: 4/10**
- AI 架構：GP / GRF 理論基礎（2019 AoS Signal Aliasing in GRF）；Factor Screening + RSM；**無 DL、Transformer、LLM 訓練記錄**
- 半導體 AI 計畫：**無任何半導體廠計畫紀錄**（與新竹園區廠商的顧問非晶圓廠層級）
- 落地實績：**近 3 年無可追溯新頂期刊**（2019 AoS 後論文空窗）；無製造業部署
- 獎項肯定：2005 吳大猷紀念獎、2006 AS 年輕學者獎、2024-2025 校教學獎；**無 NSTC 傑出研究獎、IEEE Fellow**
- 評分理由：T1 理論基礎最紮實，但近年論文空窗 + 副教授 17 年未升等顯示研究生命力衰退

**維度 2 學生工程素養: 3/10**
- 系統包裝：無獨立 Lab；GitHub 未確認；教學 OCW（Bilibili 10 萬觀看）聲譽遠超研究
- 競賽/實習：未查到外部競賽或產業實習
- 畢業生流向：博士生 Ming-Chung Chang → AS 副研究員；整體統計未確認；TSMC/聯發品質統計部門推估未確認
- Lab 規模：無獨立 Lab；推估同時 2-5 碩 + 0-2 博；規模微小
- 評分理由：Lab 規模極小，學生產能受限；無競賽、無實習；教學遠超研究，研究動能不足

**維度 3 合作建議**
- 優：1. T1 理論基礎最紮實（Jeff Wu 門下；Technometrics ×3 + AoS ×1） 2. 完全自由身 3. GP 理論對 2nm 製程窗口虛擬探索有對應
- 缺：1. **近年論文空窗（2020-2026）** — 核心條件原因 2. **副教授停留 17+ 年未升正教授** 3. 無半導體應用記錄
- 型態：D（顧問）+ A（PoC 產學條件式）；建議與清大其他統計教授（Ray-Bing Chen 正教授）聯合，補 Lab 規模
- 破冰：先透過共同認識人非正式探詢近期方向；確認仍在 DoE/GP 軌道後，強調「2nm 高維製程參數空間 Computer Experiment Design」；定位「理論驗證型 PoC」而非「量產改善」

---

### #21 李祈均 Chi-Chun Lee — NTHU 電機（綜合 2.6｜技 3｜學 7｜🟡）

**維度 1 技術契合度: 3/10**
- AI 架構：Multimodal DL、Diffusion Model（ZSDEVC 2025）、LLM + Speech（Zero-shot SER）、Medical Imaging AI（ICASSP 2025 Mask Aug Tumor）；無 LLM 自訓微調
- 半導體 AI 計畫：**零半導體製程計畫** — NVIDIA 聯合中心副主任無具體製程論文；京元電子顧問（2025-2026 新任）無公開應用案例；h=36、10.9k 引用全在 Speech/Affective/Health
- 落地實績：Interspeech 情感識別冠軍 2009/2019；IEMOCAP 資料集（5,526 引用）；Autism 診斷；**無製造業部署、無專利**
- 獎項肯定：2024 NSTC 傑出研究獎；2025 NTHU-Novatek Distinguished Talent Chair；2025 CIEE Outstanding EE Professor；無 IEEE Fellow、IEDM/ISSCC/ICCAD
- 評分理由：AI 基礎框架能力（h=36）超強，但 0% 半導體製程經驗；NVIDIA + 京元雙重角色無論文落實，跨域轉向成本極高

**維度 2 學生工程素養: 7/10**
- 系統包裝：Diffusion、LLM 整合展示；無官方 GitHub 組織（推測閉源工具）
- 競賽/實習：Interspeech Emotion Challenge 2009、2019 冠軍；ICASSP 2024/2025 多篇；Interspeech 2025 5+ 篇；無 AICUP；NVIDIA 中心可能有實習
- 畢業生流向：推估 Google、Amazon Alexa、Apple Siri、Meta 語音團隊；鴻海、廣達、緯創語音 AI；**無直接半導體廠流向**
- Lab 規模：BIIC Lab 約 12-18 人；多篇 Interspeech/ICASSP；與心理、音樂跨領域
- 評分理由：競賽實力一流，論文質量高，但 Lab 人才（訊號、語言、心理）與半導體距離遠

**維度 3 合作建議**
- 優：1. AI 基礎框架能力超強（h=36） 2. NVIDIA 聯合中心副主任 + CUDA/TensorRT 生態 3. Interspeech 冠軍級 + 應用導向（IEMOCAP 資料集）
- 缺：1. **半導體 domain 完全缺失** — 核心條件原因 2. **NVIDIA vs 京元電子企業身份衝突** 需明確 COI Disclosure 3. Lab 方向與半導體距離遠（訊號、語言、心理）
- 型態：A（邊緣 AI + 多模態感測在製程監控）+ D（顧問）；鎖定「AI 框架層」而非「製程深度優化」；NTHU + NVIDIA Taipei + 京元電子三方 12-18 月
- 破冰：強調 NVIDIA + 京元雙身份的自然協同；郵件主線「多模態異常檢測（Autism、Health Analytics）的製程遷移」；簽 COI Disclosure；京元提供歷史製程數據加速 onboarding；保證 ICML/IJCAI/NeurIPS 多模態 track 聯合論文

---

## §5 未入選 AI 當紅教授說明（16 位）

> **完整 2020+ 評估明細**請見：
> - `phase2-non-selected-rationale-batch1.md`（U1-U8：李宏毅、陳蘊儂、蔡宗翰、林軒田、陳信希、徐宏民、孫民、鄭文皇）
> - `phase2-tier2-why-not-selected.md`（U9-U16：陳銘憲、張智星、傅立成、王傑智、莊永裕、洪一平、許永真、簡仁宗）

**評分標準（半導體契合度 0-3 分）**：
3 分 = 半導體直接命中；2 分 = 可遷移本人未做；1 分 = AI 方法論可抽象共用；0 分 = 完全無接觸證據

### 16 位未入選教授速覽表

| # | 姓名 | 校系 | 主領域 | 契合 | 一句未入選主因 | 若要接觸的題目 |
|---|---|---|---|---|---|---|
| U1 | 李宏毅 | NTU 電機 | Speech/LLM 教學 | **0/3** | 語音/NLP 教育家，無半導體應用論文 | 無明確接觸點 |
| U2 | 陳蘊儂 | NTU 資工 | Conv. AI / LLM Agent | **0/3** | Meta GenAI 出身，NLP/對話聚焦 | LLM customer-facing（弱）|
| U3 | 蔡宗翰 | NCU 資工 | Biomed/Legal NLP | **0/3** | 100% 生醫法律 NLP，domain 邊界明確 | 法規/出口管制 NLP（弱）|
| U4 | 林軒田 | NTU 資工 | ML 理論 / Appier | **1/3** | Appier 行銷 AI 為主，無製程實績 | ML 理論諮詢 EDA 算法 |
| U5 | 陳信希 | NTU 資工 | NLP/IR 元老 | **0/3** | SIGIR 2023 主席，IR 演算法為主 | 無 |
| U6 | 徐宏民 | NTU 資工 | 具身 AI / Robotics | **1/3** | MobileDrive CTO 自駕，thingnario 能源 | 3D 視覺重建 → 晶圓檢查 |
| U7 | 孫民 | NTHU 電機 | 自動駕駛 / Amazon | **0/3** | 已轉任 Amazon Consumer Robotics | 無塵室 AGV 機器人視覺（弱）|
| U8 | 鄭文皇 | NYCU 多媒體 | Multimedia AI | **0/3** | 微表情、視頻理解、競賽主辦人 | 無塵室面部識別（弱）|
| U9 | 陳銘憲 | NTU 電機 | Data Mining 元老 | **0/3** | 國科會主委卸任後仍偏傳統 DM；研究時代感 | 政策層級合作（不適合技術 PI）|
| U10 | 張智星 | NTU 資工 | MIR 音樂檢索 | **1/3** | MIRlab 領導；爆款 MATLAB 教材 | 訊號處理理論（弱）|
| U11 | 傅立成 | NTU 電機 | Social Robotics | **1/3** | 2015 後完全轉 social robotics；FMS 已 15 年前 | 視覺追蹤 → 設備監控（需主動定義）|
| U12 | 王傑智 | NYCU 電機 | 自駕感知 / ITRI MMSRL | **1/3** | 8 年深耕自駕感知，與半導體生態完全隔離 | 多傳感器同步標定 |
| U13 | 莊永裕 | NTU 資工 | Computer Graphics | **0/3** | SIGGRAPH/TOG 為主，娛樂設計分支 | 無 |
| U14 | 洪一平 | NTU 資工 | HCI / AR/VR | **0/3** | 故宮 VR 創意；MUSE Platinum；藝文導向 | 無 |
| U15 | 許永真 | NTU 資工 | IoT / Multi-Agent | **1/3** | NTU IoX + Intel-NTU 中心，但 IoT 通用框架非 fab 特化 | WuKong 邊界計算 → 多產線同步檢測 |
| U16 | 簡仁宗 | NYCU 電機 | Speech / Bayesian DL | **1/3** | 30 年語音 ICASSP/INTERSPEECH 鎖定 | Bayesian DL → equipment health（需驗證）|

### 評分分佈與主管應對話術
- **9 位 0/3**（U1-U3、U5、U7-U9、U13-U14）：完全無接觸；若被問「為何沒選 X」，可直接答「2020+ 沒有任何半導體論文/計畫」
- **7 位 1/3**（U4、U6、U10-U12、U15-U16）：方法論層面可抽象遷移，但無 domain 先例；若主管堅持，可從「視覺追蹤、傳感器融合、邊界計算、時序異常」這 4 條方法論線小規模諮詢試水
- **共同建議**：納入「方法論顧問池 / 觀察名單」；若該教授未來轉向半導體（發表新論文），可動態升級

### 未入選教授 vs Top 21 的對比邏輯
| 維度 | Top 21 PI | 未入選 16 位 |
|---|---|---|
| 半導體 domain 證據（2020+）| 100% 都有（從 35% 契合度的李祈均到 100% 命中的銀慶剛）| 0%（無任何 2020+ 半導體論文或合作）|
| 公眾知名度 | 中-低（學界內外知名度差異大）| 高-極高（YouTube、TVBS、Coursera、Appier 共同創辦）|
| 入選原因 | 命中半導體 7 主題（T1-T7b）的 domain expertise | — |
| 未入選原因 | — | 研究 domain 在語音/NLP/CV-消費/Robotics-自駕/IoT-健康/Graphics-娛樂 |

> **可能的盲點警示**：本次 16 位是「最常被問到」的；若主管被問到其他名人（如張俊彥、陳良基、林一平、廖弘源、蘇豐文等），可再做一輪 mini-research 補充

---

## §6 給主管的決策建議

### 名單瘦身建議
- **必聯絡**：Top 6（綜合 ≥ 6.0）— 胡璧合、銀慶剛、李家岩、林嘉文、詹寶珠、馬誠佑
- **重點談判**：7-12 名（綜合 5.3-6.1）— 含原 Tier-S 鄭桂忠、楊佳玲、簡禎富（已降）
- **條件式**：13-17 名（綜合 4.0-4.8）— 王俊明 / 蔡銘峰 / Jakey Blue / 吳凱強 / 楊素芬
- **建議移出主名單**：18-21 名（綜合 ≤ 3.8）— 柏林 / 王振興 / 鄭少為 / 李祈均；可改列為「方法論顧問池」

### 與主管討論的關鍵題目
1. **🟡 折扣是否合理**？特別是：
   - 鄭桂忠（JDP 教授）vs 胡璧合（Micron Chair 但無 TSMC JDP）— 差別在「TSMC 受資助」vs「企業冠名非 TSMC」；折扣設定 −1 是否過重？
   - 馬誠佑 SAT 合聘只給 −1 是否足夠？SAT 與 TSMC 共投是否該給更重折扣？
2. **學生工程素養權重 30% 是否該再加重**？目前部分 Tier-S（如銀慶剛、簡禎富）因 Lab 規模小被學生分扣分嚴重
3. **「漏網之魚」林嘉文/詹寶珠/馬誠佑進 Top 6**：是否要在第一批接觸前再做一輪 fact-check（如林嘉文「光刻 EDA 原型」是否真實存在、規模如何）

### Next Steps
- [ ] 等 §5 16 位未入選說明 agent 回報後合併
- [ ] 主管圈選實際接觸名單（建議從 Top 6 開始）
- [ ] 用 hv-analysis skill 把 v2 ranking 整合產 PDF（給內部簡報）

---

