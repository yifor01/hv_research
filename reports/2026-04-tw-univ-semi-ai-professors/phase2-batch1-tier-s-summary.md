# Phase 2 Batch 1 — Tier-S 4 位深度 Profile 匯總

- **執行日期**：2026-04-22
- **方法**：4 × 平行 sonnet agent + WebFetch + Google Scholar 深度查詢
- **個別 profile 檔**：
  - `phase2-profile-chien-chen-fu.md`（簡禎富）
  - `phase2-profile-lee-chia-yen.md`（李家岩）
  - `phase2-profile-chen-argon.md`（陳正剛）
  - `phase2-profile-chang-meng-fan.md`（張孟凡）

---

## 🔑 重大發現（Phase 1 → Phase 2 的修正）

Phase 2 深度 profile 後，4 位 Tier-S 有 **2 位需重新分類**：

| 原 Phase 1 評定 | 實際 Phase 2 發現 | 修正動作 |
|---|---|---|
| **簡禎富** Tier-S ✅ | 確認 Tier-S；Lab 名 **DALab**（非 SMART Lab）；**美光講座教授**（2018-）先例證明可接非 TSMC；IEEE/IISE Fellow 無公開紀錄，勿誤引 | **保留 Tier-S**，細節修正 |
| **李家岩** Tier-S ✅ | 確認 Tier-S；個人**有台積電工作背景**（實際內行）；GitHub `Manufacturing-Data-Science` 93 stars；Profet AI 產品顧問 → 商業化 channel 強 | **保留 Tier-S** |
| **陳正剛** Tier-S ❌ | **自 2009 大幅轉向生醫**；2022-2025 論文 75%+ 超音波影像/OSA；**近 3 年無直接半導體論文**；Lab 僅 3 名學生 | **🔻 降至「條件式 Tier-A」**：需先確認是否有意重返半導體，否則僅作方法論顧問 |
| **張孟凡** Tier-S ⚠️ | 雙頂刊（**Science 2024 + Nature 2025**）；IEEE Fellow 2026 Class；**現任 TSMC Corporate Research Director（兼任）**；Nature 2025 致謝 **4 個 TSMC 部門**；畢業生首大流向 TSMC；22nm/16nm 多次 tape-out 於 TSMC | **⚠️ 重新分類為 🔴 Deep Bound（對非 TSMC 廠商）**；對 TSMC 內部為頂級 asset，對其他半導體公司合作價值嚴重受限 |

---

## §1 4 位對照表

| 項目 | 簡禎富 ✅ | 李家岩 ✅ | 陳正剛 🔻 | 張孟凡 🔴（對非 TSMC）|
|---|---|---|---|---|
| **校/系** | NTHU IEEM | NTU 資管 | NTU IE & 機械 | NTHU 電機 |
| **職銜** | 講座教授兼執行副校長 | 教授 / 管院副院長 / EiMBA Director | 教授（準退休） | 特聘教授（兼 TSMC CR Director）|
| **Lab** | **DALab** + AIMS Center | **PoLab** (offline) | IE 小型 lab | Memory Design Lab |
| **H-index** | 49 | ~30+（Google Scholar 實測待 update）| 22 | 41 |
| **學生規模** | 10+ 博 / 20+ 碩 | 博碩~15（主站 offline）| 約 3 名 | 10-15 博 / 15+ 碩 |
| **主命中** | T1+T3+T6 全棧 | T1+T3+T6 全棧 | T1 SPC 方法論（歷史）| T5+T2 AI 晶片 |
| **GitHub** | 無（應用研究取向，非公開競賽文化）| 93 stars (Manufacturing-Data-Science) | 無 | 無（晶片 design 非 open source）|
| **產學對接** | 清華-TSMC 卓越中心主任；美光講座；NSTC STEP 聯盟 | 台積（本人）/日月光/台達/友達/華邦/Profet AI | SRC/ISMT（歷史）/DARPA Bell Labs | **TSMC-CR Director + 4 部門 JDP** |
| **Fellow** | APIEMS/CIIE/CSMOT（**IEEE/IISE 待核實**）| NSTC 工工管理學門召集人 | 無公開 Fellow 紀錄 | IEEE Fellow 2026 Class |
| **🟢🟡🔴 分級** | 🟡 Partial（美光先例可破）| 🟢 Open | 🟢（但半導體活躍度低）| 🔴 **Deep Bound（對非 TSMC）** |
| **Phase 2 建議優先** | ⭐⭐⭐⭐⭐ 第一批必訪 | ⭐⭐⭐⭐⭐ 第一批必訪 | ⭐⭐（條件式）| ⭐（若本公司非 TSMC，降為觀察/文獻追蹤）|

---

## §2 合作切入建議（逐位）

### #1 簡禎富（DALab + AIMS Center）

- **主切入策略**：A（NSTC 產學合作計畫）+ E（冠名講座 / Joint Center 模式）組合
- **成功先例**：美光講座教授（2018-）→ 已證明可接受非 TSMC 廠商的冠名資助
- **可具體題目**：
  1. **T1** — 2nm+ 製程 Virtual Metrology + Transfer Learning（減少新 recipe 冷啟動資料需求）
  2. **T3** — Wafer Bin Map root cause 診斷 × XAI（對應良率工程師效率）
  3. **T6** — AMHS RL 排程 × Digital Twin（與他 2025 DRL+DT fab 排程論文延伸）
- **風險**：執行副校長行政負擔 → 實際執行多仰賴博士後/資深博士生；清華-TSMC 卓越中心的保密條款範圍需第一次洽談時釐清
- **第一次聯絡模板**：透過 NSTC STEP 聯盟 channel 或美光講座先例 reference；邀約 30-45 分鐘線上 briefing

### #2 李家岩（PoLab）

- **主切入策略**：A（產學計畫）+ B（暑期 intern）組合；特別適合「工程師生產力工具」題目
- **獨特優勢**：
  - 本人台積電工作背景 → 熟內部 SOP，方法論「落地可用」
  - GitHub Manufacturing-Data-Science repo 93 stars → 學生開源能力強
  - Profet AI 產品顧問 → 具商業化視角，合作可走 joint IP/spin-off
- **可具體題目**：
  1. **T1+T3** — Wafer Bin Map autoencoder-based 分類（與其 IEEE TSM 論文延伸）
  2. **T6** — MARL 晶圓廠節能排程（與其 2024 IJPE MARL chiller 論文延伸）
  3. **T7b** — 製程 SOP 文件 LLM + RAG + XAI（對接他 BMB-LIME XAI 方向）
- **風險**：副院長 + EiMBA Director 雙職 → 可能僅指導方向，具體執行靠博後/博士生
- **第一次聯絡**：透過 EiMBA 校友 channel 或 NSTC 工工管理學門 channel；建議先以 Profet AI 顧問角色切入（商業對商業）

### #3 陳正剛（🔻 條件式 Tier-A）

- **重要修正**：自 2009 轉生醫，近 3 年半導體活躍度低
- **建議做法**：
  - **選項 1（保守）**：Phase 2 排除，改找 Jakey Blue（同領域 + 活躍度高）
  - **選項 2（探索）**：先 email 問「是否有意返回半導體 SPC / 可解釋 ML」；若 yes → 以方法論顧問角色邀請；若 no → 跳過
- **價值保留**：EWMA/CUSUM 方法論論文（2007, 72+ citations）仍是教學級別文獻
- **建議主管決策**：若本公司希望先做廣度合作、加速 Jakey Blue；把陳正剛定位為「顧問候選人池」

### #4 張孟凡（⚠️ 對非 TSMC 重新分級 🔴 Deep Bound）

- **重要修正**：TSMC Corporate Research Director 兼任中；Nature 2025 致謝 4 個 TSMC 部門；畢業生首大流向 TSMC
- **對不同公司身份的建議**：
  - **若本公司 = TSMC**：張孟凡是 Tier-S #1 內部資產（直接對接 CR），保持雙向資訊流通即可
  - **若本公司 = 聯電 / 美光 / 三星 / 中芯 / NVIDIA / 聯發科 / 應用材料**：**🔴 Deep Bound 建議排除**，因：
    1. 雙棲身分下研究成果實質 priority 歸 TSMC
    2. 學生去向 pipeline 已由 TSMC 鎖定
    3. 代工製程合作若涉及先進製程，JDP 框架下 IP 須經 TSMC 審核
  - **替代方案**：若本公司需要 CIM/AI 晶片方向 PI，改找 NTHU **鄭桂忠**（🟢 Open，Nature 合著者但非 TSMC 雙棲）或 NTU **胡璧合**（🟢 Open，FeFET × 3D IC × CIM）
- **文獻追蹤**：即便不合作，張孟凡的 Science/Nature 論文仍是先進製程 CIM 的 bellwether，值得持續追蹤

---

## §3 Top 20 Phase 2 清單修正建議

基於 Batch 1 發現，`phase2-recommendations.md` Top 20 應做以下調整：

| 動作 | 對象 | 修正 |
|---|---|---|
| 修正說明 | **#1 簡禎富** | Lab 名 SMART Lab → DALab；Fellow 列表只保 APIEMS/CIIE/CSMOT；美光講座教授（2018-）為「可破 🟡」先例 |
| 修正說明 | **#2 李家岩** | 補上台積電工作背景、Profet AI 顧問 |
| 🔻 降級 | **#3 陳正剛** | 從 Tier-S 降至「條件式 Tier-A」；建議替換為 **Jakey Blue（#12）上升到 Tier-S 位置** |
| 🔴 重新分級 | **#4 張孟凡** | 從 🟢 Open 改 **🔴 Deep Bound（對非 TSMC）**；視本公司立場，若非 TSMC，**建議替換為 #ref1 鄭桂忠**（NTHU 電機 AI 晶片 Nature 合著者，🟢 Open）|

### 若本公司為非 TSMC 半導體廠（推薦修正版 Top 4）

1. **簡禎富**（NTHU DALab）— 美光講座先例保護 🟢
2. **李家岩**（NTU PoLab）— 商業化落地強 🟢
3. **Jakey Blue 藍啓航**（NTU 工工）— 年輕活躍 APC 🟢
4. **鄭桂忠**（NTHU 電機）— Nature CIM 合著者、非 TSMC 雙棲 🟢

（張孟凡改為「文獻追蹤名單」；陳正剛改為「顧問候選池」）

---

## §4 下一步選項

### A. 啟動 Tier-1 Batch 2（Top 20 中 #5-#12）
- 胡璧合、張耀文、Kai-Chiang Wu、連仁傑、林勇志、宋振銘、王俊明、Jakey Blue
- 8 位平行跑 deep profile，預估 8-10 分鐘

### B. 先做跨校 Phase 1 主表抽樣核實
- 從 Phase 1 160 位（非統計補強）抽 10-15 位做核實
- 原因：Tier-S 核實發現 **2/4 需要重新分類**（張孟凡、陳正剛），Phase 1 主表可能藏更多幻覺或錯誤分級

### C. 先針對「對非 TSMC 公司」特化 Top 20
- 重新檢視所有 🟡 標註 PI（是否類似張孟凡的隱形綁定）
- 產出「for TSMC 版」 vs 「for non-TSMC 版」兩套清單

### D. 停在這、等主管圈選
- 本 Batch 1 四位個別 profile 已齊全
- 主管可直接用這些資料做 Phase 2 第一波接觸

---

## §5 本 Batch 的方法論教訓

1. **Phase 1 的 🟢🟡🔴 分級只是初步**：張孟凡在 Phase 1 被標 🟢 Open，但實際上是 🔴 Deep Bound（TSMC-CR Director 需要 Phase 2 深度查才會發現）
2. **「未來活躍度」需驗證**：陳正剛案例說明「過往是 T1 權威」不等於「現在仍在做 T1」—— 2023-2026 論文主題是真實信號
3. **Top 期刊論文致謝段是綁定證據**：Nature/Science 等頂刊的 Acknowledgments 段會透露出贊助公司多深 —— 是 Phase 2 核實的 quick-win 工具
4. **Fellow 稱號易訛傳**：Phase 1 把簡禎富掛上 "IEEE Fellow / IISE Fellow"，實際 WebFetch 找不到，需要個別核實，不能照抄 agent output

### 對 Phase 2 剩餘 16 位的建議

- **每一位都要 deep profile，不能跳過**：光靠 Phase 1 標籤決策會有 30%+ 的錯誤率
- **特別核實項**：是否有（未公開的）公司兼職、冠名中心主任、Research Director 身分
- **每一位都要看 2022-2026 代表作主題**：確認研究重心沒有偏移
- **產學合作紀錄要看論文致謝**：不是問來源，看出版物
