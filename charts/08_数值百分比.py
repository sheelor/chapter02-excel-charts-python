"""08 数值百分比：柱形 + 同比百分比标注"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
from common import save, PALETTE, strip_axes

regions = ["华北", "华南", "东北", "西北", "西南", "华东"]
sales = [4321, 1946, 1536, 1872, 1369, 2109]
yoy = [-0.136, -0.208, -0.093, -0.159, -0.179, -0.058]

fig, ax = plt.subplots(figsize=(9, 5))
x = np.arange(len(regions))
ax.bar(x, sales, width=0.55, color=PALETTE[0], zorder=3)

for xi, v, r in zip(x, sales, yoy):
    ax.text(xi, v + 90, str(v), ha="center", va="bottom", fontsize=10)
    arrow = "↑" if r >= 0 else "↓"
    color = "#C00000" if r >= 0 else "#2E7D32"
    ax.text(xi, v + 420, f"{arrow}{abs(r):.1%}", ha="center", va="bottom",
            fontsize=10, color=color, fontweight="bold")

ax.set_xticks(x)
ax.set_xticklabels(regions, fontsize=11)
ax.set_ylim(0, 5200)
ax.set_title("各区域销量及同比", fontsize=15, pad=12)
ax.grid(axis="y", ls="--", alpha=0.3)
ax.set_axisbelow(True)
strip_axes(ax, keep=("left", "bottom"))
save(fig, "08_数值百分比")
