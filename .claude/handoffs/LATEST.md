# Handoff — hv-research Setup — 2026-04-20

## Goal
建立跨領域深度研究產出基地，並準備跑第一份研究（Claude Code 最新資訊與原理）。

## Current State
- ✅ `~/projects/hv-research/` 目錄完整（reports / articles / raw-materials + CLAUDE.md + README.md + .gitignore）
- ✅ git repo init，首 commit `de6b22e`
- ✅ `~/vault/projects/hv-research/` 追蹤檔完成（status.md + lessons.md）
- ✅ vault sync 已跑，`~/vault/CLAUDE.md` Active Projects 清單含 `hv-research`
- ✅ 兩個 skill 已安裝並轉繁體：
  - `~/.claude/skills/hv-analysis/`
  - `~/.claude/skills/khazix-writer/`
- ⏳ 第一份研究尚未跑

## Key Decisions Made
- **專案命名**：`hv-research`（呼應 hv-analysis skill），不侷限 AI 領域
- **目錄分層**：`reports/`（PDF） + `articles/`（khazix-writer 產出）+ `raw-materials/`（原始素材），每份研究一個 `YYYY-MM-<topic>/` 子資料夾
- **git 排除**：PDF / HTML / raw-materials 不進 git，Markdown 原稿要追蹤
- **skill 繁化策略**：opencc s2twp + 客製字典，中國平台專有名詞（公眾號、微信、小紅書）保留

## Files Modified
- `~/projects/hv-research/`（新建）：CLAUDE.md、README.md、.gitignore、三個空資料夾
- `~/vault/projects/hv-research/`（新建）：status.md、lessons.md
- `~/vault/CLAUDE.md`、`~/vault/README.md`（vault sync 自動更新）
- `~/.claude/skills/hv-analysis/`、`~/.claude/skills/khazix-writer/`（新裝並繁化）

## Blockers / Issues
- (none)

## Next Steps
1. **下一個 session**：`cc hv-research` 進到專案目錄
2. **第一次依賴**：`pip install weasyprint markdown --break-system-packages`
3. **跑第一份研究**（完整 prompt）：
   ```
   幫我用橫縱分析法深度研究 Claude Code，重點放在：
   - 縱向：從 2024 年發布到現在的版本演進、重大功能里程碑
     （MCP、hooks、skills、plugins、sub-agents、Claude Agent SDK 等）
   - 橫向：與 Cursor / Cline / Aider / Codex CLI / Gemini CLI 的差異
   - 原理：架構（Ink/React TUI、tool use loop、context 管理、
     permission system）、設計哲學（terminal-native、thin wrapper）

   補充素材：我本機 ~/projects/claude-code-sourcemap_v2.1.88/ 有一份
   v2.1.88 的逆向分析（15 章 + 38 SVG），研究「原理」章節時優先
   引用這份，避免只靠聯網搜尋。

   輸出資料夾：reports/2026-04-claude-code/
   ```
4. 預計產出：`reports/2026-04-claude-code/*.pdf`
5. 選配：跑 `khazix-writer` 改寫為公眾號長文到 `articles/2026-04-claude-code.md`

## Verification
新 session 進去後檢查：
```bash
ls ~/.claude/skills/hv-analysis ~/.claude/skills/khazix-writer  # 兩個 skill 存在
cat ~/projects/hv-research/CLAUDE.md  # 工作流程
```
