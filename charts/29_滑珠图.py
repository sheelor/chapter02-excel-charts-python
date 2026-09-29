"""29 滑珠图：完成率轨道 + 滑珠"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
from common import save, PALETTE, strip_axes

regions = ["华东", "西北", "东北", "华北", "华南"]
rates = [0.35, 0.51, 0.62, 0.74, 0.86]

fig, ax = plt.subplots(figsize=(9, 5))
y = np.arange(len(regions))[::-1]

ax.barh(y, [1] * len(y), height=0.14, color="#E3E9F0", zorder=2)          # 轨道
ax.barh(y, rates, height=0.14, color="#B7CBE3", zorder=3)                 # 已完成段
ax.scatter(rates, y, s=420, color=PALETTE[0], zorder=4,
           edgecolor="white", linewidth=2)                                # 滑珠

for yi, r in zip(y, rates):
    ax.text(r, yi, f"{r:.0%}", ha="center", va="center",
            fontsize=10, color="white", fontweight="bold", zorder=5)
    ax.text(1.03, yi, f"{r:.0%}", va="center", fontsize=10, color=PALETTE[0])

ax.set_yticks(y)
ax.set_yticklabels(regions, fontsize=11)
ax.set_xlim(0, 1.12)
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:.0%}"))
ax.set_title("各区域目标完成率滑珠图", fontsize=15, pad=12)
ax.grid(axis="x", ls="--", alpha=0.3)
ax.set_axisbelow(True)
strip_axes(ax, keep=("left", "bottom"))
save(fig, "29_滑珠图")
