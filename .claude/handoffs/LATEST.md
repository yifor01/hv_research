# Handoff — TSMC PI v4.1 全面 web 核實完成 — 2026-04-25

## Goal

完成所有 71 位 PI 的 Sonnet web check 與基本資料修正，產出 v4.1 雙 PDF。

## Current State — v4.1 已完成（待 commit）

### 本次 session 完成項目

**1. 派 5 組 Sonnet agent 並行核實 A21-B60（40 位）**：每組 8 位
- Group 1 (A21-A28) / Group 2 (A29-B36) / Group 3 (B37-B44) / Group 4 (B45-B52) / Group 5 (B53-B60)
- 加派 1 組深查 A22 王蒞君實際研究領域

**2. 移除 4 位選人錯誤 PI**（總數 71 → 67）：
- B50 丁顥（Academia Sinica 統計所完整名錄查無此人）
- B55 陸元平（公開研究是 AI/智慧製造/射出成型，與封裝材料/失效分析無關）
- B56 鄭永斌（機構錯置 NTNU→NCU；半導體關聯薄弱）
- B58 羅明琇（NCCU 企管系而非資管/中研院；研究是供應鏈/服務管理）

**3. 重大狀態修正（11 位）**：
- A21 李建模 PhD UCSB → **Stanford ECE 2002**；教授 → **副教授**
- A22 王蒞君 AOI 描述為誤植 → **6G/UAV/RIS（h-54）**；定位降為精省/5G 私網顧問
- A26 張孟凡 IEEE Fellow **Class of 2026**；ISSCC 2025 三篇（非雙篇）
- A30 郭浩中 Chair → **Distinguished Professor**；五料 Fellow
- B31 高宏宇 助理教授 → **正教授**（嚴重錯誤修正；NCKU 已 10+ 年正教授）
- B34 游濟華 助理 → **副教授**
- B35 羅裕龍 特聘 → **講座教授兼工學院副院長**
- B47 李宏毅 副 → **正教授（2023 升等）**
- B48 許嘉裕 NTUT 副 → **NTHU 教授**（機構修正）
- B51 杜長慶 NCU EE → **NYCU ICST（2026/02 起）**；研究 SiQD + 功率電子並存
- B54 簡禎富 副校長 2024/07 屆滿；**2025/02 任臻鼎科技總經理** → 改不啟動
- B60 洪英超 NCCU 統計 → **NTU IE（2022/8 起）**

**4. 全 36 位 A21-B60 補完整 PhD 學校年份、h-index、Lab 名稱、4-6 條 verified URLs**

### 產出檔案

| 檔案 | 大小 | 用途 |
|---|---|---|
| `TSMC_PI_彙整大表_v4.1.pdf` | 1027.6 KB | 直向主 PDF（封面+大表+Profile+披露附錄）|
| `TSMC_PI_統一大表_橫式_v4.1.pdf` | 537.5 KB | A3 橫式大表速查 |
| `TSMC_v4_00_封面與執行摘要.md` | — | v4.1 update（含 v4.1 重大修正章節）|
| `TSMC_v4_01_統一大表.md` | — | 67 位（移除 B50/B55/B56/B58）|
| `TSMC_v4_03_統一Profile.md` | — | 56 位 S+A+B 級 Profile |

## Pending（下一個 session 待辦）

### 已知尚未驗證項目

1. **A20 郭鴻飛**：所長/副院長現任狀態待 NTUST GSAC 確認（前次 handoff 已標記）
2. **C61-C80**：「多位 Appier 綁定」需逐一核實（前次已修正 B47 李宏毅）
3. **PhD 年份未公開**：B41 林勇志 / B43 黃乾怡（已查到 1996）/ B44 楊素芬 / B53 曾釋鋒 / B59 陳正剛 等仍有少數 PhD 年份未在公開頁列出
4. **B54 簡禎富 NTHU 教職狀態**：是否留職停薪待人事室確認
5. **B38 彭文志**：TSMC 借調 2025 為內部已確認（公開資料無佐證屬正常）

### v4.0 PDF 是否保留

- 目前 v4.0 與 v4.1 兩份 PDF 並存
- 建議：commit 後可刪除 v4.0 PDF，僅保留 v4.1（避免主管混淆）

## How to Resume

打開新 session 後：

```
讀 .claude/handoffs/LATEST.md，繼續 v4.1 後續清理工作（C 級 + A20 / B54 留職停薪確認）
```

## Verification

```bash
# 確認 PDFs
ls -la reports/2026-04-tw-univ-semi-ai-professors/TSMC_PI_*v4.1.pdf

# 確認移除 4 位
grep -c "^| B5" reports/2026-04-tw-univ-semi-ai-professors/TSMC_v4_01_統一大表.md
# 應顯示 6（B49/B51/B52/B53/B54/B57/B59/B60 共 8 行，扣除 v4.0 9 行 +1 = 8）

# 樣本檢查 critical 修正
grep "B31.*高宏宇" reports/2026-04-tw-univ-semi-ai-professors/TSMC_v4_01_統一大表.md
# 應顯示「正教授」非「助理教授」
```
