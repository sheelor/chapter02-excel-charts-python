"""06 蝴蝶图：2021 vs 2022 各区域销量对比（左右对称条形）"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
from common import save, PALETTE

regions = ["华东", "西北", "东北", "华北", "华南"]
sales_2022 = [1215, 1321, 1426, 1531, 2238]
sales_2021 = [1003, 1265, 1531, 1436, 2066]

fig, ax = plt.subplots(figsize=(9, 5))
y = np.arange(len(regions))
ax.barh(y, [-v for v in sales_2022], height=0.6, color=PALETTE[0], zorder=3, label="2022年销量")
ax.barh(y, sales_2021, height=0.6, color=PALETTE[1], zorder=3, label="2021年销量")

for yi, (v22, v21) in enumerate(zip(sales_2022, sales_2021)):
    ax.text(-v22 - 60, yi, str(v22), ha="right", va="center", fontsize=10)
    ax.text(v21 + 60, yi, str(v21), ha="left", va="center", fontsize=10)
    ax.text(0, yi, regions[yi], ha="center", va="center", fontsize=11,
            fontweight="bold", bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none"))

ax.set_yticks([])
ax.set_xlim(-3000, 3000)
ax.set_xticks([-2000, -1000, 0, 1000, 2000])
ax.set_xticklabels([2000, 1000, 0, 1000, 2000])
ax.axvline(0, color="#666666", lw=1)
ax.set_title("2021 vs 2022 各区域销量蝴蝶图", fontsize=15, pad=12)
ax.legend(loc="lower right", frameon=False)
ax.grid(axis="x", ls="--", alpha=0.3)
ax.set_axisbelow(True)
for side in ("top", "right", "left"):
    ax.spines[side].set_visible(False)
save(fig, "06_蝴蝶图")
