"""04 标注柱形图：突出最高值并添加标注"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
from common import save, PALETTE, strip_axes

items = ["口红", "面膜", "隔离", "防晒", "精华", "面霜", "眼影", "气垫"]
sales = [9221, 5102, 6571, 5760, 6321, 8612, 2645, 5321]

fig, ax = plt.subplots(figsize=(9, 5))
x = np.arange(len(items))
imax = int(np.argmax(sales))
colors = [PALETTE[1] if i == imax else PALETTE[0] for i in range(len(items))]
ax.bar(x, sales, width=0.55, color=colors, zorder=3)

for xi, v in zip(x, sales):
    ax.text(xi, v + 150, str(v), ha="center", va="bottom", fontsize=10)

ax.annotate(f"销量最高：{items[imax]} {sales[imax]}",
            xy=(imax, sales[imax] + 300), xytext=(imax + 1.6, sales[imax] * 0.92),
            fontsize=12, color=PALETTE[1], fontweight="bold",
            arrowprops=dict(arrowstyle="->", color=PALETTE[1], lw=1.5))

ax.set_xticks(x)
ax.set_xticklabels(items, fontsize=11)
ax.set_ylim(0, 10500)
ax.set_title("商品销量（突出最高值）", fontsize=15, pad=12)
ax.grid(axis="y", ls="--", alpha=0.3)
ax.set_axisbelow(True)
strip_axes(ax, keep=("left", "bottom"))
save(fig, "04_标注柱形图")
