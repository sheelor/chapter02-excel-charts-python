"""01 渐变柱形图：各区域销售量"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
from common import save, gradient_bars, strip_axes

regions = ["华北", "华南", "东北", "西北", "西南", "华东"]
sales = [2354, 1902, 3524, 2698, 2896, 2563]

fig, ax = plt.subplots(figsize=(8, 5))
x = np.arange(len(regions))
gradient_bars(ax, x, sales, width=0.5, color=("#5B9BD5", "#1F4E79"))

for xi, v in zip(x, sales):
    ax.text(xi, v + 70, str(v), ha="center", va="bottom", fontsize=11)

ax.set_xticks(x)
ax.set_xticklabels(regions, fontsize=11)
ax.set_xlim(-0.75, len(regions) - 0.25)
ax.set_ylim(0, 4000)
ax.set_title("各区域销售量", fontsize=15, pad=12)
ax.grid(axis="y", ls="--", alpha=0.3)
ax.set_axisbelow(True)
strip_axes(ax, keep=("left", "bottom"))
save(fig, "01_渐变柱形图")
