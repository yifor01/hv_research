# Phase 2 最終匯總 — 19/20 完成

- **執行期間**：2026-04-22（單日 5 批並行 deep profile）
- **完成**：19/20（剩 2 位因 agent 打限額，隔日可補）
- **方法**：20 個 sonnet agents 分 5 批並行 WebFetch + Google Scholar + 隱形綁定檢查

---

## §1 Phase 2 五批狀態表

| Batch | 完成數 | 內容 | 主要發現 |
|---|---|---|---|
| Batch 1 Tier-S | 4/4 | 簡禎富 ✅ / 李家岩 ✅ / 陳正剛 🔻 / 張孟凡 🔴 | **張孟凡 新 🔴 Deep Bound** 發現 |
| Batch 2a 關鍵 | 4/4 | Jakey Blue ✅升 / 鄭桂忠 ✅升 / 胡璧合 ✅升 / 連震杰 ✅ | Jakey Blue **師承陳正剛**；姓名勘誤「連仁傑 → 連震杰」 |
| Batch 2b EDA/封裝 | 4/4 | 張耀文 🔴 / Kai-Chiang Wu ✅ / 林勇志 🔴 / 宋振銘 ✅ | **張耀文 MediaTek 董事 + 林勇志 前 TSMC 13 年** 兩位新 🔴 |
| Batch 2c Tier-1 剩 | 4/4 | 王俊明 🟡 / 王振興 ✅ / 蔡佩璇 ✅ / 楊佳玲 🟡 | **楊佳玲 借調數發部次長**；姓名勘誤「Zhen-Xing → Jeen-Shing Wang」 |
| Batch 2d 統計+T7b | 3/5 | 洪英超 ⚠️轉向 / 楊素芬 ✅ / 柏林 ✅ / ~~蔡銘峰~~ / ~~鄭少為~~ | **洪英超 2012 後 10 年未做 SPC**；柏林實為語音辨識非 LLM |

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

### 🥇 第一批（立即接觸）— 5 位 Tier-S

1. **簡禎富**（NTHU DALab）🟡 可破 — T1/T3/T6 全棧
2. **李家岩**（NTU PoLab）🟢 — 商業化強；T1/T3/T6 全向
3. **Jakey Blue**（NTU 工工）🟡 低風險 — T1 APC 年輕活躍
4. **鄭桂忠**（NTHU 電機）🟡 — T2/T5 CIM 頂級（張孟凡替代）
5. **胡璧合**（NTU 電機）🟢 — T5 FeFET/M3D/CIM（Micron Chair）

### 🥈 第二批（短期接觸）— 5 位 Tier-1

6. **連震杰**（NCKU 資工）🟢 — T3 3D AOI 南科地緣
7. **宋振銘**（NCHU 材料）🟢 — T4 先進封裝 AI（林勇志替代）
8. **Kai-Chiang Wu**（NYCU 資工）🟢 — T2 EDA + Edge AI
9. **楊素芬**（NCCU 統計）🟢 — T1 SPC 30 年無漂移，工業統計純方法論
10. **蔡佩璇**（NCKU IMIS）🟢 — T6 Digital Twin（2025-Q3 Fulbright 回）

### 🥉 第三批（條件式 / 需確認後）— 4 位

11. **王俊明**（NSYSU SAT）🟡 — T6 AI 光刻；email 確認 TSMC 年數
12. **楊佳玲**（NTU 資工）🟡 借調中 — 2027 後 T7b/T5 CIM 架構級
13. **王振興**（NCKU 電機）🟢 — T6 AIoT；半導體契合 5% 需轉譯
14. **柏林**（NTNU 資工）🟢 — T7b ASR + 口說評估（非 LLM）

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

### ⏭ 待補 profile（reset 後隔日）— 2 位

- **蔡銘峰**（NCCU 資科）— T7b RAG/IR（agent 打限額，12pm Asia/Taipei reset 後補）
- **鄭少為**（NTHU 統計）— T1 DoE/GP（agent 打限額）

---

## §6 7 大主題覆蓋度（最終版）

| 主題 | 第一批 PI | 第二批 PI | 深度 |
|---|---|---|---|
| **T1 製程控制** | 簡禎富、李家岩、Jakey Blue | 楊素芬、（蔡銘峰待補、鄭少為待補）| ⭐⭐⭐⭐⭐ |
| **T2 AI-EDA** | 鄭桂忠（CIM 硬體）| Kai-Chiang Wu | ⭐⭐⭐⭐（張孟凡/張耀文排除後仍足）|
| **T3 良率/缺陷** | 李家岩、簡禎富 | 連震杰（3D AOI 命中）| ⭐⭐⭐⭐⭐ |
| **T4 先進封裝** | （林勇志排除）| **宋振銘（接棒）**| ⭐⭐⭐（弱於預期，可考慮補 NYCU 陳冠能 ICST 院長）|
| **T5 Device/新材料** | 胡璧合、鄭桂忠 | （張孟凡排除對 TSMC 外）| ⭐⭐⭐⭐ |
| **T6 智慧製造/IIoT** | 簡禎富、李家岩 | 蔡佩璇、王振興（限半導體 5%）、王俊明 | ⭐⭐⭐⭐ |
| **T7b LLM/Agentic** | （楊佳玲借調）| 柏林（實為 ASR）、（蔡銘峰待補）| ⭐⭐（弱，需蔡銘峰補回）|

### T4 / T7b 薄弱點

- **T4 僅 1 位主力（宋振銘）**：建議可以補 NYCU 陳冠能（ICST 院長）做 2 分之 1 profile
- **T7b 核心待蔡銘峰補回**：RAG on 製程文件是工程師生產力工具核心，蔡銘峰是必要拼圖

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

### 選項 A：補完最後 2 位（推薦）
- Asia/Taipei 12pm reset 後重新 launch 2 個 agents：蔡銘峰 + 鄭少為
- 完成後 Phase 2 達 20/20，100% 覆蓋

### 選項 B：進入主管圈選階段
- 14 位有 deep profile（14 位可上接觸清單）
- 依照 §5 的 3 批次順序主動聯絡
- 從「第一批 5 位 Tier-S」開始，每週 1-2 位線上邀約

### 選項 C：T4 補強（可選）
- 補 NYCU 陳冠能（ICST 院長）做 profile
- 目前 T4 僅宋振銘 1 位主力

### 選項 D：產出最終 PDF 研究報告
- 用 `hv-analysis` skill 把所有 14 份 profile + 清單 + 圖表整合成 PDF
- 主管可帶著 PDF 去做內部簡報
