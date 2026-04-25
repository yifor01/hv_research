# Phase 2 Batch 2c — Tier-1 剩 4 位深度 Profile 匯總

- **執行日期**：2026-04-22
- **方法**：4 × 平行 sonnet agent + WebFetch + 隱形綁定檢查
- **個別 profile 檔**：
  - `phase2-profile-wang-chun-ming.md`（王俊明）
  - `phase2-profile-wang-zhen-xing.md`（**王振興 Jeen-Shing Wang** — 姓名勘誤）
  - `phase2-profile-tsai-pei-hsuan.md`（蔡佩璇）
  - `phase2-profile-yang-chia-lin.md`（楊佳玲）

---

## 🔑 本 Batch 關鍵發現

### 1. 第二位姓名勘誤：王振興 英文名
- Phase 1 記為「Zhen-Xing Wang」，正確為 **Jeen-Shing Wang**
- **AI4DT 中心**（NCKU 電機自設）≠ Quanta-NCKU AI Research Center（林一平主持）
- Phase 1 把兩個中心混淆

### 2. 楊佳玲借調政府職：2026-2-2 就任數發部次長
- 原 Phase 1 🟢 → 實際 🟡 條件性可行
- 借調期間（預估 2026-2-2 至 2027）不適合啟動新計畫
- 2027 回歸學術後可升高優先

### 3. 王俊明（NSYSU）TSMC 年數不明但風險低於林勇志
- 無商秘獎、無 TSMC assignee 專利
- Caltech 應用物理博士（純學術訓練）
- **行動**：email 確認 TSMC 年數（<8 年 = 🟡 可合作；≥10 年 + 商秘 = 🔴）

### 4. 蔡佩璇 Fulbright 赴 Pittsburgh 2024-08 至 2025-Q3
- 返台前合作啟動有時間差
- 🟢 低風險，T6 組最乾淨的候選人之一
- 學生管道強（2024 屆 3 人入 TSMC、Phison、ASML）

---

## §1 4 位 Batch 2c 結論

| PI | 校/系 | 分級 | 關鍵修正 |
|---|---|---|---|
| **王俊明** | NSYSU SAT | 🟡 | TSMC 年數不明；Caltech PhD；KLA 合作；**待 email 確認年數** |
| **王振興** | NCKU 電機 | 🟢 | **姓名勘誤 Jeen-Shing Wang**；AI4DT 中心主任（非 Quanta 冠名）；半導體 5% 需轉譯 |
| **蔡佩璇** | NCKU IMIS | 🟢 | **Fulbright Pittsburgh 2024-08 至 2025-Q3**；CV SOP 驗證直接產業可用 |
| **楊佳玲** | NTU 資工 | 🟡 | **2026-2-2 借調數發部次長**；2027 後回歸再升高優先；IEEE Fellow 2026 |

---

## §2 Phase 2 狀態（16/20 完成）

**已完成 deep profile（14 位，不含 🔴 排除）**：
- Tier-S 5 位：簡禎富 ✅、李家岩 ✅、Jakey Blue ✅、鄭桂忠 ✅、胡璧合 ✅
- Tier-1 9 位：張耀文（🔴 MediaTek）、Kai-Chiang Wu ✅、連震杰 ✅、林勇志（🔴 TSMC）、宋振銘 ✅、王俊明 🟡、王振興 🟢、蔡佩璇 🟢、楊佳玲 🟡（借調）
- 🔻 降級：陳正剛
- 🔴 Deep Bound：張孟凡（替 鄭桂忠）、林勇志（替 宋振銘）

**剩餘 4-6 位待 profile**（T7b + 統計補強）：
- **T1 統計補強**：洪英超（NTU 工工）、鄭少為（NTHU 統計，核實後）、楊素芬（NCCU 統計，核實後）
- **T7b LLM/Agentic**：蔡銘峰（NCCU 資科，RAG）、柏林（NTNU 資工，Mandarin LLM）
- **T3 Causal**（optional）：陳立榜（NCCU 統計，半導體關聯度低）

---

## §3 累計 🔴 Deep Bound 清單（截至 Batch 2c）

| # | PI | 校 | 綁定 | 來源 |
|---|---|---|---|---|
| 1 | 吳安宇 | NTU | MediaTek-NTU Center Director | Phase 1 |
| 2 | 王鈺強 | NTU | NVIDIA Research Taiwan Director | Phase 1 |
| 3 | 林本堅 | NTHU | TSMC 前副總、冠名 Director | Phase 1 |
| 4 | 李耀仁 Yao-Jen Lee | NYCU | TSRI 16 年 | Phase 1 |
| 5 | 林君雄 Chun-Hsiung Lin | NYCU | 前 TSMC R&D Manager | Phase 1 |
| 6 | YuanFu Yang | NYCU | 前 TSMC Data Scientist | Phase 1 |
| **7** | **張孟凡** ⚠️ | **NTHU** | **TSMC CR Director 現職兼任** | **Phase 2 Batch 1 發現** |
| **8** | **張耀文** ⚠️ | **NTU** | **MediaTek 獨立董事 2024-5** | **Phase 2 Batch 2b 發現** |
| **9** | **林勇志** ⚠️ | **NSYSU** | **前 TSMC 13 年 + 2 專利 + 商秘獎** | **Phase 2 Batch 2b 發現** |

**Phase 1 → Phase 2 的分類準確度**：
- Phase 1 標記 6 位 🔴
- Phase 2 額外發現 3 位 🔴
- **Phase 1 對 🔴 綁定的識別率 ~67%**（6/9）

---

## §4 下一步：Batch 2d（最後一批，5 位平行）

依照 Auto mode 原則繼續執行：
- 🥇 洪英超（NTU 工工，T1 SPC/Profile Monitoring）
- 🥇 鄭少為（NTHU 統計，T1 DoE/GP，核實後搬到 NTHU）
- 🥇 楊素芬（NCCU 統計，T1 SPC，核實後搬到 NCCU）
- 🥇 蔡銘峰（NCCU 資科，T7b RAG/IR，工程師 copilot 關鍵）
- 🥇 柏林 Berlin Chen（NTNU 資工，T7b Mandarin LLM）

**完成後**：全部 Top 20 都有 deep profile，進入主管圈選階段。
