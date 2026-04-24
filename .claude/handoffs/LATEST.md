# Handoff: TSMC Top 15 v3.4 + Backup v1.4 — Phase 4 補強重排（3 進 3 出）
Generated: 2026-04-24 17:00 Asia/Taipei
Branch: master
Status: Ready for Review（等主管圈選第一波 8 位 + 鄭芳田顧問）
Progress: 100% — 兩份 PDF 已重出，文件全部同步

## 目標
回應主管 18 位「為何沒選」追問清單。Phase 4 啟動 14 位新 profile（10 完整 + 5 mini）+ 嚴格按分排序原則 3 進 3 出 Top 15。產出 v3.4 主名單 + v1.4 備選 兩份新 PDF + 4 條新 lessons + template v1.1。

## 已完成（本 session 迭代）
- [x] 5 個 research agent 並行盡調 14 位 PI（NCKU IYM 三人組、NTHU IEEM 兩位、NTU 補位兩位、技職 4 位、類別 B 五位）
- [x] 嚴格按分排序原則 3 進 3 出（江蕙如/陳亮嘉/謝昱銘 進；林嘉文/蔡銘峰/黃瀚萱 退）
- [x] Top 15 v3.4 重排（13 欄含建議合作方式 + ⭐ 標記新進）
- [x] 教授檔案 1-8 / 9-15 重組（江蕙如、陳亮嘉、謝昱銘 完整 profile section；林嘉文/蔡銘峰/黃瀚萱 移走）
- [x] 主管摘要更新（第一波 6 → 8 位 + NCKU IYM 學派叢一次串聯）
- [x] 附錄更新（接觸策略 / 預算 5 年 7300-11600 萬 / 法務 IYM 三人組 / Phase 4 補強說明 §F + Reference URL §G）
- [x] Backup v1.4 擴增（38 → 55 位；§1B Phase 4 17 位大表 + §2B 個別內容 + §4 補強說明）
- [x] Top 15 v3.4 PDF 產出（832 KB）
- [x] Backup v1.4 PDF 產出（1017 KB）
- [x] CHANGELOG / vault lessons.md +4 條 / template v1.1（§8 防漏 checklist）
- [x] 主管校準原則：「**不因主管點到名而上推**」嚴格遵守

## 未完成
- [ ] [P1] 主管圈選第一波 8 位（王俊明/江蕙如/馬誠佑/陳亮嘉/胡璧合/陳冠能/銀慶剛/謝昱銘）+ 鄭芳田顧問費批准
- [ ] [P2] 法務 check NCKU IYM 學派叢三人組（銀慶剛 + 謝昱銘 + 鄭芳田顧問）：US12354122B2 IP 共有狀態（影響三人合作範圍）
- [ ] [P2] 張國浩 (Backup A+1) Powerchip 排擠 + Micron Chair 釐清；若無誤可遞補 Top 15 替換蔡佩璇
- [ ] [P3] 陳亮嘉 Reference URL 補完（NTU 機械系教師頁、SPIE Profile、2022 NSTC 未來科技獎公告）
- [ ] [P3] 謝昱銘 Lab 規模獨立性核實（業界 visibility 偏低需 TSMC 主動 due diligence）

## 失敗的方法（不要重複）
- **agent 給分不可全信**：陳亮嘉 agent 報 10/10、江蕙如 agent 報 9.0、謝昱銘 agent 報 8.5 — 校準後 8.9 / 9.0 / 8.3。校準原則：年齡未確認 / Lab 規模未明應扣 0.2-1.0
- **誘惑：4 進 4 出**（張國浩 7.8 vs 蔡佩璇 7.7 邊際 0.1 差）— 改為 3 進 3 出，張國浩列首選遞補。理由：張有 🟡 待釐清，蔡 Fulbright 即將回國
- **誘惑：因主管點到名而加分**（用戶明確要求不要這樣做）— 嚴格按分排序執行

## 關鍵決策
- **嚴格按分排序，不因主管點到名而上推 Top 15**（用戶原話：「不用因為點出來而特意上升到 top15，依評分 & 排序原則來排」）
- **3 進 3 出而非 4 進 4 出**：邊際 0.1 差用「綁定風險」打破平局
- **鄭芳田列「戰略顧問特殊類」而非主名單**：72 歲已退休，5 年回收期不足，但戰略價值大（IYM 系統創始人 + TSMC 終生合作對象）
- **NCKU IYM 學派叢一次串聯**：銀慶剛（Top 15 #7）+ 謝昱銘（Top 15 #9 ⭐）+ 鄭芳田（戰略顧問 100-200 萬/年）= 跨校學派合作（共 1500-2500 萬 / 5 年）
- **RAG 軸退場到 Backup A 類**：蔡銘峰、黃瀚萱配套退場；保留 RAG 軸隨時遞補
- **林嘉文光刻 EDA 退場**：被陳亮嘉「立即可用 + AOIEC 聯盟 43 家」的優先度取代；可遞補
- **陳亮嘉補完 T0 製程量測軸**：原 Top 15 零覆蓋，OCD/HAR TSV/AI metrology 全套
- **江蕙如補張耀文 EDA 空缺**：張耀文 2024-05 MediaTek 獨董失效後 EDA 軌道唯一無縫接棒人選

## 程式碼上下文

**PDF 生成命令**:
```bash
# Top 15 v3.4
python3 scripts/md_to_pdf.py \
  reports/2026-04-tw-univ-semi-ai-professors/TSMC_Top15_v3_00_封面與摘要.md \
  reports/2026-04-tw-univ-semi-ai-professors/TSMC_Top15_v3_01_大表.md \
  reports/2026-04-tw-univ-semi-ai-professors/TSMC_Top15_v3_02_教授檔案_1-8.md \
  reports/2026-04-tw-univ-semi-ai-professors/TSMC_Top15_v3_03_教授檔案_9-15.md \
  reports/2026-04-tw-univ-semi-ai-professors/TSMC_Top15_v3_05_附錄.md \
  --title "TSMC × 台灣學界 PI 長期投資分析 v3.4" \
  --subtitle "Top 15 主名單 — Phase 4 補強重排版（3 進 3 出，新增 NCKU IYM 學派叢 + AI-EDA + 製程量測軸）" \
  --author "盡職調查團隊" \
  --section-titles ... \
  --section-descs ... \
  -o reports/2026-04-tw-univ-semi-ai-professors/TSMC_Top15_長期投資分析_v3.4.pdf

# Backup v1.4
python3 scripts/md_to_pdf.py \
  reports/2026-04-tw-univ-semi-ai-professors/TSMC_Backup_v1_00_封面與說明.md \
  reports/2026-04-tw-univ-semi-ai-professors/TSMC_Backup_v1_01_統一大表.md \
  reports/2026-04-tw-univ-semi-ai-professors/TSMC_Backup_v1_02_個別內容.md \
  reports/2026-04-tw-univ-semi-ai-professors/TSMC_Backup_v1_03_附錄.md \
  -o reports/2026-04-tw-univ-semi-ai-professors/TSMC_Backup_備選候選名單_v1.4.pdf
```

**Top 15 v3.4 排序**:
```
1.  王俊明 9.0       | 1. 江蕙如 ⭐ 9.0
3.  馬誠佑 8.9       | 3. 陳亮嘉 ⭐ 8.9
5.  胡璧合 8.8       | 5. 陳冠能 8.8
7.  銀慶剛 8.5
8.  陳智 8.4
9.  詹寶珠 8.3       | 9. 謝昱銘 ⭐ 8.3
11. 江國寧 8.1
12. 宋振銘 8.0       | 12. 李家岩 8.0       | 12. 鄭桂忠 8.0
15. 蔡佩璇 7.7
```

**Backup v1.4 結構**: 55 位 = v1.0 38 位 (5 類: A 4 + B 6 + C 3 + D 20 + E 5) + Phase 4 14 位 (A+ 7 + B 2 + B' 1 + C 3) + Top 15 退場 3 位 (進 A 類 → A5/A6/A7) + 鄭芳田特殊類 1 位

## 下一步（可直接執行）
1. **等主管圈選第一波 8 位 + 鄭芳田顧問**（每位 3-5 KB briefing 包，含合作題目 × 預算 × KPI × Email 模板）
2. **法務 NCKU IYM 三人組 IP check**：銀慶剛 + 謝昱銘 + 鄭芳田顧問均涉 US12354122B2 共有狀態
3. **張國浩 Backup 遞補釐清**：Powerchip 排擠 + Micron Chair 兩項；若無誤可換蔡佩璇

## 需要載入的檔案（恢復時）
- `.claude/handoffs/LATEST.md`（本檔副本）
- `reports/2026-04-tw-univ-semi-ai-professors/TSMC_Top15_長期投資分析_v3.4.pdf`（主交付，832 KB）
- `reports/2026-04-tw-univ-semi-ai-professors/TSMC_Backup_備選候選名單_v1.4.pdf`（備選交付，1017 KB）
- `reports/2026-04-tw-univ-semi-ai-professors/phase4-补强說明.md`（補強動機與決策原則）
- `reports/2026-04-tw-univ-semi-ai-professors/phase4-profile-*.md`（10 份完整 profile）
- `reports/2026-04-tw-univ-semi-ai-professors/phase4-mini-*.md`（5 份 mini profile）
- `templates/pi-due-diligence-framework.md` v1.1（含 §8 Phase 4 防漏 checklist）
- `~/vault/projects/hv-research/lessons.md`（14 條 lessons，本 session 新增 4 條）

## Resume Prompt
恢復 hv-research：TSMC Top 15 v3.4（3 進 3 出 + 832 KB）+ Backup v1.4（55 位 + 1017 KB）已重出 push 到 master；等主管圈選第一波 8 位 + 鄭芳田顧問；下一步法務 NCKU IYM 三人組 IP check + 張國浩 Powerchip/Micron Chair 釐清。
