# CLAUDE.md — hv-research

This file provides guidance to Claude Code when working in this project.

## 專案目的

跨領域深度研究產出基地。使用 `hv-analysis` skill（橫縱分析法）對任何主題做系統性研究並產出 PDF 研究報告；選擇性地用 `khazix-writer` skill 將研究成果改寫成公眾號長文。

**不限 AI 領域** — 產品、公司、概念、技術、人物、歷史事件、社會現象皆可。

## 目錄結構

```
hv-research/
├── reports/                    # hv-analysis / PI 盡職調查產出的 PDF
│   └── YYYY-MM-<topic>/        # 每份研究自成一個資料夾
│       ├── *.md                # Markdown 原稿（分檔 research_NN_*.md + 合併檔）
│       ├── *.pdf               # 最終 PDF（多版本時加 _vN 後綴）
│       ├── *.html              # weasyprint 中介產物（選擇性保留）
│       └── sources.md          # 引用資料來源清單
│   # 大型多版本研究（≥3 版本或 ≥30 檔）建議分層：
│   #   vX.Y-final/ + archive/{pdfs-old-versions,md-superseded}/ +
│   #   process/ + planning/ + README.md（索引）
│   # 案例：reports/2026-04-tw-univ-semi-ai-professors/
├── articles/                   # khazix-writer 產出的公眾號文章（目前未啟用）
├── raw-materials/              # 研究前蒐集的原始素材（PDF、截圖、筆記）
├── scripts/                    # PDF 生成等工具
│   └── md_to_pdf.py
├── templates/                  # 跨題目復用的方法論 template
│   ├── pi-due-diligence-framework.md
│   └── scoring-rubric-v2.md   # PI 盡職調查 5 維度評分標準
├── CHANGELOG.md                # 版本紀錄（每份研究交付後追加）
└── README.md
```

## 工作流程

### 新研究主題
1. 在 `raw-materials/YYYY-MM-<topic>/` 放入已蒐集的素材（若有）
2. 執行 `hv-analysis` skill：
   ```
   幫我用橫縱分析法深度研究 <topic>，重點：...
   補充素材：raw-materials/YYYY-MM-<topic>/ 下的檔案
   ```
3. skill 會自動產出 PDF，存進 `reports/YYYY-MM-<topic>/`

### 改寫為公眾號文章（選配）
1. 執行 `khazix-writer` skill：
   ```
   把 reports/YYYY-MM-<topic>/*.md 用卡茲克風格改寫成公眾號長文。
   原型：<五選一>
   我的第一手經歷/觀察：...
   ```
2. 輸出存進 `articles/YYYY-MM-<topic>.md`

### PI 盡職調查類研究（template 驅動）

對人物盤點類題目（例如「台灣半導體 AI 教授 Top N」），用 `templates/pi-due-diligence-framework.md`：

1. 廣度掃描候選池（agent 產初步名單，注意 ~30% 幻覺率 → WebFetch 核實姓名系所）
2. 每位候選產 profile（5 維度評分 + 隱形綁定檢查 + 代表實績）
3. 整合排名 + 主管 3 問防禦（題目互補 / 替代候選 / 為何沒選名人）
4. 交付：主名單 PDF（Top N 兩層結構）+ 備選 PDF（分類候選池）；**必附 Reference URL**
5. 能力限制聲明：WebSearch 無法驗證企業內部借調 / 顧問私約 / 未公開合作（見 lessons.md）

累積案例：`reports/2026-04-tw-univ-semi-ai-professors/`（TSMC Top 15 + 38 位備選）

### 區域市場 / 決策等級研究（新增類別）

不動產、消費市場、投資標的等「買賣決策」類題目，除 hv-analysis 縱橫結構外,建議多一層「**審視意見書回應版**」流程:

1. v1:照 hv-analysis 標準流程產出
2. v2:用「房仲盡調 / 投資盡調」標準自審或外請審，補上:
   - 租金投報率(Cap Rate) / 持有成本 / 稅負試算
   - 風險揭露(地質 / 淹水 / 嫌惡設施 / 耐震)
   - 平台均價差異解釋(樂居/591/實登差距的結構性原因)
   - 三劇本推演去除無依據機率數字,改定性排序
3. v3:加入 SVG 示意圖降低閱讀門檻(歷時折線、對比條、決策樹、金字塔)

累積案例:`reports/2026-04-hsinchu-east-guanpu-housing/`(關埔/光埔購屋 v1/v2/v3 + 6 張示意圖)

### 健康 / 個人領域研究（分檔結構）

與使用者個人健康/情境綁定的研究（如 PCOS 飲食、皮膚問題），建議採「分檔 research → 合併報告」結構：

1. `research_01_<sub-topic>.md` ~ `research_NN_<sub-topic>.md`：每章獨立深查（病史 / 比較 / 在地化）
2. 合併輸出：`<topic>_橫縱分析報告.md` + `.pdf`
3. 因素材高度個人化（年齡、地點、現有體質），素材放 `raw-materials/<topic>/`

案例：`reports/2026-04-tsmc-pcos-low-gi-diet/`（4 章 research + 合併報告）、`reports/2026-04-acne-dehydrated-skincare/`（含 6 張 SVG）

## 命名規則

- `<topic>`：英文小寫，連字號分隔（`claude-code`、`tsmc-2nm`、`ai-coding-agent`）
- 日期：ISO 8601（2026-04）
- PDF 檔名（三種常見格式）：
  - 標準：`<topic>_橫縱分析報告.pdf`（hv-analysis skill 預設）
  - 多版本：`<topic>_橫縱分析報告_vN.pdf`（v1/v2/v3 流程，如關埔購屋）
  - 自訂主題：`<自訂中文名>_v<X.Y>.pdf`（PI 盡調等大型研究，如 `TSMC_PI_彙整大表_v4.2.pdf`）

## 前置依賴

```bash
pip install weasyprint markdown --break-system-packages
```

## 慣例

- **每份研究獨立資料夾**，不要把多份研究的檔案混在同一層
- **素材溯源**：`sources.md` 記錄所有引用 URL + 訪問日期，方便日後驗證
- **PDF 產物連同 Markdown 原稿一併追蹤進 git**（方便遠端直接下載/分享給主管）；若單份 PDF > 50 MB 再個案討論
- **產 PDF 工具**：`scripts/md_to_pdf.py`（weasyprint + markdown），支援多 MD 合併、封面、目錄、emoji → 樣式化標記替換、**SVG 區塊保護**（抽出 → markdown 渲染 → 重插，避免 `nl2br` 破壞 shapes）
- **PDF 寬表格上限**：A4 頁寬下約 10-11 欄；超過會被切斷，改用「標籤列」或分段表
- **SVG 示意圖慣例**（抽象概念視覺化用）：
  - 直接在 Markdown 內嵌 `<svg viewBox="0 0 580 XXX" ...>`（寬度 580 剛好貼合 A4 頁寬扣除 margin）
  - **圖片編號依章節先後順序排列**，不是設計順序（讀者看圖 1 在 §2 比圖 2 在 §3 自然）
  - **箭頭/對比色必須與底色反差足夠**（深藍底 + 灰色箭頭 = 看不見；改用亮黃 #f1c40f 或白色）
  - 箭頭終點需落在目標形狀 **外緣**；若進入填色區會被同色遮蔽
  - **多邊形寬度需容納最長中文字串**：頂部梯形 / 徽章若有 10+ 字的名單，頂寬 ≥ 180px；否則會被 clip
  - WeasyPrint 的 `<marker>` 渲染纖細，重要箭頭建議改用顯式 `<polygon>` 箭頭頭(見 acne 報告圖 5/6 修正)
  - **WeasyPrint 不支援 `font:` CSS shorthand**（只認 `font-weight + font-size + font-family` 顯式三屬性，否則粗體標題消失）— 見 agentic AI v2 教訓
  - **內嵌 pill 寬度 ≥ 文字寬 + 12-15px buffer**：text-anchor 為 middle 時，pill 寬若小於文字寬，文字會視覺溢出 pill 邊界（agentic v3 `auto re-plan` 56→70px 修正）
  - **WeasyPrint SVG `break-inside: avoid` 支援不完整**：viewBox 高度 ≥ 280px 的 SVG 若放在頁面下半仍會被切跨頁。穩定解法：(a) 在 SVG 標題前手動加 `<div style="page-break-before: always; height: 0;"></div>` 強制圖從新頁頂部開始；(b) 同時壓縮 viewBox 高度 ≤ 280px。兩條都做才穩定（lean-pcos-collagen 報告圖 1 修正案）
  - **右側標籤超出 SVG width 會被裁切**：寬度 580 的 SVG，從 x=360 起的長中文字串易超界；改用 `text-anchor: end` 配 x=560 從右算起
  - 累積案例：關埔購屋研究(6 張)、痘痘肌報告(6 張)、Agentic AI 報告(10 張，v3 補圖版)
- **主管報告必附 Reference URL**：Due diligence 類交付，每位 PI 至少 2-3 個公開連結（學校頁 / Scholar / Lab）
- **Companion PDF 結構要跟主 PDF 一致**：同 session 出多份 PDF 時，結構對齊降低閱讀成本
- **跨領域學習**：研究過程中遇到的方法論心得寫進 `~/vault/projects/hv-research/lessons.md`
- **大型研究多版本清理**：研究歷經 ≥3 版本或 ≥30 檔案時，用 `git mv` 重組為 `vX-final/ + archive/{pdfs-old-versions,md-superseded}/ + process/ + planning/ + README.md` 分層；舊 PDF 搬移不刪除（保留版本對比能力）
- **CHANGELOG.md 維護**：每次研究交付（PDF push）或重大改版（如 v4.0 → v4.2），於 root `CHANGELOG.md` 追加 `## [YYYY-MM-DD]` 條目，依 Added/Changed/Fixed 分類
