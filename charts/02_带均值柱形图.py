"""02 带均值柱形图：柱形 + 均值虚线"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
from common import save, PALETTE, strip_axes

regions = ["华北", "华南", "东北", "西北", "西南", "华东"]
sales = [2354, 1902, 3524, 2698, 2896, 2563]
mean = float(np.mean(sales))  # 对应 Excel 公式 =AVERAGE(C3:C8)

fig, ax = plt.subplots(figsize=(8, 5))
x = np.arange(len(regions))
ax.bar(x, sales, width=0.5, color=PALETTE[0], zorder=3, label="销售量")
ax.axhline(mean, color=PALETTE[1], ls="--", lw=1.8, zorder=4, label=f"均值 {mean:.0f}")
ax.text(x[-1] + 0.45, mean, f"{mean:.0f}", color=PALETTE[1],
        fontsize=11, va="center", ha="left", fontweight="bold")

for xi, v in zip(x, sales):
    ax.text(xi, v + 70, str(v), ha="center", va="bottom", fontsize=10)

ax.set_xticks(x)
ax.set_xticklabels(regions, fontsize=11)
ax.set_xlim(-0.6, len(regions) - 0.1)
ax.set_ylim(0, 4000)
ax.set_title("各区域销售量与均值", fontsize=15, pad=12)
ax.legend(loc="upper right", frameon=False)
ax.grid(axis="y", ls="--", alpha=0.3)
ax.set_axisbelow(True)
strip_axes(ax, keep=("left", "bottom"))
save(fig, "02_带均值柱形图")
