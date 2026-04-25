# Phase 2 最終匯總 — 21/20（+1 補強完成）

- **執行期間**：2026-04-22（單日 7 批並行 deep profile + 晚間 4 組 Haiku 核實 pass + 深夜 3 組 Haiku 漏網之魚 + Phase 2 補強 5 份）
- **完成**：25/20（Phase 2 深度 profile + 銀慶剛補強 + 漏網之魚 4 位補強，水野潤身份核實後剔除）
- **方法**：23 個 sonnet agents 分 7 批並行 WebFetch + Google Scholar + 隱形綁定檢查 + 4 組 Haiku 當日現況核實 + 3 組 Haiku 11 校漏網之魚掃描 + 3 組 Haiku Phase 2 補 profile
- **Phase 1 盲點補強**：銀慶剛 Ching-Kang Ing（NTHU 統計所清華講座教授）— Phase 1 標籤偏見漏抓，補做 profile 後判定為 **Tier-S 級**（2025 IMS Fellow 台灣唯一、2014 TSMC 產學合作紀錄、2022 成大 IYM 生態半導體專利、2025 JCGS 明確應用缺陷機台識別）

## §0 2026-04-22 晚間核實 pass 重大發現

4 組 Haiku agent 對 19 位候選人做現況核實（扣除 🔴 排除 3 位），發現 **2 位重大異動** + **1 位研究方向漂移** + **2 位新榮譽加分** + **2 位論文宣稱需人工再查**：

### 🚨 重大異動（需重新評估優先度）

| PI | 異動 | 對合作影響 |
|---|---|---|
| **簡禎富**（原 Tier-S #1）| **2025-02-27 離任清華執行副校長，轉任臻鼎科技(KY)總經理（PCB 產業）** | 時間/精力大幅壓縮；清華講座教授身分保留；AIMS 中心主任與清華-台積電卓越中心主持人仍在任；合作仍可能但不再是「全時投入 PI」，建議從「立即接觸」降為「確認可用時間後接觸」 |
| **吳凱強**（原 Tier-1 #7）| **新發現：Neuchips 創鑫智慧技術顧問**（現任；AI 推論晶片新創）| 需先確認顧問合約條款；若含排他性或 AI 加速器領域限制，可能影響合作範圍；Intel 歷史關係 vs Neuchips 現任顧問兩者並存 |

### ⚠️ 研究方向漂移

| PI | 漂移方向 |
|---|---|
| **連震杰**（原 Tier-1 #6，T3 AOI）| 2025 論文多轉向醫療影像 AI（膽管、肺結節、肝腫瘤、聯邦學習）；T3 半導體 AOI 仍可合作但已非主軸 |

### ✅ 新榮譽加分

| PI | 新榮譽 |
|---|---|
| **鄭桂忠**（Tier-S #5）| 2026-02 國科會傑出研究獎；ISSCC 2025 × 2 篇持續高產 |
| **胡璧合**（Tier-S #6）| IEDM 2025 × 2 篇確認；2025-08 起兼任 GUPS（國際學院全球半導體本科課程）主任 |
| **銀慶剛**（Tier-S #3）| 2025 JASA（高維 Knockoffs Time Series）+ JCGS 論文獨立核實屬實；IMS Fellow 2025 屬實 |

### ❓ 論文宣稱無法公開核實（需人工查期刊原文）

| PI | 宣稱 | 狀態 |
|---|---|---|
| **楊素芬** | 2025 Scientific Reports + 2026 IJIE | Google Scholar / 期刊搜尋未返回結果；建議直接查 NCCU 教師頁或寄信確認 |
| **蔡銘峰** | SIGIR 2025 論文 | SIGIR 2025 proceedings 搜尋未返回其名；可能發表於不同會議（WSDM/CIKM/EMNLP）|

---

## §0b 深夜 11 校漏網之魚 pass + Phase 2 補強發現（2026-04-22）

3 組 Haiku agent 對 11 校做系統性漏網掃描（聚焦資工/工工/資管/統計/電機），經嚴格篩選剔除誤報後，確認 **3 位 Phase 1 真正漏網的頂階 PI**，隨後另派 3 組 Haiku 完成 Phase 2 深度 profile：

### ✅ 新增 Tier-1（3 位，已完成 Phase 2 profile）

| PI | 校/系 | T 類別 | 關鍵訊號 | 半導體契合 | 綁定 |
|---|---|---|---|---|---|
| **林嘉文 Chia-Wen Lin** | NTHU 電機 + 半導體學院 | T7a / T3 | IEEE Fellow 2018 + 2024 NSTC 傑出 + 2025 李國鼎會士獎；h-index 69 / 17.4k 引用；**已有光刻 EDA + 光罩修正原型** | 70% | 🟢 |
| **馬誠佑 Cheng-Yu Ma** | NSYSU 電機（合聘 SAT） | T5（FeFET/TFT）| IEEE TED 2024 × 2 + 2025 × 1；ADDA Lab；南科地緣 40 min；與胡璧合**北南 T5 雙軸互補** | 92% | 🟡 SAT |
| **詹寶珠 Pau-Choo Chung** | NCKU 電機特聘 + 電資學院院長 | T3（AOI / 缺陷檢測） | IEEE Fellow；醫學影像 DL 先驅；跨設備/域適應方法論；Phase 1 原列但未進 Top 20 | 待 PoC 驗證 | 🟢 Free |

### ⏸ 新增條件式（1 位，已完成 profile）

| PI | 狀態 |
|---|---|
| **李祈均 Chi-Chun Lee**（NTHU 電機）| Tier-2 條件式；**NVIDIA Joint Center Deputy + 京元電子顧問雙重身份 🟡**；Speech/Affective AI 半導體契合僅 35%，需轉譯；2024 NSTC 傑出研究獎 |

### 🔴 身份核實後剔除（1 位）

| PI | 原推測 | 核實結果 |
|---|---|---|
| **水野潤 Jun Mizuno** | NCKU 先進封裝中心 | **實為日本早稻田大學（Waseda）正職教授**，NCKU 為客座/訪問身份；從台灣學界名單剔除；若有興趣應 TSMC ↔ Waseda 直接協議 |

### 🚫 誤報剔除（其他 agent 建議但核查後不採納）

梁從主（NCKU 電機，本業 Power Electronics SiC/GaN 非半導體 AI）、謝明得（NCKU Miin Wu 院長，純行政）、鍾國亮/鮑興國/戴文凱（NTUST 資工，多媒體/遊戲 ML 遷移薄弱）、Mei-Chen Yeh（NTNU 行政負擔重）、廖文宏/劉昭麟（NCCU 無產業接觸點）、李毅郎/陳宏銘（NYCU 僅 EDA 課程無論文佐證）、黃義佑/陳英忠（機構混淆：ASGI 在 NTUST 不在 NSYSU）

### 漏網之魚方法論教訓

1. **NTU 零漏網** — Phase 1 對 NTU 覆蓋已完整
2. **NTHU 電機為 Phase 1 最大盲點** — 連續漏掉 2 位 2024 NSTC 傑出研究獎（林嘉文、李祈均），原因是 training-data bias 偏好「製程控制」「AI chip」，Computer Vision / Speech AI 被過濾掉
3. **合聘身份需獨立掃描** — 馬誠佑（電機系合聘 SAT）等跨系身份在單系掃描中被漏
4. **IEEE Fellow 舊榮譽 × 近期 NSTC 獎疊加 = 高信度訊號** — 未來 Phase 1 應將此組合作為獨立掃描維度
5. **「已在 Phase 1 但未進 Top 20」的中層 PI 值得二次審視** — 詹寶珠即為一例

---

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

### 🥇 第一批（立即接觸）— 5 位 Tier-S（**2026-04-22 晚間核實後排序重整**）

1. **銀慶剛**（NTHU 統計所清華講座）🟢 **新 #1** — **T1/T3 方法論頂級**；2025 IMS Fellow 台灣唯一；JASA + JCGS 2025 雙頂刊獨立核實屬實；2014 TSMC 合作先例（不良率降 11-14%、980/1000 命中率）；2022 成大 IYM 生態半導體專利；方法論可直接落地 VM feature selection / 高維 SPC / Time Series Knockoffs
2. **李家岩**（NTU PoLab）🟢 — 商業化強；T1/T3/T6 全向；NTU 資管副院長現職確認；Profet AI 顧問持續
3. **鄭桂忠**（NTHU 電機）🟡 — T2/T5 CIM 頂級（張孟凡替代）；**2026-02 國科會傑出研究獎 + ISSCC 2025 × 2 篇新榮譽**
4. **胡璧合**（NTU 電機）🟢 — T5 FeFET/M3D/CIM（Micron Chair）；**IEDM 2025 × 2 篇 + 2025-08 兼 GUPS 主任**
5. **Jakey Blue**（NTU 工工）🟡 低風險 — T1 APC 年輕活躍；師承陳正剛

### ⏸ 從 Tier-S 降至「條件式接觸」— 1 位

- **簡禎富**（NTHU DALab）🟡 可破 — **2025-02-27 轉任臻鼎科技總經理**，時間/精力大幅壓縮；T1/T3/T6 全棧方法論仍頂尖；合作仍可能但需先確認可用時間；清華-台積電卓越中心主持身分保留

> 注：原排序 Tier-S #1 簡禎富因 CEO 轉任改為「條件式接觸」；第一批主力改為 5 位：銀慶剛 / 李家岩 / 鄭桂忠 / 胡璧合 / Jakey Blue

### 🥈 第二批（短期接觸）— 8 位 Tier-1（含漏網之魚補強 3 位）

6. **連震杰**（NCKU 資工）🟢 — T3 AOI 南科地緣；⚠️ 核實發現 2025 論文多轉醫療影像 AI，半導體 AOI 仍可但非主軸
7. **宋振銘**（NCHU 材料）🟢 — T4 先進封裝 AI（林勇志替代）；⚠️ 2025 未來科技獎需人工查 PDF 得獎名單
8. **Kai-Chiang Wu 吳凱強**（NYCU 資工）🟡 **新增 Neuchips 顧問綁定** — T2 EDA + Edge AI；**核實新發現：Neuchips 創鑫智慧技術顧問**，需先確認排他條款
9. **楊素芬**（NCCU 統計）🟢 — T1 SPC 30 年無漂移，工業統計純方法論；⚠️ 2025/2026 論文宣稱需人工查期刊原文（公開搜尋未返回）
10. **蔡佩璇**（NCKU IMIS）🟢 — T6 Digital Twin（Fulbright 已於 2025-Q3 回台確認）；IoT Journal 2025 論文確認
11. **林嘉文**（NTHU 電機 + 半導體學院）🟢 🆕 漏網 — T7a Computer Vision/Video AI；IEEE Fellow 2018 + 2024 NSTC 傑出 + 2025 李國鼎會士獎；h-index 69；**已有光刻 EDA + 光罩修正原型**；半導體契合 70%
12. **馬誠佑**（NSYSU 電機/SAT）🟡 SAT 🆕 漏網 — T5 FeFET/TFT 純 device；IEEE TED 2024 × 2 + 2025 × 1；**與胡璧合形成北南 T5 雙軸互補**；南科地緣 40 min；半導體契合 92%
13. **詹寶珠**（NCKU 電機 + 電資學院院長）🟢 🆕 漏網 — T3 缺陷檢測遷移；IEEE Fellow；醫學影像 DL 先驅；跨域適應方法論直接對接 AOI；需 PoC 驗證

### 🥉 第三批（條件式 / 需確認後）— 6 位

11. **王俊明**（NSYSU SAT）🟡 — T6 AI 光刻；email 確認 TSMC 年數
12. **楊佳玲**（NTU 資工）🟡 借調中 — 2027 後 T7b/T5 CIM 架構級
13. **王振興**（NCKU 電機）🟢 — T6 AIoT；半導體契合 5% 需轉譯
14. **柏林**（NTNU 資工）🟢 — T7b ASR + 口說評估（非 LLM）
15. **蔡銘峰**（NCCU 資科）🟢🟡 — T7b RAG/IR 製程文件檢索；**無半導體 domain 先例**需廠方提供匿名資料集 onboarding；⚠️ SIGIR 2025 論文公開搜尋未返回，需再查證是否在 WSDM/CIKM/EMNLP 發表
16. **鄭少為**（NTHU 統計）🟢🟡 — T1 DoE/GP Emulator；**近 5 年頂期刊論文不可追溯**（核實再次確認：2020-2026 無可追溯新頂刊，副教授 17 年未升等，2025 獲教學獎非研究獎）；若要接觸需先確認是否有意應用
17. **李祈均**（NTHU 電機）🟡 🆕 漏網 — T7b Speech/Affective + Health Analytics；2024 NSTC 傑出研究獎；**NVIDIA Joint Center Deputy + 京元電子雙顧問**；半導體契合僅 35% 需轉譯

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
| **T1 製程控制** | 李家岩、Jakey Blue、**銀慶剛（方法論頂級 + 2014 TSMC 先例）**| 楊素芬、鄭少為（🟡 方法論顧問軌）| ⭐⭐⭐⭐⭐ |
| **T2 AI-EDA** | 鄭桂忠（CIM 硬體）| Kai-Chiang Wu、**林嘉文（光刻 EDA）🆕** | ⭐⭐⭐⭐⭐（補入林嘉文後 EDA 軸加固）|
| **T3 良率/缺陷** | 李家岩、**銀慶剛（高維缺陷追因 × Knockoffs）** | 連震杰（3D AOI，但方向漂移）、**詹寶珠（DL 跨域遷移 AOI）🆕** | ⭐⭐⭐⭐⭐ |
| **T4 先進封裝** | （林勇志排除）| **宋振銘（接棒）**| ⭐⭐⭐（弱點，建議補 NYCU 陳冠能；水野潤確認為 Waseda 非 NCKU 正職已剔除）|
| **T5 Device/新材料** | 胡璧合、鄭桂忠 | **馬誠佑 NSYSU（與胡璧合北南雙軸）🆕** | ⭐⭐⭐⭐⭐（馬誠佑補入後南部覆蓋完整）|
| **T6 智慧製造/IIoT** | 李家岩（+ 簡禎富 條件式）| 蔡佩璇、王振興（限半導體 5%）、王俊明 | ⭐⭐⭐⭐ |
| **T7a Video/Vision AI** | — | **林嘉文（Computer Vision / 設備視訊監控）🆕** | ⭐⭐⭐⭐（新開軸，林嘉文獨角戲）|
| **T7b LLM/Agentic** | （楊佳玲借調）| 柏林（實為 ASR）、**蔡銘峰（🟡 RAG/IR 核心）**、**李祈均（🟡 條件式 Speech）🆕** | ⭐⭐⭐（蔡銘峰需 domain onboarding；李祈均半導體契合僅 35%）|

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
