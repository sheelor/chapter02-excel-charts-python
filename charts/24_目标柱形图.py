"""24 目标柱形图：实际销量柱形 + 目标横线"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
from common import save, PALETTE, strip_axes

items = ["口红", "面膜", "隔离", "防晒", "精华", "面霜"]
actual = [653, 523, 648, 856, 714, 785]
target = [700, 500, 600, 900, 600, 600]

fig, ax = plt.subplots(figsize=(9, 5))
x = np.arange(len(items))
colors = [PALETTE[4] if a >= t else "#A6B8D4" for a, t in zip(actual, target)]
ax.bar(x, actual, width=0.45, color=colors, zorder=3, label="实际销量")

# 目标线
for xi, t in zip(x, target):
    ax.plot([xi - 0.32, xi + 0.32], [t, t], color=PALETTE[1], lw=2.5, zorder=4)
ax.plot([], [], color=PALETTE[1], lw=2.5, label="目标销量")

for xi, v in zip(x, actual):
    ax.text(xi, v + 18, str(v), ha="center", va="bottom", fontsize=10)

ax.set_xticks(x)
ax.set_xticklabels(items, fontsize=11)
ax.set_ylim(0, 1000)
ax.set_title("商品实际销量 vs 目标销量", fontsize=15, pad=12)
ax.legend(frameon=False, loc="upper right")
ax.grid(axis="y", ls="--", alpha=0.3)
ax.set_axisbelow(True)
strip_axes(ax, keep=("left", "bottom"))
save(fig, "24_目标柱形图")
