# Phase 2 Batch 2b — EDA + 封裝 4 位深度 Profile 匯總

- **執行日期**：2026-04-22
- **方法**：4 × 平行 sonnet agent + WebFetch + Google Scholar + 隱形綁定檢查
- **個別 profile 檔**：
  - `phase2-profile-chang-yao-wen.md`（張耀文）
  - `phase2-profile-wu-kai-chiang.md`（Kai-Chiang Wu 吳凱強）
  - `phase2-profile-lin-yung-chih.md`（林勇志）
  - `phase2-profile-sung-chen-ming.md`（宋振銘）

---

## 🔑 重大發現：**2 位新的 🔴 Deep Bound**

本 Batch 是 Phase 2 至今「隱形綁定命中率」最高的一輪 — 4 位裡 2 位發現 Phase 1 未標記的重大風險：

### ⚠️ 張耀文 — 🔴 **MediaTek 獨立董事（2024-5 就任）**

- **現任 MediaTek 獨立董事**，進入永續及 M&A 策略委員會
- 這不是顧問關係 — 有薪資、有法律義務
- Synopsys 技術歷史（NTUplace3/4 被收購）已結束，不構成當前綁定
- NVIDIA/Cadence/TSMC/Siemens EDA 無綁定
- **對策**：涉及 IC Design 自動化題目需先走利益揭露程序；建議主題靠向 Packaging EDA（非 IC Design）以避開 MediaTek 業務核心

### ⚠️ 林勇志 — 🔴 **前 TSMC 13 年、現有 TSMC 專利、2021 商秘獎**

- 前 TSMC 主任工程師 → **特殊模組處經理（2010-2023）**
- **US11688717B2**（2021 申請）+ **US20240186258A1**（2023 申請）兩件 TSMC assignee 專利，林勇志共同發明人
- 2021 獲 **TSMC 黃金貿易秘密獎（銀獎）** — NDA 覆蓋範圍高不透明
- 離職僅 2.5 年（NDA 典型保護期 2-5 年，仍在窗口）
- 研究主題（晶圓對準、Hybrid Bonding、CoWoS）完全重疊 TSMC 核心 IP
- **對策**：法務先行 — IP 邊界 + NDA 期限確認後才能接觸；推薦**宋振銘**（NCHU）為林勇志的 T4 替代方案

---

## §1 4 位 Batch 2b 結論

| PI | 校/系 | 分級變動 | 關鍵發現 |
|---|---|---|---|
| **張耀文** | NTU 電機 | **🔴 MediaTek 董事風險**（Phase 1 🟡）| Phase 1 低估 — 2024-5 MediaTek 獨立董事現職 |
| **Kai-Chiang Wu** | NYCU 資工 | ✅ 🟢/🟡 Open 確認 | 研究 2022 後轉 Edge AI / LLM 壓縮；ICCAD Contest 出題人 |
| **林勇志** | NSYSU SAT | **🔴 TSMC 重大綁定**（Phase 1 🟡 推測）| 前 TSMC 13 年 + 2 件專利 + 2021 商秘獎；離職 2.5 年 |
| **宋振銘** | NCHU 材料 | ✅ 🟢 Open 確認 | Tier-S 級；研發長（🚩 行政 30-40% 時間）|

---

## §2 更新 Phase 2 Top 20（修正版，對非 TSMC 廠商）

### 🥇 Tier-S（修正後）— 5 位

1. **簡禎富** NTHU DALab 🟡（Micron 先例破）
2. **李家岩** NTU PoLab 🟢
3. **Jakey Blue** NTU 工工 🟡（TSMC alumni 2010-11，離職 15 年）→ 替補 #3 陳正剛
4. **鄭桂忠** NTHU 電機 🟡（JDP 教授，無 TSMC 正式職）→ 替補 #4 張孟凡
5. **胡璧合** NTU 電機 🟢（Micron Chair 2024）→ 從 Tier-1 升

### 🥈 Tier-1（修正後）— 6 位

6. **連震杰** NCKU 資工 🟢（南科地緣、5 項專利、CUDA 工程化）
7. **宋振銘** NCHU 材料 🟢（T4 無綁定旗艦 — **林勇志替代**）
8. **Kai-Chiang Wu** NYCU 資工 🟢/🟡（ICCAD Contest 出題人、Edge AI/LLM 壓縮）
9. **洪英超** NTU 工工 🟢（SVR Profile Monitoring，工業統計純 T1）
10. **鄭少為** NTHU 統計 🟢（DoE/GP Emulator，核實後已轉清大）
11. **楊素芬** NCCU 統計 🟢（傑出教授，EWMA/CUSUM；核實後改 NCCU）

### ⚠️ 重新分類 / 降級

- **#3 陳正剛**：🔻 條件式 Tier-A（已轉生醫）→ 改 Jakey Blue 升 Tier-S 替補
- **#4 張孟凡**：🔴 Deep Bound 對非 TSMC（TSMC CR Director）→ 改 鄭桂忠 升 Tier-S 替補
- **#6 張耀文**：⚠️ 🔴 MediaTek 董事 → 建議改做「Packaging EDA 合作」避開 IC Design；若本公司與聯發科業務重疊需謹慎
- **#9 林勇志**：🔴 TSMC Deep Bound（13 年、2 專利、商秘獎）→ 改 宋振銘 升為主要 T4 PI
- **#13 彭健育**：📍 實際在中研院（非 NTHU）— 合作管道不同
- **#15 唐麗英**：📍 疑似榮休 → 改 鄭少為
- 待評估：**楊佳玲、蔡銘峰、柏林、蔡佩璇、王振興、王俊明**（Batch 2c 候選）

### 🚫 Phase 2 建議排除（對非 TSMC / 非 MediaTek 廠商）

| PI | 原因 |
|---|---|
| 張孟凡 | TSMC Corporate Research Director |
| 林勇志 | 前 TSMC 13 年 + 2 件 TSMC 專利 + 商秘獎 |
| 張耀文 | **MediaTek 獨立董事** |
| 陳正剛 | 2009 轉生醫，半導體活躍度低 |
| 唐麗英 | 疑似榮休 |
| 洪志洋、王春和、鄭宇翔 | training-data 完全幻覺（核實 pass 確認不存在） |

---

## §3 本 Batch 的方法論教訓（累計）

1. **Phase 1 的 🟡 標記可能嚴重低估 🔴 風險**
   - 張耀文 Phase 1 🟡 → 實際 🔴 MediaTek 董事
   - 林勇志 Phase 1 🟡 → 實際 🔴 TSMC 13 年資深
   - **建議**：Phase 2 深度 profile 是揭露隱形綁定的唯一可靠方法

2. **4 種新發現的 🔴 Deep Bound 類型**（全部在 Batch 1+2）：
   | PI | 類型 | 證據 |
   |---|---|---|
   | 張孟凡 | 現職董事 / Research Director | TSMC Corporate Research Director |
   | 張耀文 | 上市公司董事 | MediaTek 獨立董事 2024-5 |
   | 林勇志 | 前 13 年資深 + 未過期 NDA + 專利共有 | TSMC 特殊模組處經理 |
   | （Phase 1 已知）林本堅、王鈺強、吳安宇 | 冠名中心主任 | NTHU-TSMC、NVIDIA-NTU、MediaTek-NTU |

3. **累計 🔴 Deep Bound 名單（截至 Batch 2b）**：
   - NTU：吳安宇（MediaTek-NTU）、王鈺強（NVIDIA）、**張耀文（MediaTek 董事）**
   - NTHU：林本堅（TSMC）、**張孟凡（TSMC CR Director）**
   - NYCU：李耀仁（TSRI）、林君雄（TSMC）、YuanFu Yang（TSMC）
   - NSYSU：**林勇志（TSMC 13 年）**
   - **累計 9 位**，Phase 1 只標記了 6 位，Phase 2 多發現 3 位 ⚠️

4. **命中率統計（隱形綁定發現率）**：
   - Batch 1 Tier-S 4 位 → 2 位需重新分類（50%）
   - Batch 2a 4 位 → 1 位師承關係重要發現（25%）
   - Batch 2b 4 位 → 2 位新 🔴 Deep Bound（50%）
   - **Phase 1 分級可靠度估計約 70-75%**，剩餘 25-30% 需 Phase 2 補強

---

## §4 Phase 2 狀態（8/20 完成）

**已 profile（8 位）**：簡禎富、李家岩、陳正剛、張孟凡、Jakey Blue、鄭桂忠、胡璧合、連震杰、張耀文、Kai-Chiang Wu、林勇志、宋振銘

等等，算錯了：**12 位已完成 deep profile**（Batch 1 + Batch 2a + Batch 2b）

**剩餘 8 位未 profile**：
- Tier-1：王俊明、王振興、蔡佩璇、楊佳玲
- T7b：蔡銘峰、柏林
- 統計補強：洪英超、鄭少為、楊素芬、陳立榜

## §5 下一步建議

### 選項 A：Batch 2c（剩餘 8 位平行 profile）
8 個 parallel agents 分 2 批（4+4），完成所有 Top 20 deep profile

### 選項 B：停在這，等主管優先圈選
12 位已完成，主管可能已經有足夠資訊做 Phase 2 實際接觸

### 選項 C：全面核實 Phase 1 主表 ~150 位
鑑於 Phase 2 累計發現 3 位 Phase 1 未抓到的 🔴，主表可能還有更多 — 但這是大工程（~30 位抽樣預估 3-5 小時）
