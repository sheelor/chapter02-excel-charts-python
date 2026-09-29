"""25 子弹图：实际值 vs 目标值，背景为及格/良好/优秀三档区间"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
from common import save, strip_axes

items = ["口红", "面膜", "隔离", "防晒", "精华", "面霜"]
actual = [653, 523, 648, 856, 714, 785]
target = [700, 500, 600, 900, 600, 600]
bands = [("及格", 600, "#D9D9D9"), ("良好", 200, "#BFBFBF"), ("优秀", 200, "#A6A6A6")]
XMAX = 1000

fig, ax = plt.subplots(figsize=(9, 5.5))
y = np.arange(len(items))[::-1]

for yi in y:
    left = 0
    for name, width_v, c in bands:      # 三档背景区间（堆叠横条）
        ax.barh(yi, width_v, left=left, height=0.72, color=c, zorder=2)
        left += width_v

ax.barh(y, actual, height=0.30, color="#2E75B6", zorder=3, label="实际")
for yi, t in zip(y, target):
    ax.plot([t, t], [yi - 0.36, yi + 0.36], color="#C00000", lw=2.5, zorder=4)
ax.plot([], [], color="#C00000", lw=2.5, label="目标")

for yi, v in zip(y, actual):
    ax.text(v + 12, yi, str(v), va="center", fontsize=10, color="#2E75B6")

ax.set_yticks(y)
ax.set_yticklabels(items, fontsize=11)
ax.set_xlim(0, XMAX)
ax.set_title("商品销量子弹图", fontsize=15, pad=12)
ax.legend(frameon=False, loc="upper center", bbox_to_anchor=(0.5, -0.10), ncol=2)
ax.grid(axis="x", ls="--", alpha=0.3)
ax.set_axisbelow(True)
strip_axes(ax, keep=("left", "bottom"))
# 区间说明
ax.text(300, len(items) - 0.1, "及格 <600", ha="center", fontsize=9, color="#666666")
ax.text(700, len(items) - 0.1, "良好 600-800", ha="center", fontsize=9, color="#666666")
ax.text(900, len(items) - 0.1, "优秀 800-1000", ha="center", fontsize=9, color="#666666")
save(fig, "25_子弹图")
