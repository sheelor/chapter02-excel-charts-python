"""12 菱形走势图：完成率（菱形标记折线）"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
from common import save, PALETTE, strip_axes

months = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月"]
rates = [0.536, 0.498, 0.527, 0.708, 0.609, 0.496, 0.586, 0.704]

fig, ax = plt.subplots(figsize=(9, 5))
x = np.arange(len(months))
ax.plot(x, rates, color=PALETTE[0], lw=2, zorder=3)
ax.plot(x, rates, linestyle="none", marker="D", markersize=13,
        markerfacecolor=PALETTE[1], markeredgecolor="white",
        markeredgewidth=1.5, zorder=4)

for xi, r in zip(x, rates):
    ax.text(xi, r + 0.018, f"{r:.1%}", ha="center", va="bottom", fontsize=10)

ax.set_xticks(x)
ax.set_xticklabels(months, fontsize=11)
ax.set_ylim(0.42, 0.78)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:.0%}"))
ax.set_title("各月完成率走势", fontsize=15, pad=12)
ax.grid(ls="--", alpha=0.3)
ax.set_axisbelow(True)
strip_axes(ax, keep=("left", "bottom"))
save(fig, "12_菱形走势图")
