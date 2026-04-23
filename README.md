# hv-research

跨領域深度研究產出基地。以橫縱分析法（Horizontal-Vertical Analysis）對任何主題做系統性研究，產出排版精美的 PDF 研究報告。

## Skills

- [`hv-analysis`](~/.claude/skills/hv-analysis/) — 研究主力，產出 PDF
- [`khazix-writer`](~/.claude/skills/khazix-writer/) — 把研究成果改寫為公眾號長文（選配）

## Quick Start

```bash
# 1. 進入專案
cc hv-research

# 2. 跟 Claude 說
幫我用橫縱分析法深度研究 <主題>
```

詳細工作流程見 `CLAUDE.md`。

## Directory

- `reports/` — PDF 研究報告（hv-analysis / PI 盡職調查等）
- `articles/` — 公眾號文章版本
- `raw-materials/` — 研究前素材
- `scripts/` — 工具（含 `md_to_pdf.py`,支援 SVG 區塊保護、多 MD 合併、封面目錄、emoji → 樣式化標記）
- `templates/` — 跨題目復用的方法論 template（如 `pi-due-diligence-framework.md`）
- `CHANGELOG.md` — 變更紀錄
