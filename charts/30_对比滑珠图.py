"""30 对比滑珠图：2021 vs 2022 完成率（哑铃图）"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
from common import save, PALETTE, strip_axes

regions = ["华东", "西北", "东北", "华北", "华南"]
rate_2022 = [0.35, 0.51, 0.62, 0.74, 0.86]
rate_2021 = [0.45, 0.39, 0.53, 0.69, 0.92]

fig, ax = plt.subplots(figsize=(9, 5))
y = np.arange(len(regions))[::-1]

ax.barh(y, [1] * len(y), height=0.10, color="#EEF1F5", zorder=2)          # 轨道
for yi, r22, r21 in zip(y, rate_2022, rate_2021):
    lo, hi = sorted([r21, r22])
    ax.plot([lo, hi], [yi, yi], color="#B9C6D8", lw=5,
            solid_capstyle="round", zorder=3)                             # 连接杆

ax.scatter(rate_2022, y, s=380, color=PALETTE[0], zorder=4,
           edgecolor="white", linewidth=2, label="2022完成率")
ax.scatter(rate_2021, y, s=380, color=PALETTE[1], zorder=4,
           edgecolor="white", linewidth=2, label="2021完成率")

for yi, r22, r21 in zip(y, rate_2022, rate_2021):
    ax.text(r22, yi + 0.28, f"{r22:.0%}", ha="center", fontsize=9, color=PALETTE[0])
    ax.text(r21, yi - 0.32, f"{r21:.0%}", ha="center", fontsize=9, color=PALETTE[1])

ax.set_yticks(y)
ax.set_yticklabels(regions, fontsize=11)
ax.set_xlim(0, 1.08)
ax.set_ylim(-0.6, len(regions) - 0.2)
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:.0%}"))
ax.set_title("2021 vs 2022 各区域完成率对比滑珠图", fontsize=15, pad=12)
ax.legend(frameon=False, loc="upper left")
ax.grid(axis="x", ls="--", alpha=0.3)
ax.set_axisbelow(True)
strip_axes(ax, keep=("left", "bottom"))
save(fig, "30_对比滑珠图")
