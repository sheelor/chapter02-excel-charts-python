"""13 对比折线图：2021 vs 2022 月销量"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
from common import save, PALETTE, strip_axes

months = ["1月", "2月", "3月", "4月", "5月", "6月"]
y2021 = [1686, 1345, 1934, 1658, 1865, 1936]
y2022 = [1385, 1846, 1654, 1936, 2564, 2236]

fig, ax = plt.subplots(figsize=(9, 5))
x = np.arange(len(months))
ax.plot(x, y2021, color=PALETTE[0], lw=2.2, marker="o", markersize=7, zorder=3)
ax.plot(x, y2022, color=PALETTE[1], lw=2.2, marker="o", markersize=7, zorder=3)

# 系列名称标注在折线末端（Excel 常见做法）
ax.text(x[-1] + 0.15, y2021[-1], "2021年", color=PALETTE[0], fontsize=12,
        va="center", fontweight="bold")
ax.text(x[-1] + 0.15, y2022[-1], "2022年", color=PALETTE[1], fontsize=12,
        va="center", fontweight="bold")

for xi, (a, b) in enumerate(zip(y2021, y2022)):
    ax.text(xi, a + 80, str(a), ha="center", va="bottom", fontsize=9, color=PALETTE[0])
    ax.text(xi, b - 80, str(b), ha="center", va="top", fontsize=9, color=PALETTE[1])

ax.set_xticks(x)
ax.set_xticklabels(months, fontsize=11)
ax.set_xlim(-0.4, len(months) + 0.3)
ax.set_ylim(1100, 2900)
ax.set_title("2021 vs 2022 月销量对比", fontsize=15, pad=12)
ax.grid(ls="--", alpha=0.3)
ax.set_axisbelow(True)
strip_axes(ax, keep=("left", "bottom"))
save(fig, "13_对比折线图")
