# Handoff: TSMC v4.0 統一大表 + Rubric v2.0 披露規則 — 已 ship
Generated: 2026-04-24 19:46 Asia/Taipei
Branch: master（待 commit）
Status: **Ready for Review**（PDF v4.0 976 KB 已生成；等待 commit & push + 用戶核對 32 位清單全部覆蓋）
Progress: 100% ship — Rubric v2.0 + 16 位 Haiku 快掃 + 71 位統一重評 + 6 份 MD + 單一 PDF v4.0

## 目標
回應用戶兩大需求：
1. **取消 Top 15 / Backup 二分 → 統一大表 71 位**
2. **Double-check 用戶清單 32 位**（16 位已收錄，16 位新增）
3. **系統性 refactor**：新 Rubric v2.0（合作衝突從「排除」→「漸進打分 + 披露」）

## 已完成

### Rubric v2.0 方法論
- [x] `templates/scoring-rubric-v2.md` 完成
- [x] 5 維度加權（20/25/20/20/15）；維度 4 改漸進打分 0-10
- [x] 新增「與外部公司合作狀況」專欄；取消 E ❌ 剔除類

### 16 位 Haiku 快掃（4 組並行，Haiku 4.5）
- [x] G1 NCKU：游濟華 6.9 / 羅裕龍 6.8 / 劉禹辰 6.4 / 謝旻甫 5.6
- [x] G2 NYCU：王蒞君 7.3 / 吳添立 6.9 🚩 / 郭浩中 6.9 🚩 / 陳柏宏 6.9
- [x] G3 NCU：陳以錚 6.6 / 林錦德 6.15 / 杜長慶 5.75 / 鄭永斌 4.95 🚩
- [x] G4 技職/其他：**楊哲化 8.1 S ⭐⭐** / 陸元平 5.1 / 羅明琇 4.7 / 林清安 4.0

### 校系/姓名修正
- [x] 藍啓航 → **藍俊宏**（NTU 工工副教授正名）
- [x] 高宏宇 NCKU 正教授 → **NTHU 助理教授**（2024/8 轉校）

### 71 位統一重評（55 原 + 16 新）
- [x] E ❌ 5 位重評納入（張耀文 7.3 / 張孟凡 7.2 / 彭文志 6.4 / 水野潤 7.2 / 林勇志 6.3）
- [x] 優先級分佈：S 15 位 / A 14 位（含 5 🚩）/ B 30 位（含 3 🚩）/ C 12+ 位

### 6 份 v4.0 MD 檔案
- [x] TSMC_v4_00_封面與執行摘要.md
- [x] TSMC_v4_01_統一大表.md（71 位完整表）
- [x] TSMC_v4_05_合作狀況披露附錄.md（🚩 12 位 A-E 五池 + 決策矩陣）
- [x] TSMC_v4_06_方法論與版本差異.md（Rubric v2.0 + v3.4→v4.0 diff）
- [x] unified-score-table-v4.md（中間計算表，保留追蹤）

### PDF v4.0
- [x] `TSMC_PI_彙整大表_v4.0.pdf`（976 KB）— 7 章節：封面 + 統一大表 + S 級 profile 1-8 + 9-15 + 楊哲化新進 + 合作披露 + 方法論

### CHANGELOG
- [x] CHANGELOG.md 更新 v4.0 段落

## 未完成
- [ ] [P0] **commit & push**（本次 refactor 所有檔案）
- [ ] [P1] vault 同步：status.md 更新至 v4.0 + lessons.md 補 3 條方法論心得
- [ ] [P1] 驗證用戶 32 位清單全部已覆蓋（可快速掃 `grep -c` 確認）
- [ ] [P2] TSMC_v4_02/03/04 BC 級摘要檔（目前 BC 級在大表已有一句話描述，profile 檔沿用舊 Backup 資料；若主管要求獨立 BC profile 可後補）
- [ ] [P3] 吳添立 MediaTek Chair 條款法務核實
- [ ] [P3] 郭浩中 Picosun→應材 收購後延伸條款法務核實
- [ ] [P3] 楊哲化 TSMC 實際對接 — 3D 封裝 PoC 簡報邀約

## 失敗的方法（不要重複）
- **cwd 雙路徑錯誤**：cd 到 reports 子資料夾後用 `reports/2026-04-.../xxx.md` 會找不到；改用絕對路徑
- **Agent 給分跨組偏差**：G2 NYCU Haiku 給分整組 +0.3 偏樂觀（4 位全 7.0+）；G4 技職組最嚴格。校準原則：依組調整而非個案

## 關鍵決策
- **取消 E ❌ 剔除類 → 改漸進打分 + 合作狀況披露**（用戶原話：「不需要再剔除 合作衝突的部分, 寫在 與外部公司合作狀況即可」）
- **取消 Top 15 / Backup 二分** → 統一大表 71 位（用戶原話：「不要再區分 top 15 & backup」）
- **優先級切線**：S ≥ 8.0 / A 7.0-7.9 / B 5.5-6.9 / C < 5.5（用戶確認）
- **Rubric v2.0 作為 2027 盤點基準** — 版本可比性優於批次特例
- **楊哲化 8.1 S 是本次最大意外發現**（NTUT 技職院校；3D 封裝雷射超音波補位 T4 軸）

## 程式碼上下文

**v4.0 優先級分佈**：
```
S 級（≥ 8.0，15 位）：王俊明 9.0 / 江蕙如 9.0 / 馬誠佑 8.9 / 陳亮嘉 8.9 /
                     胡璧合 8.8 / 陳冠能 8.8 / 銀慶剛 8.5 / 陳智 8.4 /
                     詹寶珠 8.3 / 謝昱銘 8.3 / 楊哲化 ⭐ 8.1 / 江國寧 8.1 /
                     宋振銘 8.0 / 李家岩 8.0 / 鄭桂忠 8.0

A 級（7.0-7.9，14 位，含 🚩 5 位）
B 級（5.5-6.9，30 位，含 🚩 3 位）
C 級（< 5.5，12+ 位）
```

**🚩 高關注 12 位**（合作狀況需特別處理）：
- TSMC 內部：張孟凡 7.2（Director）、彭文志 6.4（借調處長）
- 競業獨董/Chair：張耀文 7.3（MediaTek 獨董）、吳添立 6.9（MediaTek Chair）、胡璧合 8.8（美光非獨家）
- 商秘綁定：林勇志 6.3（前 TSMC 13 年）
- 特殊身份：水野潤 7.2（日籍）、鄭芳田 7.3（已退休 72 歲）、楊佳玲 5.3（政務次長借調）
- 設備商：郭浩中 6.9（Picosun→應材）、陳智 8.4（Chemleader）
- 弱綁定：李淑敏 7.3（Synopsys/Cadence）、吳凱強 5.7（Neuchips）

**PDF v4.0 生成命令**（可複用）：
```bash
cd /home/yifor/projects/hv-research && python3 scripts/md_to_pdf.py \
  reports/2026-04-tw-univ-semi-ai-professors/TSMC_v4_00_封面與執行摘要.md \
  reports/2026-04-tw-univ-semi-ai-professors/TSMC_v4_01_統一大表.md \
  reports/2026-04-tw-univ-semi-ai-professors/TSMC_Top15_v3_02_教授檔案_1-8.md \
  reports/2026-04-tw-univ-semi-ai-professors/TSMC_Top15_v3_03_教授檔案_9-15.md \
  reports/2026-04-tw-univ-semi-ai-professors/phase5-haiku-scan/phase5-yang-che-hua.md \
  reports/2026-04-tw-univ-semi-ai-professors/TSMC_v4_05_合作狀況披露附錄.md \
  reports/2026-04-tw-univ-semi-ai-professors/TSMC_v4_06_方法論與版本差異.md \
  --title "..." --subtitle "..." --author "..." \
  --section-titles ... --section-descs ... \
  -o reports/2026-04-tw-univ-semi-ai-professors/TSMC_PI_彙整大表_v4.0.pdf
```

## 下一步（可直接執行）
1. **git add + commit**（v4.0 refactor 打包）
2. **git push origin master**
3. **vault 同步**：`python3 ~/vault/scripts/vault-cli.py ...` 或直接寫檔
4. **用戶核對**：確認 32 位清單是否全部在 v4.0 大表中（可用 `grep -c` 檢查）

## 需要載入的檔案（恢復時）
- `.claude/handoffs/LATEST.md`（本檔副本）
- `templates/scoring-rubric-v2.md`（新 Rubric 標準）
- `reports/2026-04-tw-univ-semi-ai-professors/TSMC_PI_彙整大表_v4.0.pdf`（主交付 976 KB）
- `reports/2026-04-tw-univ-semi-ai-professors/unified-score-table-v4.md`（計算表）
- `reports/2026-04-tw-univ-semi-ai-professors/TSMC_v4_00_封面與執行摘要.md`（主管摘要）

## Resume Prompt
恢復 hv-research：TSMC v4.0 統一大表 71 位（含 Haiku 快掃 16 位新增）+ Rubric v2.0 披露規則完成；PDF 976 KB 已生成；下一步 commit/push + vault 同步 + 用戶核對 32 位清單覆蓋率。
