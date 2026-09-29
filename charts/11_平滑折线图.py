"""11 平滑折线图：销量走势（样条平滑）"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import PchipInterpolator
from common import save, PALETTE, strip_axes

months = ["5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月", "1月", "2月", "3月"]
sales = [146, 198, 296, 412, 506, 615, 789, 1021, 3782, 3215, 2936]

x = np.arange(len(months))
xs = np.linspace(0, len(months) - 1, 300)
ys = PchipInterpolator(x, sales)(xs)  # PCHIP 平滑且保形，不会过冲

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(xs, ys, color=PALETTE[0], lw=2.2, zorder=3)
ax.fill_between(xs, ys, 0, color=PALETTE[0], alpha=0.12, zorder=2)
ax.scatter(x, sales, color=PALETTE[0], s=36, zorder=4)

for xi, v in zip(x, sales):
    ax.text(xi, v + 120, str(v), ha="center", va="bottom", fontsize=9)

ax.set_xticks(x)
ax.set_xticklabels(months, fontsize=10)
ax.set_ylim(0, 4500)
ax.set_title("月销量走势（2021.05 - 2022.03）", fontsize=15, pad=12)
ax.grid(axis="y", ls="--", alpha=0.3)
ax.set_axisbelow(True)
strip_axes(ax, keep=("left", "bottom"))
save(fig, "11_平滑折线图")
