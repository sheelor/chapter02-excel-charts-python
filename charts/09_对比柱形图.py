"""09 对比柱形图：2021 vs 2022 分组柱形 + 差值标注"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
from common import save, PALETTE, strip_axes

items = ["口红", "面膜", "隔离", "防晒", "精华"]
sales_2021 = [3568, 4135, 4436, 4106, 4936]
sales_2022 = [2569, 3241, 2965, 3209, 3541]

fig, ax = plt.subplots(figsize=(9, 5))
x = np.arange(len(items))
w = 0.32
ax.bar(x - w / 2, sales_2021, width=w, color=PALETTE[0], zorder=3, label="2021销量")
ax.bar(x + w / 2, sales_2022, width=w, color=PALETTE[1], zorder=3, label="2022销量")

for xi, (v21, v22) in enumerate(zip(sales_2021, sales_2022)):
    ax.text(xi - w / 2, v21 + 60, str(v21), ha="center", va="bottom", fontsize=9)
    ax.text(xi + w / 2, v22 + 60, str(v22), ha="center", va="bottom", fontsize=9)
    diff = v21 - v22  # 对应 Excel 差值列 =C-D
    ax.text(xi, max(v21, v22) + 330, f"↓{diff}", ha="center", va="bottom",
            fontsize=10, color="#2E7D32", fontweight="bold")

ax.set_xticks(x)
ax.set_xticklabels(items, fontsize=11)
ax.set_ylim(0, 5900)
ax.set_title("2021 vs 2022 商品销量对比", fontsize=15, pad=12)
ax.legend(frameon=False)
ax.grid(axis="y", ls="--", alpha=0.3)
ax.set_axisbelow(True)
strip_axes(ax, keep=("left", "bottom"))
save(fig, "09_对比柱形图")
