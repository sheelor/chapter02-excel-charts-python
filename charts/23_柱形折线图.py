"""23 柱形折线图：销售量（柱） + 同比（线，副轴）"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
from common import save, PALETTE, strip_axes

years = ["2017", "2018", "2019", "2020", "2021", "2022"]
sales = [1603, 2106, 2406, 3265, 3721, 3921]
yoy = [0.27] + [sales[i] / sales[i - 1] - 1 for i in range(1, len(sales))]  # =C4/C3-1

fig, ax = plt.subplots(figsize=(9, 5))
x = np.arange(len(years))
ax.bar(x, sales, width=0.5, color=PALETTE[0], zorder=3, label="销售量")
for xi, v in zip(x, sales):
    ax.text(xi, v + 70, str(v), ha="center", va="bottom", fontsize=10)

ax2 = ax.twinx()
ax2.plot(x, yoy, color=PALETTE[1], lw=2.2, marker="o", markersize=7,
         zorder=4, label="同比")
for xi, r in zip(x, yoy):
    ax2.text(xi, r + 0.02, f"{r:.1%}", ha="center", va="bottom",
             fontsize=9, color=PALETTE[1])

ax.set_xticks(x)
ax.set_xticklabels(years, fontsize=11)
ax.set_ylim(0, 4600)
ax2.set_ylim(0, 0.50)
ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:.0%}"))
ax.set_title("历年销售量与同比", fontsize=15, pad=12)
ax.grid(axis="y", ls="--", alpha=0.3)
ax.set_axisbelow(True)
strip_axes(ax, keep=("left", "bottom"))
strip_axes(ax2, keep=("right",))
h1, l1 = ax.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax.legend(h1 + h2, l1 + l2, loc="upper left", frameon=False)
save(fig, "23_柱形折线图")
