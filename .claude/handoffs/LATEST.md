# Handoff — Phase 3 啟動（B template + C 候選池擴大） — 2026-04-22
Generated: 2026-04-22（深夜 Phase 2 結束後）
Branch: master（與 origin/master 同步）
Status: Phase 2 完成 + PDF 交付；Phase 3 有 2 個 agent 在背景跑

## 目標
為 TSMC AI 部門深化「長期合作學界 PI」決策基礎，補足 Phase 2 剩下的 2 個缺口：
- **方法論沉澱**（template）：把本次 5 維度 TSMC 視角盡職調查框架抽成可重用 template，未來換題目/換公司視角可直接套用
- **候選池擴大**（Top 7 單兵作戰的 2 個題目補人）：
  - 人員效率 RAG 只有蔡銘峰（Top 11）
  - CoWoS/封裝 AI 只有宋振銘（Top 8）

## Phase 2 結束狀態（已交付）

- `reports/2026-04-tw-univ-semi-ai-professors/TSMC_Top10_長期投資分析.pdf`（52 頁，955 KB，已進 git）
- 主管正在審查；Wave 1 接觸準備（Option A）**暫緩等主管圈選**
- Top 7：馬誠佑 8.9 / 胡璧合 8.7 / 銀慶剛 8.5 / 詹寶珠 8.3 / 李家岩 8.0 / 鄭桂忠 8.0 / 林嘉文 7.5
- 建議新增 Wave 1：王俊明 9.0（法務 check 後確認）

## Phase 3 進行中

### 🟡 [RUNNING] Batch A：LLM/RAG PI 候選（非蔡銘峰）
- 目標：找 2-3 位額外的 LLM / Agentic AI / RAG / IR PI 遷移到製程文件 RAG / 工程師助手
- Agent 條件：2023-2026 ACL/EMNLP/SIGIR/NeurIPS/ICLR 主會議 + 3+ 研究生 + 無 NVIDIA/Google/Meta 深度綁定
- 參考候選方向：NTU CSIE、NTHU 電機/資工、NYCU 資工、AS（已排除蔡銘峰 + 16 未入選 U1-U16）
- 產出：`phase3-batch-a-llm-rag-candidates.md`（5 維度評分 + Phase 2-lite profile 格式）

### 🟡 [RUNNING] Batch B：CoWoS/封裝 PI 候選（非宋振銘）
- 目標：找 2-3 位額外的材料 / 封裝 / Cu-Cu bonding / 3D IC / HBM PI
- Agent 條件：2023-2026 IEDM/ECTC/IMAPS/Nature 等封裝/材料頂會 + AI 遷移可行 + 5+ 研究生 + 無日月光/ASE/SPIL 深度獨占
- 參考候選方向：NTU 材料/機械/電機、NTHU 材料/工工、NYCU 材料、NCKU 工科/材料、NTUST、NCU 工科
- 產出：`phase3-batch-b-packaging-candidates.md`（5 維度評分 + Phase 2-lite profile 格式）

### 🔴 [PENDING] B：方法論 template
- 目標：把 5 維度 × 0-2 分 TSMC 視角盡職調查框架抽成 `templates/pi-due-diligence-framework.md`
- 內容：
  - 5 維度定義 + 評分錨點（什麼是 2 / 1.5 / 1 / 0.5 / 0）
  - 綁定折扣判斷樹（Director 級→扣多少；JDP→中性；SAT 同陣營→不扣；大廠 Chair→看額度）
  - Phase 1 篩選 → Phase 2 profile → Phase 3 TSMC 視角重評 標準流程
  - 換公司視角（非 TSMC）時維度 4 的重新定義模板
- 尚未開始；等 Batch A/B 結束後一併做，可把新候選人當作模板的驗證案例

## 未完成（Phase 2 繼承）

- [P1] 主管圈選 Wave 1 候選接觸 owner（**4 位**：馬誠佑 / 胡璧合 / 銀慶剛 / 王俊明）— **等主管**
- [P1] Wave 1 預算核准（1500-2500 萬台幣 / 5 年，+ 王俊明 300-500 萬）— **等主管**
- [P2] 法務確認：
  - (a) 銀慶剛 US12354122B2 與 NCKU 鄭芳田 IP 共有狀態
  - (b) 王俊明 TSMC 離職年數 + 商秘獎/專利綁定
- [P3] URL 可達性 check（phase2-top7-investment-analysis.md agent 產出 ref 有部分 placeholder）

## Git 狀態

- origin/master = b3c1d58
- 最近 commits：
  - b3c1d58 docs: 更新 CLAUDE.md — PDF 追蹤進 git
  - b62ed18 chore: 追蹤 PDF 產出（移除 *.pdf gitignore）
  - a34337f fix: md_to_pdf emoji 替換 + 表格窄欄斷字
  - d946623 chore: 新增 md_to_pdf 腳本
  - d188154 chore: handoff 更新 — 3 commit 完成 + 5 位重評併入 Top 12
  - 907f233 docs: TSMC 視角 Top 7 + 5 位重評
  - 737c58b docs: 16 未入選 AI 名人分析
  - af6761b docs: Phase 2 補完 profile + v2 三維度量化排序

## 下一步（下次 session 恢復時）

1. **確認 2 個背景 agent 結果**：
   ```bash
   ls reports/2026-04-tw-univ-semi-ai-professors/phase3-batch-*.md
   ```
   若產出成功 → 讀兩份報告 → 整合進 phase2-top7-investment-analysis.md §1.2（調整排名）或新開 `phase3-updated-ranking.md`
2. **寫 B：方法論 template** → `templates/pi-due-diligence-framework.md`
3. **產新 PDF**（如果 Batch A/B 帶出新 Top 10 或排序變動）：
   ```bash
   python3 scripts/md_to_pdf.py -o <out>.pdf --title "..." -- phase2-top7-investment-analysis.md phase3-batch-a*.md phase3-batch-b*.md phase2-tsmc-reeval-5pis.md
   ```
4. 主管回覆 Wave 1 圈選後，再做 Option A（Wave 1 接觸 briefing 包）

## Resume Prompt

「恢復 hv-research Phase 3。Phase 2 Top 10 PDF 已交主管審查。Phase 3 有 2 個背景 agent：Batch A 補 LLM/RAG PI 候選，Batch B 補 CoWoS/封裝 PI 候選。B（方法論 template）待做。確認 agent 產出後併入 Top 10 總表，並寫 template 沉澱。」
