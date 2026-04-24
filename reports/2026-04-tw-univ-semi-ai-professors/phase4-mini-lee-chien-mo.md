# 李建模（James Chien-Mo Li）— NTU EE / GIEE 教授｜Mini Profile

> **一句話結論**：**Tier 2**（強備選）｜無顯性企業綁定，與 MediaTek 有 Vmin prediction 合著紀錄｜**Test/Yield/Diagnosis 領域的 NTU 旗手**，研究主軸從傳統 ATPG 延伸到 **AI 晶片測試 + 量子電路測試 + ML for EDA**，正好對應 TSMC 良率工程與先進製程測試需求；與 phase 1 標的「緯創合作」可能是混淆（緯創主業 ODM 而非 IC Test，建議解讀為**廣義 IC Design House 合作**）。

---

## §1 隱形綁定速查

| 維度 | 狀態 | 備註 |
|------|------|------|
| 半導體大廠職務 | **無** | Stanford 體系（PhD 2002），返台後純學界 |
| 冠名教席 | 未發現 | — |
| 競業風險 | **低** | 與 MediaTek 有合著（Vmin prediction），非顧問 |
| Lab 開放度 | **中-高** | LaDS 實驗室開源 FAN_ATPG 工具於 GitHub，有開放精神 |

**緯創合作核實**：phase 1 提到的「緯創合作紀錄」未在 NTU 官網或李建模個人頁找到直接證據，**有可能是 phase 1 agent 幻覺**或來自次級來源。較確認的合作方為 **MediaTek**（Vmin prediction 共著）。

---

## §2 技術契合度

**研究軸線**：VLSI Test & Diagnosis（傳統強項）、**AI Chip Testing**（neuromorphic 晶片測試）、**Quantum Circuit Testing**、**ML for EDA**、ATPG（FAN 演算法）。

**近年代表工作**：
1. **FAN_ATPG（GitHub 開源）** — Fan-out-oriented ATPG 工具，是 NTU LaDS-II 的招牌工具，業界與學界都在用 → 證明李建模有「**做工具給人用**」的工程能力（這是企業合作的重要訊號）
2. **Vmin Prediction with MediaTek**（Harry Chen 共著）— 直接對應 TSMC「先進製程低電壓 corner test」題目
3. **AI Neuromorphic Chip Testing** — 方向超前，2025 後 TSMC NeuroChip 量產時是必要技術
4. **Quantum Circuit Testing** — 對應 TSMC 量子計算長期研發

**對接 TSMC 題目**：
- **T3（Yield Improvement / DFT）**：本領域核心命中
- **T2（ML-for-EDA）**：近 3 年明確轉向
- **T9（Advanced Packaging Test）**：可延伸（CoWoS/SoIC 的 KGD 測試需求）

---

## §3 Lab 與學生

- **實驗室**：Lab of Dependable Systems (LaDS)，所屬 NTU EE
- **規模**：推測 6-10 位研究生（NTU 副教授級典型規模，注意：李建模當前職稱在不同來源中為「副教授」與「教授」之間，可能近年升等）
- **學生招募訊息**：個人頁公開招收 EDA 研究生 + 大學部專題（AI tool / neuromorphic / quantum）→ **積極招生中**
- **畢業生去向**（NTU Test 領域典型）：TSMC（DFT/CAD 部門）、聯發科 Test team、Synopsys TestMAX 團隊

---

## §4 5 維度速評表

| 維度 | 分數 | 一行理由 |
|------|------|----------|
| 1. 技術命中度 | **1.5** | Test/Yield 核心命中 T3，但 placement/routing 等 EDA 主流題目較弱 |
| 2. 5 年學生招募潛力 | **1.5** | NTU 牌子穩，但 Test 領域學生總量小於 IC Design |
| 3. 企業共建 Lab 開放度 | **2** | 開源工具 + MediaTek 合著 = 業界友善 |
| 4. 資源未被搶佔程度 | **2** | Test 領域競爭者少（vs. AI/EDA），TSMC 接觸可優先卡位 |
| 5. 個人黃金期剩餘 | **1** | NTU BSEE 1993 → 推估 1971 生左右，現約 54-55 歲，黃金期 7-10 年 |
| **總分** | **8.0 / 10** | **進 Backup PDF 前 25 位推薦**，特別適合「Test/Yield 專題對接」 |

---

## §5 合作建議 + Reference

**戰略定位**：**「TSMC DFT 部門的學界對口」** — 大廠 Test 部門通常缺學界搭橋（多被 Synopsys/Cadence 顧問壟斷），李建模是可繞開 EDA 大廠、直接拿到 NTU 學生 + 工具的窗口。

**合作建議**：
1. **短期（半年內）**：以「**AI 晶片量產測試**」為題邀講，重點問 LaDS 是否願意把 FAN_ATPG 工具的 AI 加速版開放給 TSMC 內部試用
2. **中期（1-2 年）**：聚焦「**N3/N2 低電壓 Vmin 預測**」單一專題，借 MediaTek 合著經驗複製到 TSMC 內部 fab
3. **長期（3-5 年）**：考慮共建「**Quantum & Neuromorphic Test Center**」，但需確認李建模是否升等為正教授（決定計畫主持資格）

**緯創疑點處理建議**：給主管報告時應明註「**緯創合作未經一手核實，可能為 phase 1 wide net 雜訊**」，避免被當場質疑。

**Reference URL**：
1. [李建模教授簡傳 - NTU EE](https://www.ee.ntu.edu.tw/bio1.php?teacher_id=943007) — 官方 Bio
2. [Prof. James Chien-Mo Li 個人首頁](http://cc.ee.ntu.edu.tw/~cmli/) — 完整研究方向
3. [FAN_ATPG GitHub](https://github.com/NTU-LaDS-II/FAN_ATPG) — 實驗室開源代表作
