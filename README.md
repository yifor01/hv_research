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
- `用戶資訊/` — 使用者長期持續性個人資料（profile + health），健康/個人類研究啟動前先讀
- `CHANGELOG.md` — 變更紀錄

## Reports 索引

研究分為 4 大類（詳見 `CLAUDE.md` §研究類別分類索引）：

### A. 一般主題研究（產品 / 技術 / 概念）

| 主題 | 路徑 | 備註 |
|---|---|---|
| Claude Code 工具深度解析 | [`reports/2026-04-claude-code/`](reports/2026-04-claude-code/) | 單版本 |
| 最新 Agentic AI 技術細節與實現方式 | [`reports/2026-04-agentic-ai-tech/`](reports/2026-04-agentic-ai-tech/) | v1 / v2 / v3 三版迭代 |
| Qwen3-VL 半導體領域適應 | [`reports/2026-04-vlm-domain-adaptation/`](reports/2026-04-vlm-domain-adaptation/) | 含 figures/ |
| Agent 長期記憶系統：框架對比、認知架構與選型決策 | [`reports/2026-04-agent-memory-systems/`](reports/2026-04-agent-memory-systems/) | v1（五大框架）+ v2（補 Long Context / Anthropic Memory tool / OpenAI Memory）+ v3（編排優化：30 秒選型卡 + 11 個選項抽象層級全景 SVG + §1-§10 本節結論；移除全文 v1/v2 inline 標註） |

### B. PI 盡職調查（人物盤點 / 候選人評估）

| 主題 | 路徑 | 備註 |
|---|---|---|
| 台灣半導體 AI 教授 Top N（TSMC 用） | [`reports/2026-04-tw-univ-semi-ai-professors/`](reports/2026-04-tw-univ-semi-ai-professors/) | v4.3-final + archive/process/planning 分層；Top 15 主名單 + 38 位備選 |

### C. 區域市場 / 決策等級（不動產 / 投資）

| 主題 | 路徑 | 備註 |
|---|---|---|
| 新竹東區關埔／光埔購屋分析 | [`reports/2026-04-hsinchu-east-guanpu-housing/`](reports/2026-04-hsinchu-east-guanpu-housing/) | v1 / v2（房仲盡調自審）/ v3（SVG 補圖） |

### D. 健康 / 個人領域（補品 / 飲食 / 美容 / 醫療）

| 主題 | 路徑 | 備註 |
|---|---|---|
| 痘痘肌外油內乾／粉刺內包痘調理 | [`reports/2026-04-acne-dehydrated-skincare/`](reports/2026-04-acne-dehydrated-skincare/) | 單版本 |
| Lean PCOS 與膠原蛋白補充 | [`reports/2026-04-lean-pcos-collagen/`](reports/2026-04-lean-pcos-collagen/) | v1 / v2（outcome 重定位） |
| 竹科工程師 PCOS 低 GI 飲食計畫 | [`reports/2026-04-tsmc-pcos-low-gi-diet/`](reports/2026-04-tsmc-pcos-low-gi-diet/) | 分檔 research_01~04 + 合併報告 |

> 命名與版本流程約定：A/B/C/D 各類專屬慣例見 `CLAUDE.md` §慣例。
