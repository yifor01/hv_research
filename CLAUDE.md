# CLAUDE.md — hv-research

This file provides guidance to Claude Code when working in this project.

## 專案目的

跨領域深度研究產出基地。使用 `hv-analysis` skill（橫縱分析法）對任何主題做系統性研究並產出 PDF 研究報告；選擇性地用 `khazix-writer` skill 將研究成果改寫成公眾號長文。

**不限 AI 領域** — 產品、公司、概念、技術、人物、歷史事件、社會現象皆可。

## 目錄結構

```
hv-research/
├── reports/                    # hv-analysis 產出的 PDF 研究報告
│   └── YYYY-MM-<topic>/        # 每份研究自成一個資料夾
│       ├── *.md                # Markdown 原稿
│       ├── *.pdf               # 最終 PDF
│       └── sources.md          # 引用資料來源清單
├── articles/                   # khazix-writer 產出的公眾號文章
│   └── YYYY-MM-<topic>.md
├── raw-materials/              # 研究前蒐集的原始素材（PDF、截圖、筆記）
│   └── YYYY-MM-<topic>/
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

## 命名規則

- `<topic>`：英文小寫，連字號分隔（`claude-code`、`tsmc-2nm`、`ai-coding-agent`）
- 日期：ISO 8601（2026-04）
- PDF 檔名：`<topic>_橫縱分析報告.pdf`（skill 預設格式）

## 前置依賴

```bash
pip install weasyprint markdown --break-system-packages
```

## 慣例

- **每份研究獨立資料夾**，不要把多份研究的檔案混在同一層
- **素材溯源**：`sources.md` 記錄所有引用 URL + 訪問日期，方便日後驗證
- **PDF 產物連同 Markdown 原稿一併追蹤進 git**（方便遠端直接下載/分享給主管）；若單份 PDF > 50 MB 再個案討論
- **產 PDF 工具**：`scripts/md_to_pdf.py`（weasyprint + markdown），支援多 MD 合併、封面、目錄、emoji → 樣式化標記替換
- **跨領域學習**：研究過程中遇到的方法論心得寫進 `~/vault/projects/hv-research/lessons.md`
