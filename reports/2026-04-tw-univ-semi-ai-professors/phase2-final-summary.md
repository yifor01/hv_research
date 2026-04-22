# Phase 2 最終匯總 — 21/20（+1 補強完成）

- **執行期間**：2026-04-22（單日 7 批並行 deep profile）
- **完成**：21/20（全部 Phase 2 深度 profile 完成 + 1 位 Phase 1 遺漏補強）
- **方法**：23 個 sonnet agents 分 7 批並行 WebFetch + Google Scholar + 隱形綁定檢查
- **Phase 1 盲點補強**：銀慶剛 Ching-Kang Ing（NTHU 統計所清華講座教授）— Phase 1 標籤偏見漏抓，補做 profile 後判定為 **Tier-S 級**（2025 IMS Fellow 台灣唯一、2014 TSMC 產學合作紀錄、2022 成大 IYM 生態半導體專利、2025 JCGS 明確應用缺陷機台識別）

---

## §1 Phase 2 五批狀態表

| Batch | 完成數 | 內容 | 主要發現 |
|---|---|---|---|
| Batch 1 Tier-S | 4/4 | 簡禎富 ✅ / 李家岩 ✅ / 陳正剛 🔻 / 張孟凡 🔴 | **張孟凡 新 🔴 Deep Bound** 發現 |
| Batch 2a 關鍵 | 4/4 | Jakey Blue ✅升 / 鄭桂忠 ✅升 / 胡璧合 ✅升 / 連震杰 ✅ | Jakey Blue **師承陳正剛**；姓名勘誤「連仁傑 → 連震杰」 |
| Batch 2b EDA/封裝 | 4/4 | 張耀文 🔴 / Kai-Chiang Wu ✅ / 林勇志 🔴 / 宋振銘 ✅ | **張耀文 MediaTek 董事 + 林勇志 前 TSMC 13 年** 兩位新 🔴 |
| Batch 2c Tier-1 剩 | 4/4 | 王俊明 🟡 / 王振興 ✅ / 蔡佩璇 ✅ / 楊佳玲 🟡 | **楊佳玲 借調數發部次長**；姓名勘誤「Zhen-Xing → Jeen-Shing Wang」 |
| Batch 2d 統計+T7b | 3/5 | 洪英超 ⚠️轉向 / 楊素芬 ✅ / 柏林 ✅ | **洪英超 2012 後 10 年未做 SPC**；柏林實為語音辨識非 LLM |
| Batch 3 最終補 | 2/2 | 蔡銘峰 🟢🟡 / 鄭少為 🟢🟡 | 兩位均 Free Agent 零綁定；**蔡銘峰 T7b RAG/IR 契合高但無半導體 domain 先例**；**鄭少為 TSMC-JDP 未列名，但 2020+ 無可追溯頂期刊論文、副教授 17 年未升等**（最大風險點） |
| Batch 4 遺漏補強 | 1/1 | 銀慶剛 🟢 | **Phase 1 標籤偏見系統性盲點**：training-data agent 偏愛「工業統計」關鍵字明確的 PI，漏掉這位清華講座 + Academia Sinica 曾任研究員、2014 TSMC 產學合作（不良率降 11-14%）、2022 成大 IYM 生態半導體專利、2025 IMS Fellow（台灣唯一）、JCGS 明確應用缺陷機台識別的頂階 PI；判定 Tier-S 級，替換陳正剛位置 |

---

## §2 累計 🔴 Deep Bound 全景（9 位）

**Phase 1 原標 6 位**：吳安宇（MediaTek-NTU Dir.）、王鈺強（NVIDIA Dir.）、林本堅（TSMC 前副總）、李耀仁（TSRI）、林君雄（前 TSMC）、YuanFu Yang（前 TSMC）

**Phase 2 新發現 3 位**：
- **張孟凡**（NTHU 電機）— **現任 TSMC Corporate Research Director 兼任**
- **張耀文**（NTU 電機）— **MediaTek 獨立董事（2024-5 就任）**
- **林勇志**（NSYSU SAT）— **前 TSMC 13 年 + 2 專利共同發明人 + 2021 商秘獎**

**Phase 1 對 🔴 的識別率 67%（6/9）** — 33% 需 Phase 2 才能抓到

---

## §3 🟡 狀態特別處理（6 位）

| PI | 校 | 狀態 | 處理建議 |
|---|---|---|---|
| 簡禎富 | NTHU | 清華-TSMC 卓越中心主任（非排他）| Micron 冠名先例可破；合作題目避開 TSMC 核心機密 |
| 李家岩 | NTU | 有台積工作背景（過往）| 正面資訊 — 熟 TSMC 內情 |
| Jakey Blue | NTU | TSMC alumni 2010-11（離職 15 年）| 低風險，論文致謝無 TSMC |
| 鄭桂忠 | NTHU | TSMC-NTHU JDP 教授（Delta 先例）| 計畫受資助人，非機構忠誠義務 |
| 王俊明 | NSYSU | TSMC 年數不明 | **行動：email 確認**（<8 年 OK；≥10 年 + 商秘 = 🔴）|
| 楊佳玲 | NTU | 2026-2 借調數發部次長 | 2026-2027 暫緩，2027 後可升高優先 |

---

## §4 🔻 Phase 1 標籤過期（3 位）

Phase 1 靠 training-data 識別出「過去是 T1 權威」但實際活躍度已低：

| PI | Phase 1 描述 | 實際 2023-2026 狀態 |
|---|---|---|
| 陳正剛 Argon Chen | 🎯 SPC/EWMA/CUSUM 權威 | **自 2009 轉生醫，75%+ 論文超音波/OSA**，Lab 僅 3 人 |
| 洪英超 Ying-Chao Hung | 🎯 SVR Profile Monitoring | **SPC 代表作是 2012-13**，現做 EV/Granger/MC-QMC |
| 柏林 Berlin Chen | 🎯 Mandarin LLM 先驅 | **實為語音辨識（ASR）專家**，未參與 TAIDE/Taiwan-LLM |

**教訓**：Phase 1 agent 用的是「學界印象」資料，Phase 2 靠 2023-26 近期發表才能抓到現行動量。

---

## §5 推薦 Phase 2 最終清單（對非 TSMC 廠商）

### 🥇 第一批（立即接觸）— 5 位 Tier-S（**陳正剛降級，銀慶剛補入**）

1. **簡禎富**（NTHU DALab）🟡 可破 — T1/T3/T6 全棧
2. **李家岩**（NTU PoLab）🟢 — 商業化強；T1/T3/T6 全向
3. **銀慶剛**（NTHU 統計所清華講座）🟢 — **T1/T3 方法論頂級**；2025 IMS Fellow 台灣唯一；2014 TSMC 合作先例（不良率降 11-14%、980/1000 命中率）；2022 成大 IYM 生態半導體專利；2025 JCGS 明確應用缺陷機台識別；**方法論可直接落地 VM feature selection / 高維 SPC / Time Series Knockoffs**
4. **Jakey Blue**（NTU 工工）🟡 低風險 — T1 APC 年輕活躍
5. **鄭桂忠**（NTHU 電機）🟡 — T2/T5 CIM 頂級（張孟凡替代）
6. **胡璧合**（NTU 電機）🟢 — T5 FeFET/M3D/CIM（Micron Chair）

> 注：原 Tier-S 的陳正剛因 75%+ 論文已轉生醫、Lab 僅 3 人，已降至條件式降優先（見下方），Tier-S 改為 5 位（上方 1-5）+ 銀慶剛加入後實際為 6 位候選（#3 銀慶剛 可與 #5 鄭桂忠 並列優先）

### 🥈 第二批（短期接觸）— 5 位 Tier-1

6. **連震杰**（NCKU 資工）🟢 — T3 3D AOI 南科地緣
7. **宋振銘**（NCHU 材料）🟢 — T4 先進封裝 AI（林勇志替代）
8. **Kai-Chiang Wu**（NYCU 資工）🟢 — T2 EDA + Edge AI
9. **楊素芬**（NCCU 統計）🟢 — T1 SPC 30 年無漂移，工業統計純方法論
10. **蔡佩璇**（NCKU IMIS）🟢 — T6 Digital Twin（2025-Q3 Fulbright 回）

### 🥉 第三批（條件式 / 需確認後）— 6 位

11. **王俊明**（NSYSU SAT）🟡 — T6 AI 光刻；email 確認 TSMC 年數
12. **楊佳玲**（NTU 資工）🟡 借調中 — 2027 後 T7b/T5 CIM 架構級
13. **王振興**（NCKU 電機）🟢 — T6 AIoT；半導體契合 5% 需轉譯
14. **柏林**（NTNU 資工）🟢 — T7b ASR + 口說評估（非 LLM）
15. **蔡銘峰**（NCCU 資科）🟢🟡 — T7b RAG/IR 製程文件檢索；**無半導體 domain 先例**需廠方提供匿名資料集 onboarding
16. **鄭少為**（NTHU 統計）🟢🟡 — T1 DoE/GP Emulator；**近 5 年頂期刊論文不可追溯**，需確認是否有意應用；若 Yes 則可接 Virtual Fab 模擬

### 🔴 排除 3 位（對非 TSMC / 非 MediaTek）

- 張孟凡 — TSMC CR Director
- 張耀文 — MediaTek 獨立董事
- 林勇志 — 前 TSMC 13 年 + 專利 + 商秘獎

### ⏸ 條件式降優先 3 位

- 陳正剛 — 已轉生醫，顧問池即可
- 洪英超 — 10 年無 SPC，方法論顧問
- 唐麗英 — 疑似榮休

### 🚫 training-data 幻覺（剔除）— 3 位

- 洪志洋 / 王春和 / 鄭宇翔（核實 pass 確認不存在）

---

## §6 7 大主題覆蓋度（最終版）

| 主題 | 第一批 PI | 第二批 PI | 深度 |
|---|---|---|---|
| **T1 製程控制** | 簡禎富、李家岩、Jakey Blue、**銀慶剛（方法論頂級 + 2014 TSMC 先例）**| 楊素芬、鄭少為（🟡 方法論顧問軌）| ⭐⭐⭐⭐⭐ |
| **T2 AI-EDA** | 鄭桂忠（CIM 硬體）| Kai-Chiang Wu | ⭐⭐⭐⭐（張孟凡/張耀文排除後仍足）|
| **T3 良率/缺陷** | 李家岩、簡禎富、**銀慶剛（高維缺陷追因 × Knockoffs）** | 連震杰（3D AOI 命中）| ⭐⭐⭐⭐⭐ |
| **T4 先進封裝** | （林勇志排除）| **宋振銘（接棒）**| ⭐⭐⭐（弱於預期，可考慮補 NYCU 陳冠能 ICST 院長）|
| **T5 Device/新材料** | 胡璧合、鄭桂忠 | （張孟凡排除對 TSMC 外）| ⭐⭐⭐⭐ |
| **T6 智慧製造/IIoT** | 簡禎富、李家岩 | 蔡佩璇、王振興（限半導體 5%）、王俊明 | ⭐⭐⭐⭐ |
| **T7b LLM/Agentic** | （楊佳玲借調）| 柏林（實為 ASR）、**蔡銘峰（🟡 RAG/IR 核心）**| ⭐⭐⭐（蔡銘峰補回 RAG 軌，但需 domain onboarding）|

### T4 薄弱點 / T7b / T1 風險提醒

- **T4 僅 1 位主力（宋振銘）**：建議可以補 NYCU 陳冠能（ICST 院長）做 profile
- **T7b 蔡銘峰已補回**：RAG/IR 方向正確但**無半導體 domain 先例**，合作啟動需廠方提供匿名資料集做 domain onboarding
- **T1 鄭少為風險**：近 5 年頂期刊論文不可追溯，副教授 17 年未升等，建議作為「方法論顧問」而非「深度合作」PI

---

## §7 方法論總結（供未來研究參考）

### Phase 1（training-data agent 盤點）
- **覆蓋率高**（11 校 210+ 位）
- **幻覺率 ~30%**（3/10 統計補強完全幻覺）
- **對 🔴 識別率 67%**（6/9）
- **標籤過期 ~15%**（過去 vs 現在活躍度錯配）
- **姓名勘誤 2/20**（連仁傑/連震杰、Zhen-Xing/Jeen-Shing Wang）

### Phase 2（WebFetch 深度 profile）
- **隱形綁定發現率 ~20%**（4/20 發現新 🔴/🟡）
- **Phase 1 標籤過期發現率 ~15%**（3/20）
- **姓名勘誤發現率 10%**（2/20）
- **研究方向漂移發現率 15%**（陳正剛、洪英超、柏林）
- **Phase 1 系統性盲點發現（外部情報觸發）**：銀慶剛 — Phase 1 training-data agent 對「看似純方法論」的頂階 PI 有標籤偏見，漏掉了講座教授 + IMS Fellow + 有 TSMC 產學先例的人選。**啟示：未來 Phase 1 應將「講座教授／Academia Sinica 合聘／IMS/ASA Fellow」作為獨立的高優先 PI 掃描軸，不依賴「工業統計」關鍵字**

### 核實 pass（10 位）
- **完全幻覺率 30%**（3/10）
- **系所錯誤率 30%**（3/10）
- **職級/方向錯誤率 20%**（2/10）
- **完全正確率 20%**（2/10）

### 最終可信度
- **Phase 1 + Phase 2 + 核實 pass 後**，剩下的 PI 資訊可信度約 **90-95%**
- **所有進入第一接觸階段前**，建議再次 manual 校對個人頁、確認 2024-26 論文、發送邀約 email 前先查學校 alumni page

---

## §8 Next Steps

### 選項 A：進入主管圈選階段（推薦）
- 16 位有 deep profile（Tier-S 5 + Tier-1 5 + 條件式 6）
- 依照 §5 的 3 批次順序主動聯絡
- 從「第一批 5 位 Tier-S」開始，每週 1-2 位線上邀約

### 選項 B：T4 補強（可選）
- 補 NYCU 陳冠能（ICST 院長）做 profile
- 目前 T4 僅宋振銘 1 位主力

### 選項 C：產出最終 PDF 研究報告
- 用 `hv-analysis` skill 把所有 16 份 profile + 清單 + 圖表整合成 PDF
- 主管可帶著 PDF 去做內部簡報

### 選項 D：短期行動項
- email 王俊明確認 TSMC 年數（<8 年 OK；≥10 年 + 商秘 = 🔴）
- 聯絡蔡銘峰前先準備匿名製程資料集 sample 做 domain onboarding 說明
- 聯絡鄭少為前先確認其近期是否有未發表但在進行的 DoE/GP 製程相關工作
- **銀慶剛首波接觸破冰點**：2014 TSMC 合作延伸（「若當年統計模型可做到不良機台識別，2025 的 Time Series Knockoffs 能做到什麼？」）；2022 成大鄭芳田專利作品（可作為跨校合作範例）

### 選項 E：Phase 1 方法論 retrofit（中期）
- 對 NTHU、NTU 其他系所（數學所、應用數學所、資工所的方法論教授）做「非工業統計關鍵字」的第二輪掃描
- 優先指標：講座教授／Academia Sinica 合聘／IMS/ASA/IEEE Fellow／Top 期刊 Associate Editor
- 目的：補上被 Phase 1 標籤偏見漏掉的其他方法論頂級 PI
