#!/usr/bin/env python3
"""Generate figures for the Qwen3.6/Qwen3-VL semiconductor domain adaptation report v2."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Circle, Polygon
from matplotlib.lines import Line2D
import numpy as np
from pathlib import Path

# CJK font
plt.rcParams["font.sans-serif"] = ["Noto Sans CJK JP", "Noto Sans CJK SC", "Noto Sans CJK TC", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["savefig.dpi"] = 160
plt.rcParams["savefig.bbox"] = "tight"
plt.rcParams["savefig.facecolor"] = "white"

OUT = Path(__file__).parent

# Color palette
C_BLUE = "#1a5276"
C_GREEN = "#1e8449"
C_LIGHTBLUE = "#2e86c1"
C_PURPLE = "#5b2c6f"
C_ORANGE = "#d68910"
C_RED = "#c0392b"
C_GRAY = "#566573"
C_BG = "#f4f6f6"
C_BG2 = "#ebf5fb"
C_BG3 = "#fdf2e9"


def box(ax, x, y, w, h, text, fc=C_BG, ec=C_BLUE, fontsize=9, weight="normal", color="black"):
    b = FancyBboxPatch((x, y), w, h,
                       boxstyle="round,pad=0.02,rounding_size=0.08",
                       linewidth=1.4, facecolor=fc, edgecolor=ec)
    ax.add_patch(b)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            fontsize=fontsize, fontweight=weight, color=color, wrap=True)


def arrow(ax, x1, y1, x2, y2, color=C_GRAY, style="->", lw=1.4, mutation=15):
    a = FancyArrowPatch((x1, y1), (x2, y2),
                        arrowstyle=style, color=color, linewidth=lw,
                        mutation_scale=mutation)
    ax.add_patch(a)


# ============================================================
# Figure 1 — 橫縱分析法示意圖
# ============================================================
def fig1_hv_method():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.set_aspect("equal")
    ax.axis("off")

    # 縱軸
    ax.annotate("", xy=(5, 5.6), xytext=(5, 0.4),
                arrowprops=dict(arrowstyle="->", lw=2.5, color=C_BLUE))
    ax.text(5.15, 5.6, "縱軸\n(時間)", fontsize=11, color=C_BLUE, fontweight="bold")
    ax.text(4.85, 0.2, "2018", fontsize=9, color=C_BLUE, ha="right")
    ax.text(4.85, 5.4, "2026", fontsize=9, color=C_BLUE, ha="right")

    # 橫軸
    ax.annotate("", xy=(9.6, 3), xytext=(0.4, 3),
                arrowprops=dict(arrowstyle="->", lw=2.5, color=C_GREEN))
    ax.text(9.6, 3.15, "橫軸\n(當下競爭)", fontsize=11, color=C_GREEN, fontweight="bold")

    # 縱向時間節點
    for y, label in [(0.8, "ULMFiT 2018"), (1.6, "LLaMA 2023"),
                     (2.5, "Qwen2-VL 2024"), (3.6, "Qwen3-VL 2025"),
                     (4.6, "Qwen3.6 2026")]:
        ax.plot(5, y, "o", color=C_BLUE, markersize=9, zorder=5)
        ax.text(5.25, y, label, fontsize=9, va="center", color=C_BLUE)

    # 橫向競品
    for x, label in [(1, "LLaVA"), (2.5, "InternVL"),
                     (7, "Pixtral"), (8.5, "Molmo")]:
        ax.plot(x, 3, "s", color=C_GREEN, markersize=9, zorder=5)
        ax.text(x, 2.7, label, fontsize=9, ha="center", color=C_GREEN)

    # 交匯點
    ax.plot(5, 3, "*", color=C_RED, markersize=26, zorder=6)
    ax.annotate("交匯洞察\n(判斷 / 決策)", xy=(5, 3), xytext=(7, 4.5),
                fontsize=11, fontweight="bold", color=C_RED,
                arrowprops=dict(arrowstyle="->", color=C_RED, lw=1.5),
                ha="center")

    ax.set_title("橫縱分析法：縱軸追時間深度，橫軸追同期廣度，交匯出判斷",
                 fontsize=13, fontweight="bold", pad=10)

    plt.savefig(OUT / "01_hv_method.png")
    plt.close()


# ============================================================
# Figure 2 — 四階段 Pipeline 流程圖
# ============================================================
def fig2_four_stage_pipeline():
    fig, ax = plt.subplots(figsize=(15, 7.5))
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 7.5)
    ax.set_aspect("equal")
    ax.axis("off")

    stages = [
        (0.3, "Base VLM\n(Qwen3.6-27B /\nQwen3-VL-32B)", C_BG2, C_BLUE),
        (3.1, "Stage 1: CPT\n持續預訓練\n(domain corpus)", C_BG3, C_ORANGE),
        (5.9, "Stage 2: SFT\n指令微調\n(domain pair)", C_BG3, C_ORANGE),
        (8.7, "Stage 3: Alignment\nMPO / V-DPO / GRPO\n(preference / reward)", C_BG3, C_ORANGE),
        (11.5, "Stage 4: Agent SFT\nTool / GUI\n(trajectory)", C_BG3, C_ORANGE),
    ]

    for x, text, fc, ec in stages:
        box(ax, x, 3.8, 2.5, 1.9, text, fc=fc, ec=ec, fontsize=9.5, weight="bold")

    # arrows between stages
    for i in range(len(stages) - 1):
        arrow(ax, stages[i][0] + 2.5, 4.75, stages[i + 1][0], 4.75,
              color=C_GRAY, lw=2.2, mutation=20)

    # output arrow from Stage 4 up to Domain VLM box on top-right
    box(ax, 11.5, 6.15, 2.5, 0.55,
        "✓ 半導體 Domain VLM", fc="#d5f5e3", ec=C_GREEN,
        fontsize=10, weight="bold", color=C_GREEN)
    arrow(ax, 12.75, 5.7, 12.75, 6.15, color=C_GREEN, lw=2.5, mutation=22)

    # input data boxes (below stages)
    data_labels = [
        (3.1, "SemiKong 525.6M\n+ 內部 FAR/SOP\n+ SEM caption"),
        (5.9, "SemiKong 50K\n+ 內部指令\n+ SEM/wafer QA"),
        (8.7, "Preference pair\n+ Verifier\n(DRC/規則)"),
        (11.5, "MES API\n+ EDA CLI\n+ GUI trajectory"),
    ]
    for x, text in data_labels:
        box(ax, x, 1.2, 2.5, 1.6, text, fc="#fef9e7", ec=C_ORANGE,
            fontsize=8.5, color=C_GRAY)
        arrow(ax, x + 1.25, 2.8, x + 1.25, 3.8, color=C_ORANGE,
              lw=1.5, mutation=15, style="->")

    # input data section label
    ax.text(1.5, 2, "↓ 資料\n輸入", ha="center", va="center", fontsize=9.5,
            color=C_ORANGE, weight="bold", style="italic")

    ax.text(7.5, 6.95, "四階段 Pipeline 總覽：從通用 VLM 到半導體領域模型",
            fontsize=13, fontweight="bold", ha="center", color=C_BLUE)

    plt.savefig(OUT / "02_four_stage_pipeline.png")
    plt.close()


# ============================================================
# Figure 3 — 七年演化時間軸
# ============================================================
def fig3_seven_year_timeline():
    fig, ax = plt.subplots(figsize=(14, 7))

    events = [
        ("2018-01", "ULMFiT\n三階段 FT", "LLM", C_PURPLE),
        ("2019", "BioBERT /\nSciBERT", "LLM", C_PURPLE),
        ("2020-04", "DAPT/TAPT", "LLM", C_PURPLE),
        ("2021-06", "LoRA", "PEFT", C_ORANGE),
        ("2022-03", "InstructGPT\n三階段正式化", "LLM", C_PURPLE),
        ("2023-02", "LLaMA\n開源基底", "LLM", C_PURPLE),
        ("2023-04", "LLaVA\nMLP projection", "VLM", C_BLUE),
        ("2023-05", "QLoRA", "PEFT", C_ORANGE),
        ("2023-05", "DPO", "Align", C_RED),
        ("2023-08", "Qwen-VL", "VLM", C_BLUE),
        ("2024-02", "GRPO\nDoRA\nKTO", "Align/PEFT", C_RED),
        ("2024-05", "SimPO\nLoRA Learns Less", "Align", C_RED),
        ("2024-08", "Qwen2-VL\nNative Dynamic Res", "VLM", C_BLUE),
        ("2024-11", "SemiKong\nMPO", "Domain/Align", C_GREEN),
        ("2025-01", "Qwen2.5-VL\nUI-TARS", "VLM/Agent", C_BLUE),
        ("2025-09", "Qwen3-VL\n全家族", "VLM", C_BLUE),
        ("2026-04-22", "Qwen3.6-27B\nVL 併回主線", "VLM", C_BLUE),
    ]

    # timeline
    ax.axhline(y=0, color=C_GRAY, lw=2, zorder=1)

    # x positions (evenly distributed for readability)
    n = len(events)
    xs = np.linspace(0.5, 13.5, n)

    for i, ((date, label, cat, color), x) in enumerate(zip(events, xs)):
        # alternate above / below
        y_text = 0.7 if i % 2 == 0 else -0.7
        y_label = 1.3 if i % 2 == 0 else -1.3
        va = "bottom" if i % 2 == 0 else "top"

        # stem line
        ax.plot([x, x], [0, y_text], color=color, lw=1.3, zorder=2)
        # marker
        ax.plot(x, 0, "o", color=color, markersize=10, zorder=3,
                markeredgecolor="white", markeredgewidth=1.5)
        # label
        ax.text(x, y_label, label, ha="center", va=va, fontsize=8.5,
                color=color, fontweight="bold", zorder=4)
        # date
        ax.text(x, y_text + (0.15 if i % 2 == 0 else -0.15), date,
                ha="center", va=va, fontsize=7.5, color=C_GRAY, style="italic")

    # legend
    cats = [("LLM 基礎", C_PURPLE), ("VLM 架構", C_BLUE), ("對齊演化", C_RED),
            ("PEFT", C_ORANGE), ("Domain / 其他", C_GREEN)]
    handles = [Line2D([0], [0], marker="o", color="w", markerfacecolor=c, markersize=10, label=l)
               for l, c in cats]
    ax.legend(handles=handles, loc="upper left", bbox_to_anchor=(0.005, 0.995), fontsize=9, framealpha=0.95)

    ax.set_xlim(0, 14)
    ax.set_ylim(-3.5, 3.5)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_title("VLM Domain Adaptation 四階段 Pipeline 七年演化時間軸（2018–2026）",
                 fontsize=13, fontweight="bold", pad=15)

    plt.savefig(OUT / "03_seven_year_timeline.png")
    plt.close()


# ============================================================
# Figure 4 — 偏好對齊演化譜系樹
# ============================================================
def fig4_alignment_tree():
    fig, ax = plt.subplots(figsize=(13, 9))
    ax.set_xlim(0, 13)
    ax.set_ylim(-1, 8)
    ax.set_aspect("equal")
    ax.axis("off")

    # root: RLHF-PPO
    box(ax, 5, 6.7, 3, 0.8, "RLHF-PPO (2022-03)\nInstructGPT — 4 模型同顯存，超難訓",
        fc="#fadbd8", ec=C_RED, fontsize=9, weight="bold")

    # level 2: DPO (central breakthrough)
    box(ax, 5, 4.8, 3, 0.8, "DPO (2023-05)\n閉式解，2 模型即可，<100 行代碼",
        fc="#d6eaf8", ec=C_BLUE, fontsize=9, weight="bold")
    arrow(ax, 6.5, 6.7, 6.5, 5.6, color=C_GRAY, lw=1.8)
    ax.text(6.7, 6.2, "消掉\nRM", fontsize=8, color=C_GRAY, style="italic")

    # level 3: DPO variants (left block — 4 boxes in 2x2 grid to save horizontal space)
    variants_l = [
        (0.3, 3.0, "IPO (2023-10)\nDPO 正則化", C_BG2, C_BLUE),
        (3.2, 3.0, "KTO (2024-02)\n二元訊號\n不要 pair", C_BG2, C_BLUE),
        (6.1, 3.0, "ORPO (2024-03)\nSFT+對齊合併", C_BG2, C_BLUE),
        (0.3, 1.6, "SimPO (2024-05)\n去 ref model", C_BG2, C_BLUE),
    ]
    for x, y, t, fc, ec in variants_l:
        box(ax, x, y, 2.6, 0.95, t, fc=fc, ec=ec, fontsize=8.5)

    # Clean orthogonal arrows for DPO variants
    # Down from DPO (base is 6.5, 4.8)
    ax.plot([6.5, 6.5], [4.8, 4.45], color=C_GRAY, lw=1.2)
    # Horizontal line connecting the three top boxes (x centers: 1.6, 4.5, 7.4)
    ax.plot([1.6, 7.4], [4.45, 4.45], color=C_GRAY, lw=1.2)
    # Arrows to the three top boxes
    for x_center in [1.6, 4.5, 7.4]:
        arrow(ax, x_center, 4.45, x_center, 3.95, color=C_GRAY, lw=1.2)
    # Arrow to SimPO from IPO (IPO bottom is 1.6, 3.0, SimPO top is 1.6, 2.55)
    arrow(ax, 1.6, 3.0, 1.6, 2.55, color=C_GRAY, lw=1.2)

    # level 3: parallel line - GRPO (right side, clear separation)
    box(ax, 9.5, 4.8, 3.2, 0.8, "GRPO (2024-02)\n去 critic + verifiable reward",
        fc="#d5f5e3", ec=C_GREEN, fontsize=9, weight="bold")
    arrow(ax, 8, 6.9, 9.5, 5.6, color=C_GREEN, lw=1.8, style="->")
    ax.text(8.7, 6.3, "並行線\n消掉 critic", fontsize=8, color=C_GREEN, style="italic", ha="center")

    # GRPO descendants (right side, below)
    box(ax, 9.5, 3.0, 3.2, 0.95,
        "DAPO / DrGRPO / GSPO\nFaithful GRPO\n(inconsistency 24.5%→1.7%)",
        fc="#d5f5e3", ec=C_GREEN, fontsize=8)
    arrow(ax, 11.1, 4.8, 11.1, 3.95, color=C_GREEN, lw=1.2)

    # level 4: VLM-specific (bottom row)
    box(ax, 3.2, 0.1, 2.6, 1.2, "MPO (2024-11)\nDPO+BCO+SFT\nVLM 業界預設",
        fc="#fdebd0", ec=C_ORANGE, fontsize=8.5, weight="bold")
    arrow(ax, 4.5, 3.0, 4.5, 1.3, color=C_ORANGE, lw=1.3)

    box(ax, 6.1, 0.1, 2.6, 1.2, "OPA-DPO (CVPR'25)\nOn-policy\n4.8K > 16K",
        fc="#fdebd0", ec=C_ORANGE, fontsize=8.5, weight="bold")
    arrow(ax, 7.4, 3.0, 7.4, 1.3, color=C_ORANGE, lw=1.3, style="->")

    # bottom caption (below all boxes)
    ax.text(6.5, -0.7, "紅=起點（重工業） ｜ 藍=DPO 譜系 ｜ 綠=GRPO/RLVR 譜系 ｜ 橘=VLM 專用改良",
            ha="center", fontsize=9.5, color=C_GRAY, style="italic")
    ax.set_title("偏好對齊方法演化譜系樹（2022–2025）",
                 fontsize=13, fontweight="bold", pad=15)

    plt.savefig(OUT / "04_alignment_tree.png")
    plt.close()


# ============================================================
# Figure 5 — LoRA / DoRA / PiSSA 原理對比
# ============================================================
def fig5_lora_variants():
    fig, axes = plt.subplots(1, 3, figsize=(15, 5.5))

    # LoRA
    ax = axes[0]
    ax.set_xlim(0, 5); ax.set_ylim(0, 5); ax.set_aspect("equal"); ax.axis("off")
    # Titles (use ax.text with clear positioning, not set_title)
    ax.text(2.5, 4.6, "LoRA (2021)", ha="center", fontsize=12, weight="bold", color=C_BLUE)
    ax.text(2.5, 4.2, "低秩分解，只訓 A, B", ha="center", fontsize=10, color=C_BLUE)
    # W
    ax.add_patch(Rectangle((0.5, 2), 1.2, 1.2, facecolor="#d6eaf8", edgecolor=C_BLUE, lw=1.5))
    ax.text(1.1, 2.7, "W", ha="center", va="center", fontsize=11, color=C_BLUE, weight="bold")
    ax.text(1.1, 2.4, "(凍結)", ha="center", va="center", fontsize=8, color=C_BLUE)
    # B
    ax.add_patch(Rectangle((2.2, 2.3), 0.35, 0.6, facecolor="#fadbd8", edgecolor=C_RED, lw=1.5))
    ax.text(2.37, 2.6, "B", ha="center", va="center", fontsize=9, color=C_RED, weight="bold")
    # A
    ax.add_patch(Rectangle((2.8, 2.5), 0.6, 0.2, facecolor="#fadbd8", edgecolor=C_RED, lw=1.5))
    ax.text(3.1, 2.6, "A", ha="center", va="center", fontsize=8, color=C_RED, weight="bold")
    ax.text(2.7, 3.5, "ΔW = B·A\n(r << d)", ha="center", fontsize=10, color=C_RED, weight="bold")
    # plus sign
    ax.text(1.95, 2.6, "+", ha="center", va="center", fontsize=18, color=C_GRAY, weight="bold")
    ax.text(2.5, 1.1, "參數量 ↓ 10000x\n推理 0 延遲", ha="center", fontsize=9.5,
            color=C_GRAY, style="italic")

    # DoRA
    ax = axes[1]
    ax.set_xlim(0, 5); ax.set_ylim(0, 5); ax.set_aspect("equal"); ax.axis("off")
    ax.text(2.5, 4.6, "DoRA (2024-02)", ha="center", fontsize=12, weight="bold", color=C_GREEN)
    ax.text(2.5, 4.2, "解耦方向與大小", ha="center", fontsize=10, color=C_GREEN)
    ax.add_patch(Rectangle((0.2, 2), 1.2, 1.2, facecolor="#d6eaf8", edgecolor=C_BLUE, lw=1.5))
    ax.text(0.8, 2.6, "W", ha="center", va="center", fontsize=11, color=C_BLUE, weight="bold")
    ax.text(1.75, 2.6, "=", ha="center", va="center", fontsize=16, color=C_GRAY, weight="bold")
    ax.add_patch(Rectangle((2.1, 2.3), 0.4, 0.6, facecolor="#d5f5e3", edgecolor=C_GREEN, lw=1.5))
    ax.text(2.3, 2.6, "m", ha="center", va="center", fontsize=11, color=C_GREEN, weight="bold")
    ax.text(2.65, 2.6, "·", ha="center", va="center", fontsize=16, color=C_GRAY)
    # direction with LoRA update
    ax.add_patch(Rectangle((2.85, 2.1), 1.5, 1.0, facecolor="#fef9e7", edgecolor=C_ORANGE, lw=1.5))
    ax.text(3.6, 2.6, "V + ΔV", ha="center", va="center", fontsize=10, color=C_ORANGE, weight="bold")
    ax.text(3.6, 2.3, "(LoRA)", ha="center", va="center", fontsize=8, color=C_ORANGE)
    ax.text(2.6, 3.5, "方向用 LoRA 更新\n大小 m 獨立學", ha="center", fontsize=9.5, color=C_GREEN)
    ax.text(2.5, 1.1, "+3–4% accuracy\n2025 業界預設", ha="center", fontsize=9.5,
            color=C_GRAY, style="italic")

    # PiSSA
    ax = axes[2]
    ax.set_xlim(0, 5); ax.set_ylim(0, 5); ax.set_aspect("equal"); ax.axis("off")
    ax.text(2.5, 4.6, "PiSSA (2024-04)", ha="center", fontsize=12, weight="bold", color=C_PURPLE)
    ax.text(2.5, 4.2, "SVD 初始化", ha="center", fontsize=10, color=C_PURPLE)
    ax.add_patch(Rectangle((0.3, 2), 1.2, 1.2, facecolor="#d6eaf8", edgecolor=C_BLUE, lw=1.5))
    ax.text(0.9, 2.6, "W", ha="center", va="center", fontsize=11, color=C_BLUE, weight="bold")
    ax.text(1.75, 2.6, "=", ha="center", va="center", fontsize=16, color=C_GRAY, weight="bold")
    # SVD init
    ax.add_patch(Rectangle((2.1, 2.3), 0.4, 0.6, facecolor="#fadbd8", edgecolor=C_RED, lw=1.5))
    ax.text(2.3, 2.6, "B*", ha="center", va="center", fontsize=9, color=C_RED, weight="bold")
    ax.add_patch(Rectangle((2.6, 2.5), 0.65, 0.2, facecolor="#fadbd8", edgecolor=C_RED, lw=1.5))
    ax.text(2.92, 2.6, "A*", ha="center", va="center", fontsize=9, color=C_RED, weight="bold")
    ax.text(3.5, 2.6, "+ W_res", ha="left", va="center", fontsize=9.5, color=C_GRAY)
    ax.text(2.7, 3.5, "用 W 的 SVD 主成分\n初始化 A*, B*", ha="center", fontsize=9.5, color=C_PURPLE)
    ax.text(2.5, 1.1, "收斂快 2–3x\nCPT 長序列首選", ha="center", fontsize=9.5,
            color=C_GRAY, style="italic")

    fig.suptitle("PEFT 三大變體原理對比：LoRA / DoRA / PiSSA",
                 fontsize=13, weight="bold", y=0.98)
    plt.savefig(OUT / "05_lora_variants.png")
    plt.close()


# ============================================================
# Figure 6 — Qwen3-VL vs Qwen3.6 對比
# ============================================================
def fig6_qwen_compare():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Left: Qwen3-VL-32B
    ax1.set_xlim(0, 10); ax1.set_ylim(0, 10); ax1.set_aspect("equal"); ax1.axis("off")
    ax1.set_title("Qwen3-VL-32B (2025-09)", fontsize=13, weight="bold", color=C_BLUE, pad=10)

    # vision encoder
    box(ax1, 0.5, 7.5, 3.5, 1.2, "Vision Encoder\n(NaViT + Window Attn)",
        fc="#d6eaf8", ec=C_BLUE, fontsize=9, weight="bold")
    # projector / DeepStack
    box(ax1, 5.5, 6.8, 4, 1.8,
        "DeepStack Fusion\n多層 ViT 特徵 → LLM 前 3 層",
        fc="#fef9e7", ec=C_ORANGE, fontsize=9)
    # LLM
    box(ax1, 0.5, 2, 9, 3.8,
        "Standard Transformer LLM\n(M-RoPE + Interleaved)\n32B params, 64 層",
        fc="#d5f5e3", ec=C_GREEN, fontsize=10, weight="bold")
    # arrows
    arrow(ax1, 2.25, 7.5, 2.25, 5.8, color=C_BLUE, lw=1.8)
    arrow(ax1, 7.5, 6.8, 7.5, 5.8, color=C_ORANGE, lw=1.8)

    # stats
    ax1.text(5, 1, "Context: 256K 原生\nAttention: Standard\n生態: MS-SWIFT day-0 OK",
             ha="center", fontsize=9, color=C_GRAY, style="italic")
    ax1.text(5, 9.4, "VL 專用分支", ha="center", fontsize=10, color=C_BLUE, style="italic")

    # Right: Qwen3.6-27B
    ax2.set_xlim(0, 10); ax2.set_ylim(0, 10); ax2.set_aspect("equal"); ax2.axis("off")
    ax2.set_title("Qwen3.6-27B (2026-04-22)", fontsize=13, weight="bold", color=C_RED, pad=10)

    # vision encoder (native, integrated)
    box(ax2, 0.5, 7.5, 3.5, 1.2, "Vision Encoder\n(Native)",
        fc="#d6eaf8", ec=C_BLUE, fontsize=9, weight="bold")

    # Unified LLM with mixed architecture
    ax2.add_patch(FancyBboxPatch((0.5, 2.0), 9.0, 5.0, boxstyle="round,pad=0.02,rounding_size=0.08",
                                 linewidth=1.4, facecolor="#fadbd8", edgecolor=C_RED))
    ax2.text(5.0, 6.65, "Unified LLM (27B, 64 層)", ha="center", va="center",
             fontsize=10, weight="bold", color=C_RED)

    # Inner blocks showing the 3:1 mix
    for i, (y, label, color) in enumerate([
        (5.5, "Gated DeltaNet  →  FFN  (×3)", "#eaeded"),
        (4.5, "Gated DeltaNet  →  FFN  (×3)", "#eaeded"),
        (3.5, "Gated DeltaNet  →  FFN  (×3)", "#eaeded"),
        (2.5, "Gated Attention →  FFN  (×1)", "#f5cba7"),
    ]):
        ax2.add_patch(Rectangle((1, y), 8, 0.7, facecolor=color, edgecolor=C_GRAY, lw=1))
        ax2.text(5, y + 0.35, label, ha="center", va="center", fontsize=8.5,
                 color=C_GRAY if "DeltaNet" in label else C_RED, weight="bold")

    ax2.text(5, 6.33, "重複 16 次 → 64 層", ha="center", fontsize=8.5, color=C_RED, style="italic")
    arrow(ax2, 2.25, 7.5, 2.25, 7.0, color=C_BLUE, lw=1.8)
    ax2.text(5, 1, "Context: 262K 原生 / 1M 外推\nAttention: Gated DeltaNet + Attention 3:1\n生態: day-0 支援待驗證 ⚠",
             ha="center", fontsize=9, color=C_GRAY, style="italic")
    ax2.text(5, 9.4, "VL 併回主線", ha="center", fontsize=10, color=C_RED, style="italic", weight="bold")

    plt.savefig(OUT / "06_qwen_compare.png")
    plt.close()


# ============================================================
# Figure 7 — 競品 2×2 矩陣
# ============================================================
def fig7_competitor_matrix():
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.set_aspect("equal")

    # axes
    ax.axhline(y=5, color=C_GRAY, lw=1.5)
    ax.axvline(x=5, color=C_GRAY, lw=1.5)

    # quadrant backgrounds
    ax.add_patch(Rectangle((0, 5), 5, 5, facecolor="#d5f5e3", alpha=0.35, zorder=0))
    ax.add_patch(Rectangle((5, 5), 5, 5, facecolor="#fadbd8", alpha=0.35, zorder=0))
    ax.add_patch(Rectangle((0, 0), 5, 5, facecolor="#eaeded", alpha=0.35, zorder=0))
    ax.add_patch(Rectangle((5, 0), 5, 5, facecolor="#eaeded", alpha=0.35, zorder=0))

    # quadrant labels
    ax.text(2.5, 9.5, "開源 + 純文字", ha="center", fontsize=11, weight="bold", color=C_GREEN)
    ax.text(7.5, 9.5, "開源 + 多模態", ha="center", fontsize=11, weight="bold", color=C_RED)
    ax.text(2.5, 0.4, "閉源 + 純文字", ha="center", fontsize=11, weight="bold", color=C_GRAY)
    ax.text(7.5, 0.4, "閉源 + 多模態", ha="center", fontsize=11, weight="bold", color=C_GRAY)

    # occupants
    # top-left: SemiKong
    box(ax, 0.8, 7, 3.5, 1.4,
        "SemiKong\n(Llama 3.1 70B + 525.6M tokens)\n2024-11 已佔位",
        fc="white", ec=C_GREEN, fontsize=9, weight="bold", color=C_GREEN)

    # top-right: BLANK — key message
    ax.add_patch(Rectangle((5.5, 6.5), 4, 2.3, facecolor="#ffffff", edgecolor=C_RED, lw=2.5, linestyle="--"))
    ax.text(7.5, 8.2, "★ 空白象限 ★", ha="center", fontsize=11, weight="bold", color=C_RED)
    ax.text(7.5, 7.7, "尚無開源半導體 VLM", ha="center", fontsize=10, color=C_RED)
    ax.text(7.5, 7.1, "Qwen3.6 + SemiKong\n→ 切入點", ha="center", fontsize=9,
            weight="bold", color=C_RED, style="italic")

    # bottom-left: Samsung/TSMC internal
    box(ax, 0.8, 2.5, 3.5, 1.6,
        "TSMC / Samsung / Intel\n內部 domain LLM\n(無公開證據)",
        fc="white", ec=C_GRAY, fontsize=9, color=C_GRAY)

    # bottom-right: commercial VLM
    box(ax, 5.5, 2, 4, 2.3,
        "KLA AI Defect / ASML DL-OPC\nApplied SEMVision H20\nLasertec EUV Mask Inspection\nNVIDIA Cosmos Reason FT",
        fc="white", ec=C_GRAY, fontsize=9, color=C_GRAY)

    # axes labels
    ax.text(5, -0.2, "→ 是否支援視覺 (vision)", ha="center", fontsize=10, color=C_GRAY, weight="bold")
    ax.text(-0.2, 5, "↑ 是否開源", ha="center", fontsize=10, color=C_GRAY, weight="bold", rotation=90)

    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values(): s.set_visible(False)
    ax.set_title("半導體 Domain Model 競品格局 2×2 矩陣",
                 fontsize=13, weight="bold", pad=15)

    plt.savefig(OUT / "07_competitor_matrix.png")
    plt.close()


# ============================================================
# Figure 8 — Vision Encoder 凍結決策樹
# ============================================================
def fig8_freeze_decision_tree():
    fig, ax = plt.subplots(figsize=(13, 7))
    ax.set_xlim(0, 13); ax.set_ylim(0, 7); ax.set_aspect("equal"); ax.axis("off")

    # root
    box(ax, 5, 5.8, 3, 0.9, "Vision encoder\n要不要解凍？",
        fc="#d6eaf8", ec=C_BLUE, fontsize=10, weight="bold")

    # level 2: three branches
    # branch 1: RGB natural
    box(ax, 0.3, 3.8, 3.5, 1.2,
        "Domain 是 RGB\n自然影像子集？\n(e.g. e-commerce)",
        fc="#d5f5e3", ec=C_GREEN, fontsize=9)
    # branch 2: doc/chart
    box(ax, 4.7, 3.8, 3.6, 1.2,
        "Domain 是文件 / chart？\n(e.g. FAR, OCD 圖表)",
        fc="#fef9e7", ec=C_ORANGE, fontsize=9)
    # branch 3: medical/SEM
    box(ax, 9.2, 3.8, 3.5, 1.2,
        "Domain 是 SEM/TEM\n視覺分佈完全不同？\n(e.g. wafer defect)",
        fc="#fadbd8", ec=C_RED, fontsize=9)

    # arrows
    arrow(ax, 6.2, 5.8, 2.05, 5, color=C_GRAY, lw=1.5)
    arrow(ax, 6.5, 5.8, 6.5, 5, color=C_GRAY, lw=1.5)
    arrow(ax, 6.8, 5.8, 10.95, 5, color=C_GRAY, lw=1.5)

    # leaves
    box(ax, 0.3, 1.5, 3.5, 1.5,
        "✓ 全凍 ViT OK\n省最多 VRAM\nreplay ratio 可降",
        fc="white", ec=C_GREEN, fontsize=9, weight="bold", color=C_GREEN)
    box(ax, 4.7, 1.5, 3.6, 1.5,
        "✓ 凍前半、訓後半\n或解凍最後 3-6 層\nreplay 1:2",
        fc="white", ec=C_ORANGE, fontsize=9, weight="bold", color=C_ORANGE)
    box(ax, 9.2, 1.5, 3.5, 1.5,
        "✓ 全解凍 ViT\n或至少凍前 1/4\nreplay 1:2-1:3\nViT lr = LLM lr / 10",
        fc="white", ec=C_RED, fontsize=9, weight="bold", color=C_RED)

    arrow(ax, 2.05, 3.8, 2.05, 3, color=C_GREEN, lw=1.5)
    arrow(ax, 6.5, 3.8, 6.5, 3, color=C_ORANGE, lw=1.5)
    arrow(ax, 10.95, 3.8, 10.95, 3, color=C_RED, lw=1.5)

    # bottom caption
    ax.text(6.5, 0.5,
            "核心原則：原始 ViT 在 RGB 自然影像預訓練，特徵空間不覆蓋灰階高頻紋理（SEM／TEM）\n"
            "凍 = 省 VRAM 但精度受限於 ViT 天花板 ｜ 解凍 = 精度上限高但訓練不穩 + 需 replay",
            ha="center", fontsize=9, color=C_GRAY, style="italic")

    ax.set_title("Vision Encoder 凍結策略決策樹",
                 fontsize=13, weight="bold", pad=15)

    plt.savefig(OUT / "08_freeze_decision_tree.png")
    plt.close()


# ============================================================
# Figure 9 — OOM 排查 7 步法
# ============================================================
def fig9_oom_flowchart():
    fig, ax = plt.subplots(figsize=(13, 7.2))
    ax.set_xlim(0, 13); ax.set_ylim(-0.1, 7.3); ax.set_aspect("equal"); ax.axis("off")

    # === Header bar: CUDA OOM prompt ===
    box(ax, 0.2, 6.3, 12.6, 0.6, "⚠  CUDA OOM — 按效果順序嘗試 7 步；每步後重試，OK 即退出",
        fc="#fadbd8", ec=C_RED, fontsize=11, weight="bold", color=C_RED)

    # Header down-arrow into step 1 (step 1 at x=0.2, w=2.8 → top-center 1.6)
    arrow(ax, 1.6, 6.3, 1.6, 5.81, color=C_GRAY, lw=1.4)

    # === Group label: 配置級 (row 1) ===
    ax.text(0.2, 6.02, "【配置級】不改 model 結構，先試這 4 招",
            fontsize=9, color=C_ORANGE, weight="bold", style="italic")

    # === Row 1 steps (aligned: x = 0.2, 3.4, 6.6, 9.8 — 4 cols width 2.8, gap 0.4) ===
    row1 = [
        (0.2, 4.6, "1. 降 max_pixels\n(VLM 特有，省最多)"),
        (3.4, 4.6, "2. batch=1\n+ grad_accum ↑"),
        (6.6, 4.6, "3. 開 gradient\ncheckpointing"),
        (9.8, 4.6, "4. 開 FlashAttn 2/3"),
    ]
    for x, y, text in row1:
        box(ax, x, y, 2.8, 1.2, text, fc="#fdebd0", ec=C_ORANGE, fontsize=9, weight="bold")

    # Row 1 horizontal arrows (between right-edge and next left-edge, at y=5.2 = middle of box)
    for x_right in [3.0, 6.2, 9.4]:
        arrow(ax, x_right, 5.2, x_right + 0.4, 5.2, color=C_GRAY, lw=1.4)

    # === Wrap-around: step 4 → step 5 ===
    # Step 4 bottom-center (11.2, 4.6) → down to 3.9 → left to 1.6 → down to step 5 top (1.6, 3.1)
    ax.plot([11.2, 11.2], [4.6, 3.9], color=C_GRAY, lw=1.4)
    ax.plot([11.2, 1.6], [3.9, 3.9], color=C_GRAY, lw=1.4)
    arrow(ax, 1.6, 3.9, 1.6, 3.1, color=C_GRAY, lw=1.4)

    # White-bg condition label on wrap arrow (lesson: 分支標籤白底小框蓋在箭頭上)
    # zorder=5 > ax.plot default 2, otherwise line shows through label
    cond = FancyBboxPatch((5.4, 3.75), 2.2, 0.3,
                          boxstyle="round,pad=0.02,rounding_size=0.05",
                          linewidth=0.9, facecolor="white", edgecolor=C_GRAY,
                          zorder=5)
    ax.add_patch(cond)
    ax.text(6.5, 3.9, "仍 OOM ↓ 進第二層", ha="center", va="center",
            fontsize=9, color=C_GRAY, weight="bold", zorder=6)

    # === Group label: 架構級 (row 2) ===
    ax.text(0.2, 3.32, "【架構級】改 model 包裝 / 參數規模",
            fontsize=9, color=C_BLUE, weight="bold", style="italic")

    # === Row 2 steps (same alignment as row 1, 3 boxes) ===
    row2 = [
        (0.2, 1.9, "5. LoRA → QLoRA\n(4-bit)"),
        (3.4, 1.9, "6. 降 LoRA rank\n(64→32→16)"),
        (6.6, 1.9, "7. Vision encoder\n全凍 (last resort)"),
    ]
    edges2 = [C_BLUE, C_BLUE, C_RED]
    fills2 = ["#d6eaf8", "#d6eaf8", "#fadbd8"]
    for (x, y, text), ec, fc in zip(row2, edges2, fills2):
        box(ax, x, y, 2.8, 1.2, text, fc=fc, ec=ec, fontsize=9, weight="bold")

    # Row 2 horizontal arrows at y=2.5 (middle)
    for x_right in [3.0, 6.2]:
        arrow(ax, x_right, 2.5, x_right + 0.4, 2.5, color=C_GRAY, lw=1.4)

    # === Final box: centered below step 7 (step 7 bottom-center at 8.0, 1.9) ===
    box(ax, 6.2, 0.3, 3.6, 0.8, "✓ 仍 OOM → 換更大 GPU",
        fc="#d5f5e3", ec=C_GREEN, fontsize=10, weight="bold", color=C_GREEN)

    # Step 7 → Final arrow (consistent gray, not green — green reserved for success box)
    arrow(ax, 8.0, 1.9, 8.0, 1.1, color=C_GRAY, lw=1.4)

    ax.set_title("VLM Fine-tune OOM 排查 7 步法（按省 VRAM 效果排序）",
                 fontsize=13, weight="bold", pad=15)

    plt.savefig(OUT / "09_oom_flowchart.png")
    plt.close()


# ============================================================
# Figure 10 — 12 個月時程 Gantt
# ============================================================
def fig10_gantt():
    fig, ax = plt.subplots(figsize=(14, 6.5))

    tasks = [
        ("月 1 — 資料建設", 1, 1, "#95a5a6", "SemiKong import 可省 0.5-1 月"),
        ("月 2 — CPT", 2, 1, "#d68910", "8×H100 × 2 週"),
        ("月 3 — SFT", 3, 1, "#d68910", "8×H100 × 1 週"),
        ("月 4 — MPO 對齊", 4, 1, "#2e86c1", "4×H100 × 1 週, +3–7 pp 穩定性"),
        ("月 5 — V-DPO", 5, 1, "#2e86c1", "4×H100 × 2 週, 降 hallucination"),
        ("月 6–7 — GRPO", 6, 2, "#1e8449", "8×H100 × 4 週, +5–15 pp (RLVR)"),
        ("月 8–11 — Agent SFT", 8, 4, "#5b2c6f", "Tool + GUI agent"),
        ("月 12+ — 部署監測", 12, 2, "#c0392b", "Shadow → canary → 25% → 100%"),
    ]

    for i, (name, start, duration, color, note) in enumerate(tasks):
        y = len(tasks) - i - 1
        ax.barh(y, duration, left=start - 1, color=color, alpha=0.85,
                edgecolor="white", linewidth=1.5, height=0.7)
        ax.text(start - 1 + duration + 0.15, y, note, va="center",
                fontsize=8.5, color=C_GRAY, style="italic")
        ax.text(-0.3, y, name, va="center", ha="right",
                fontsize=10, weight="bold", color=color)

    ax.set_xlim(-0.5, 16)
    ax.set_ylim(-0.5, len(tasks) - 0.3)
    ax.set_xticks(range(0, 14))
    ax.set_xticklabels([f"M{i+1}" if i < 13 else "" for i in range(14)], fontsize=9)
    ax.set_yticks([])
    ax.grid(axis="x", alpha=0.2, linestyle="--")
    for s in ["top", "right", "left"]:
        ax.spines[s].set_visible(False)
    ax.set_xlabel("Month", fontsize=10)
    ax.set_title("6–8 人團隊 × Qwen3.6-27B Production 路線圖 — 12 個月時程",
                 fontsize=13, weight="bold", pad=15)

    # legend footer
    ax.text(7, -0.9, "總 infra 約 USD 200K (spot H100 × 16 + A100 × 4) + 人力 USD 1.5–2.5M = 總成本量級 USD 2–3M",
            ha="center", fontsize=9, color=C_GRAY, style="italic")

    plt.tight_layout()
    plt.savefig(OUT / "10_gantt.png")
    plt.close()


if __name__ == "__main__":
    print("Generating figures...")
    for i, fn in enumerate([
        fig1_hv_method, fig2_four_stage_pipeline, fig3_seven_year_timeline,
        fig4_alignment_tree, fig5_lora_variants, fig6_qwen_compare,
        fig7_competitor_matrix, fig8_freeze_decision_tree,
        fig9_oom_flowchart, fig10_gantt,
    ], 1):
        print(f"  [{i}/10] {fn.__name__}")
        fn()
    print(f"Done. Files in {OUT}")
