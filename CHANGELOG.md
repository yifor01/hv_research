# Changelog

All notable changes to the hv-research project.

Format: `## [YYYY-MM-DD]` with Added / Changed / Fixed / Removed subsections.

## [2026-04-24] (TSMC Top 15 v3.4 + Backup v1.4 — Phase 4 補強重排)

### Added
- `reports/2026-04-tw-univ-semi-ai-professors/` Phase 4 補強：14 位新 profile（10 完整 + 5 mini）+ 3 位 Top 15 退場移到 Backup
  - **NCKU IYM 三人組**：phase4-profile-cheng-fan-tien.md（鄭芳田，戰略顧問）/ phase4-profile-hsieh-yu-ming.md（謝昱銘，⭐ 進 Top 15）/ phase4-profile-tieng-hao.md（丁顥，C 類）
  - **NTHU IEEM 兩位**：張國浩（A 類首選遞補，7.8 分）/ 許嘉裕（A 類，6.5 分）
  - **NTU 補位兩位**：蔡坤諭（C 類，EUV/DFM 而非 Test）/ 陳亮嘉（⭐ 進 Top 15，8.9 分）
  - **技職院校四位**：范書愷（A+ 類，7.5）/ 郭鴻飛（A+ 類，7.5 / Mask AI 補位）/ 黃乾怡（B+，6.5）/ 曾釋鋒（B' 設備合作獨立，5.5）
  - **類別 B 五位 mini**：江蕙如（⭐ 進 Top 15，9.0）、李建模、李淑敏、陳朝鈞、蕭宏章
- `phase4-补强說明.md` — 補強動機 + 系統盲點根因 + 重排決策原則
- `TSMC_Top15_長期投資分析_v3.4.pdf`（832 KB） — Top 15 主名單 v3.4 重排，3 進 3 出
- `TSMC_Backup_備選候選名單_v1.4.pdf`（1017 KB） — Backup 擴至 55 位（v1.0 38 + Phase 4 14 + Top 15 退場 3）

### Changed
- Top 15 主名單 v3.3 → v3.4：嚴格按 5 維度評分，3 進 3 出
  - **進入**：江蕙如 9.0（NTU EE，AI-EDA 補張耀文空缺）/ 陳亮嘉 8.9（NTU 機械，光學量測補空白）/ 謝昱銘 8.3（NCKU IMIS，IYM 接班人）
  - **退出**：林嘉文 7.5（光刻 EDA 需 12 月 PoC）/ 蔡銘峰 7.0（RAG 軸退場）/ 黃瀚萱 7.0（CAG 同樣退場）
  - **邊際決策**：張國浩 7.8 vs 蔡佩璇 7.7 邊際 0.1 差，因張國浩 Powerchip + Micron Chair 🟡 待釐清，最終留任蔡佩璇
- 主管摘要：第一波從 6 位 → 8 位；NCKU IYM 學派叢一次串聯（謝昱銘執行 PI + 鄭芳田顧問 + 銀慶剛跨校）
- 5 年預算：v3.3 約 5,800-9,200 萬 → v3.4 約 7,300-11,600 萬（保守估計 5,000-8,000 萬）
- Backup 結構：v1.0 38 位 5 類 → v1.4 擴增 §1B Phase 4 補強 17 位 + §2B 個別內容 + §4 補強說明
- vault `lessons.md` 新增 4 條：系祖追溯法、跨校合作叢識別、技職院校 quota、Phase 1 標籤偏見再 4 條

### Fixed
- 重大盲點：v1.0 完全沒掃到 NCKU 製造資訊系系祖鄭芳田（IYM/AVM 創始人 + TSMC 終生合作對象）；v1.4 補上戰略顧問定位 + 弟子謝昱銘進 Top 15
- 主管原則嚴格遵守：「**不因主管點到名而上推 Top 15**」，依 5 維度校準後評分排序

## [2026-04-24]

### Added
- 新增 agentic AI 技術細節研究報告（reports/2026-04-agentic-ai-tech/）：四年演化縱向史 + 2026-04 橫向框架格局 + 七層技術實現深潛 + 橫縱交匯五組洞察。約 22000 中文字、PDF 1.4 MB、40+ 引用來源。

### Fixed
- **痘痘肌報告圖 5、圖 6 整張重畫**
  - **圖 5**：原本 8 節點圓周佈局 + 曲線/直線箭頭都不理想（線段太短、方向不直觀）。重畫成「4 上 4 下兩排閉環」— 上排生理鏈路（紅 1→2→3→4，左至右）、右側垂直箭頭（4→5）、下排混合鏈路（5→6→7→8，右至左；紅轉藍標示生理→行為轉場）、左側垂直箭頭（8→1 行為回饋上溯屏障），中央一顆「打破閉環 = 同時介入 3+ 節點」callout。
  - **圖 6**：原本 IGA 標籤飄在分支箭頭上造成重疊、虛線拖泥帶水、劇本 D 連接不清。重畫成三層決策樹 — 根節點（IGA 評估）→ 4 分支（白底小框內嵌 IGA 標籤蓋在箭頭線上，避免重疊）→ 劇本 A/B/C 匯流到「女性週期性？」問題 → 是/否分叉到劇本 D / 維持原劇本 → 匯流到「3 個月無效」鑑別診斷檢核。全圖用直線 + 精算多邊形箭頭端，所有連線都落在方框邊界上。
  - 已重新生成 PDF（1416.5 KB / 41 頁），圖 5、圖 6 分別位於第 33、34 頁。

## [2026-04-23]

### Added
- **新竹東區關埔/光埔購屋決策研究 v2 PDF**(912 KB / 51,775 字)— 基於一份審視意見書的補強版本,新增六個章節:
  - `§3.3` **平台均價差異解釋**(樂居/591/5168 差距的四個結構性原因)
  - `§5.5` **租金投報率與持有成本試算**(2~3 房毛投報 1.6~2.1%、跨區比較、房屋稅 2.0、管理費長期走勢)
  - `§5.6` **風險揭露**(土壤液化潛勢、淹水潛勢、嫌惡設施清查、耐震規格問題清單)
  - `§5.7` **學區設籍年限細則**(關埔國小 2 年設籍門檻、實務買房時程建議)
  - `§6` **v2 變更記錄**(透明交代補做什麼 / 未做什麼)
  - 附 v1 版本(843 KB / 41,050 字)作為對照
- **新竹東區關埔/光埔購屋決策研究 v1 PDF**(843 KB / 41,050 字)— 竹科工程師 2~3 房決策研究,涵蓋:
  - 縱向:從 2007 重劃起源 → 2018 悅揚/潤隆定調期 → 2020~2022 狂飆期 → 2023 平均地權 → 2024 第 7 波限貸 → 2025 量縮 42.2% → 2026 Q1 光埔二期整地 80%
  - 橫向:25+ 建商派系表 (T1 坤山/惠宇/國泰 / T2 富宇/春福 / T3 寶佳/興富發/昌益/豐邑) + 8 代表建案逐案拆解 (富宇天雋、竹科悅揚、竹科潤隆、富春居、豐邑相對論、國泰 TWIN PARK、興富發巨人愛家、遠雄文華匯) + 四區對比表(關埔/光埔二期/竹北高鐵/縣治三期)
  - 公設比解析(雨遮實坪制歷史根源 + 得房率換算 + 車位灌水陷阱)
  - 三劇本未來推演(續漲 35% / 盤整 45% / 鬆動 20%)
  - 購屋檢核清單:15 條避雷、議價框架、財務壓力測試表
- `reports/2026-04-hsinchu-east-guanpu-housing/sources.md` — 126 個引用來源分類清單
- `raw-materials/2026-04-hsinchu-east-guanpu-housing/研究筆記_縱向.md` / `研究筆記_橫向.md` — 三個並行聯網 agent 產出的原始研究素材(其中補充 agent 因 API 限流未完成,主執行緒自行補做學區/交通/醫療/台積電 A14 時程搜尋)
- **TSMC Top 15 教授投資分析 v3.2 PDF**（38 頁 / 692 KB）— 兩層結構：主管摘要 → 統一大表 → 個別教授三段細節（技術契合度 / 學生素養 / 合作分析）→ 附錄（策略/預算/法務/76 個 Reference URL）
- **TSMC 備選候選名單 v1.2 PDF**（23 頁 / 931 KB）— 38 位備選（A 差一點 4 / B 待觀察 6 / C 方向偏 3 / D 名氣大但未入選 20 / E 已失效 5）
- `phase3-verification-notes.md` — 16 位 WebSearch 平行驗證紀錄
- `templates/pi-due-diligence-framework.md` — PI 盡職調查 template（5 維度評分框架 v1.0）
- 附錄 E：每位教授 Reference URL（76 個公開連結）+ 能力限制聲明

### Changed
- 移除所有內部流程字樣（Phase 1/2/3、Batch A/B、Wave）— 主管版只有兩層結構
- 關鍵字矩陣表（20 欄）→ 改為每位教授 section 頂部「專長標籤列」（解決 PDF 寬表格切斷）
- Backup PDF 結構統一為 Top 15 式兩層（原四章四格式 confuse → 三章兩層式）
- CLAUDE.md 新增 PI 盡職調查工作流程 + 慣例（PDF 寬表格上限 / 必附 Reference URL / Companion 結構對齊）

### Fixed
- 彭文志從 Top 15 移除（已借調 TSMC 當處長，非合作候選；WebSearch 未能抓到）
- 王俊明 TSMC 綁定顧慮取消（SAT 中心為 TSMC 支持設立，體制內合作方 ≠ 離職自由身）

### Removed
- `TSMC_Top15_v3_04_關鍵字矩陣.md`（PDF 寬表格切斷問題）

## [2026-04-22]

### Added
- Phase 1-3 台灣 11 校半導體 AI 教授盤點完成
- Top 15 PDF v1 / v2
- `phase3-integrated-ranking.md`、`phase3-batch-a-llm-rag-candidates.md`、`phase3-batch-b-packaging-candidates.md`

### Changed
- Top 10 → Top 15 擴充（Batch A/B 各補 3 位）

## [2026-04-20]

### Added
- 專案初始化（CLAUDE.md / README.md / 目錄結構）
- 第一份研究：Claude Code 橫縱分析報告（13,860 中文字 / 1.1 MB PDF）
- `scripts/md_to_pdf.py`（weasyprint + markdown 工具）

## [2026-04-23]
### Added
- 新增研究報告：`reports/2026-04-acne-dehydrated-skincare/` — 痘痘肌 × 外油內乾 × 粉刺 × 內包痘的橫縱分析（縱向六階段認知史 + 橫向六大流派 + 化學成分／保養品／醫美／口服藥／內調五大治療類別 + 三個劇本推演）

## [2026-04-23] (補強版)
### Changed
- `reports/2026-04-acne-dehydrated-skincare/`：根據專業級審查意見大幅補強（7.38 → 預期 9+/10）
  - **新增 2.0 節**：IGA/GAGS/Leeds 嚴重度分級工具 + 8 種鑑別診斷（Malassezia folliculitis、Rosacea、Perioral Dermatitis、脂漏性皮膚炎、藥源性、機械性、髮蠟、Demodex）
  - **新增 H 類處方外用藥**：Dapsone gel、Minocycline foam、Epiduo/Epiduo Forte、Clindamycin 複方、Ivermectin、Ketoconazole
  - **大修 2.5 口服藥物**：補上 Metformin、Diane-35 / CPA、GLP-1（Semaglutide / Tirzepatide）、Bicalutamide、Flutamide、Finasteride、40:1 Myo+D-chiro-Inositol；Spironolactone 劑量修正為 50–200 mg/day，註明健康女性不必例行驗 K+；Isotretinoin 補上 ≥220 mg/kg 新證據、維持治療策略、IBD/情緒平衡論述
  - **新增 2.6 PCOS 合併痤瘡診療框架**：Rotterdam 2003 / 2023 指南、Phenotype A–D、完整檢驗套組（OGTT/DHEAS/17-OHP/SHBG/FAI/Vit D/Lipid/TSH/Prolactin/AMH）、鑑別診斷（NCCAH/Cushing's/甲狀腺/泌乳素瘤/雄激素腫瘤/Acromegaly）、Ferriman–Gallwey + Ludwig 臨床工具、四階治療階梯、子宮內膜保護
  - **新增 2.7 痘疤分型治療**：Ice Pick / Rolling / Boxcar / Hypertrophic 四種疤型對應表、痘印 PIH vs PIE 分治
  - **新增劇本 D**：女性 PCOS 型荷爾蒙痤瘡專屬治療方案（三角醫療 + 四階段 + 長期維持 + 子宮內膜保護）
  - **擴充結語**：8 條 → 10 條關鍵原則
  - **補充參考文獻**：2023 International PCOS Guideline、Endocrine Society Hirsutism 2018、Thiboutot JAAD 2023、Plovanich JAMA Derm 2015、Blasiak 2013、Coloe 2011
- 總字數：31,793 → 45,421（擴增 43%）
- PDF 大小：1.14 MB → 1.34 MB

## [2026-04-24]
### Added
- **新竹東區關埔/光埔購屋決策研究 v3 PDF**(1.19 MB / 77,510 字)— v2 基礎上加入 6 張 SVG 示意圖,讓一般讀者更快抓到關鍵觀念:
  - **圖 1 · 公設比 → 得房率**(§3.4):橫條並列 28%~40% 下的 40 坪室內實際大小
  - **圖 2 · 關埔房價歷時 2010~2026**(§2.7):折線 + 關鍵事件標註(Costco/悅揚/2nm/平均地權/第 7 波限貸)
  - **圖 3 · 四大竹科通勤區相對位置**(§3.7):以竹科為錨點的區位示意 + 價格梯度
  - **圖 4 · 戶數甜蜜點曲線**(§4.1):U 型曲線標出 <100 戶 / 200~400(甜蜜點) / 800+ 三區,點出悅揚/潤隆/相對論實際位置
  - **圖 5 · 未來 5 年三劇本樹**(§4.5):決策樹樣式,左側當前 → 中層分叉條件 → 右側 2030 結果
  - **圖 6 · 新竹建商派系金字塔**(§3.2):T1/T2/T3 三層 + 光埔二期進場名單對照
- `reports/2026-04-acne-dehydrated-skincare/`：加入 6 張 SVG 示意圖輔助理解
  - **圖 1 粉刺演化鏈**（Ch 1.2）：7 階段病灶演化 + 皮膚剖面 + 對應治療強度
  - **圖 2 皮膚屏障磚牆模型**（Ch 1.3）：健康 vs 受損屏障並排對比，解釋外油內乾物理基礎
  - **圖 3 月經週期 × 荷爾蒙 × 下顎痘痘**（Ch 2.6.1）：雌激素/黃體素/雄激素比曲線 + 濾泡/黃體期分區 + 下顎痘嚴重度色條
  - **圖 4 四種痘疤剖面形態**（Ch 2.7）：Ice Pick / Rolling / Boxcar / Hypertrophic 4 型並列剖面 + 治療對應
  - **圖 5 複合型膚質正回饋閉環**（Ch 3.2）：8 節點環形圖 + 中央「打破閉環」說明（取代舊 ASCII 圖）
  - **圖 6 治療決策樹**（Ch 3.3）：IGA 0-4 分級 → 劇本 A/B/C + 女性週期性 diamond → 劇本 D + 3 月無效 → 鑑別診斷回診
### Fixed
- `scripts/md_to_pdf.py`：加入 SVG 區塊抽出 / 重插邏輯，避免被 `nl2br` 擴充破壞（SVG 換行會被轉成 `<br>`，shapes 無法渲染）。同時去除 markdown 自動包上的 `<p>…</p>` 外殼。此修正對所有後續含 SVG 的報告皆有效。
- PDF 大小：1.34 MB → 1.41 MB；總頁數擴至 41 頁

## [2026-04-24] (圖 5/6 流程圖修正)
### Fixed
- `reports/2026-04-acne-dehydrated-skincare/` 圖 5/6 流程圖渲染問題
  - **圖 5 閉環圖**：WeasyPrint 的 SVG `<marker>` 渲染太細幾乎看不到箭頭；改用顯式 polygon 箭頭，並加粗主線（1.6 → 2.2）。節點 6 標籤「色沉 · PIE」修正為「色沉 · 紅斑」（PIE 是紅斑，色沉是 PIH，兩者並列才正確）。
  - **圖 6 決策樹**：4 個主要問題全部修正：
    1. Root → 4 分支線原本無箭頭 → 加上顯式 polygon 箭頭
    2. IGA 0–1/2/3/4 標籤原本壓在分支線上 → 改用獨立色塊容器
    3. IGA 2/3/4 到 diamond 的虛線原本懸空 → 改為 L 形折線實連到 diamond 頂點
    4. 「3 個月無效」底部盒子原本完全斷開 → 加上橘色垂直連線 + 箭頭
  - 新增底部 takeaway 總結線

