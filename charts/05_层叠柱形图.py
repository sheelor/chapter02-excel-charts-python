"""05 层叠柱形图：销售额 + 利润额堆叠"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
from common import save, PALETTE, strip_axes

quarters = ["2021Q1", "Q2", "Q3", "Q4", "2022Q1", "Q2"]
sales = [3121, 4086, 4321, 4601, 4936, 4231]
profit = [1020, 1421, 1502, 1623, 1781, 1432]

fig, ax = plt.subplots(figsize=(8.5, 5))
x = np.arange(len(quarters))
ax.bar(x, sales, width=0.55, color=PALETTE[0], zorder=3, label="销售额")
ax.bar(x, profit, width=0.55, bottom=sales, color=PALETTE[1], zorder=3, label="利润额")

for xi, s, p in zip(x, sales, profit):
    ax.text(xi, s / 2, str(s), ha="center", va="center", fontsize=10, color="white")
    ax.text(xi, s + p / 2, str(p), ha="center", va="center", fontsize=10, color="white")
    ax.text(xi, s + p + 120, str(s + p), ha="center", va="bottom", fontsize=10)

ax.set_xticks(x)
ax.set_xticklabels(quarters, fontsize=11)
ax.set_ylim(0, 7500)
ax.set_title("各季度销售额与利润额", fontsize=15, pad=12)
ax.legend(loc="upper left", frameon=False)
ax.grid(axis="y", ls="--", alpha=0.3)
ax.set_axisbelow(True)
strip_axes(ax, keep=("left", "bottom"))
save(fig, "05_层叠柱形图")
