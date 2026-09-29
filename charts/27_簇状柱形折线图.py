"""27 簇状柱形折线图：两年销量分组柱形 + 同比折线（副轴）"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
from common import save, PALETTE, strip_axes

regions = ["华北", "华南", "东北", "西北", "西南", "华东"]
sales_2022 = [2354, 1902, 3524, 2698, 2896, 2563]
sales_2021 = [2021, 1563, 3213, 2531, 2631, 2361]
yoy = [0.16, 0.22, 0.10, 0.07, 0.10, 0.09]

fig, ax = plt.subplots(figsize=(9.5, 5))
x = np.arange(len(regions))
w = 0.32
ax.bar(x - w / 2, sales_2022, width=w, color=PALETTE[0], zorder=3, label="2022销量")
ax.bar(x + w / 2, sales_2021, width=w, color=PALETTE[2], zorder=3, label="2021销量")

for xi, (a, b) in enumerate(zip(sales_2022, sales_2021)):
    ax.text(xi - w / 2, a + 50, str(a), ha="center", va="bottom", fontsize=9)
    ax.text(xi + w / 2, b + 50, str(b), ha="center", va="bottom", fontsize=9)

ax2 = ax.twinx()
ax2.plot(x, yoy, color=PALETTE[1], lw=2.2, marker="o", markersize=7,
         zorder=4, label="同比去年")
for xi, r in zip(x, yoy):
    ax2.text(xi, r + 0.012, f"{r:.0%}", ha="center", va="bottom",
             fontsize=9, color=PALETTE[1])

ax.set_xticks(x)
ax.set_xticklabels(regions, fontsize=11)
ax.set_ylim(0, 4300)
ax2.set_ylim(0, 0.30)
ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:.0%}"))
ax.set_title("各区域两年销量与同比", fontsize=15, pad=12)
ax.grid(axis="y", ls="--", alpha=0.3)
ax.set_axisbelow(True)
strip_axes(ax, keep=("left", "bottom"))
strip_axes(ax2, keep=("right",))
h1, l1 = ax.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax.legend(h1 + h2, l1 + l2, loc="upper left", frameon=False, ncol=3)
save(fig, "27_簇状柱形折线图")
