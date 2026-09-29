"""07 蝴蝶图（占比版）：2021 vs 2022 各区域销量占比"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
from common import save, PALETTE

regions = ["华东", "西北", "东北", "华北", "华南"]
share_2022 = [0.36, 0.31, 0.18, 0.13, 0.09]
share_2021 = [0.42, 0.26, 0.19, 0.12, 0.05]

fig, ax = plt.subplots(figsize=(9, 5))
y = np.arange(len(regions))
ax.barh(y, [-v for v in share_2022], height=0.6, color="#5B9BD5", zorder=3, label="2022年")
ax.barh(y, share_2021, height=0.6, color="#ED7D31", zorder=3, label="2021年")

for yi, (v22, v21) in enumerate(zip(share_2022, share_2021)):
    ax.text(-v22 - 0.015, yi, f"{v22:.0%}", ha="right", va="center", fontsize=10)
    ax.text(v21 + 0.015, yi, f"{v21:.0%}", ha="left", va="center", fontsize=10)
    ax.text(0, yi, regions[yi], ha="center", va="center", fontsize=11,
            fontweight="bold", bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none"))

ax.set_yticks([])
ax.set_xlim(-0.55, 0.55)
ax.set_xticks([-0.4, -0.2, 0, 0.2, 0.4])
ax.set_xticklabels(["40%", "20%", "0", "20%", "40%"])
ax.axvline(0, color="#666666", lw=1)
ax.set_title("2021 vs 2022 各区域销量占比蝴蝶图", fontsize=15, pad=12)
ax.legend(loc="upper right", frameon=False)
ax.grid(axis="x", ls="--", alpha=0.3)
ax.set_axisbelow(True)
for side in ("top", "right", "left"):
    ax.spines[side].set_visible(False)
save(fig, "07_蝴蝶图_占比")
