"""26 柱形圆：柱形顶端带圆形标记，圆内显示同比"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
from common import save, PALETTE, strip_axes

regions = ["华北", "华南", "东北", "西北", "西南", "华东"]
sales = [2354, 1902, 3524, 2698, 2896, 2563]
yoy = [0.12, 0.25, 0.16, 0.21, 0.18, 0.25]
CAP = 4500   # 对应 Excel 占位列

fig, ax = plt.subplots(figsize=(9, 5.5))
x = np.arange(len(regions))
ax.bar(x, sales, width=0.16, color=PALETTE[0], zorder=3)

# 用 scatter 画圆（以点为单位，保证任何坐标比例下都是正圆）
r_pt = 1500  # 圆的大小（points^2）
for xi, v, r in zip(x, sales, yoy):
    ax.scatter(xi, v + 300, s=r_pt * 2, color=PALETTE[1],
               edgecolor="white", linewidth=1.5, zorder=4)
    ax.text(xi, v + 300, f"{r:.0%}", ha="center", va="center",
            fontsize=10, color="white", fontweight="bold", zorder=5)
    ax.text(xi, v + 680, str(v), ha="center", va="bottom", fontsize=10)

ax.set_xticks(x)
ax.set_xticklabels(regions, fontsize=11)
ax.set_ylim(0, 5000)
ax.set_title("各区域销量（圆内为同比）", fontsize=15, pad=12)
ax.grid(axis="y", ls="--", alpha=0.3)
ax.set_axisbelow(True)
strip_axes(ax, keep=("left", "bottom"))
save(fig, "26_柱形圆")
