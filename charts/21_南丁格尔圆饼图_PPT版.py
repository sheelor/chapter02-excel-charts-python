"""21 南丁格尔圆饼图（PPT 版）：部门人数占比，扇区间留缝 + 图例"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
from common import save

depts = ["销售部", "采购部", "工程部", "财务部", "行政部", "人力部"]
shares = [0.292, 0.227, 0.175, 0.136, 0.103, 0.05]
colors = ["#4472C4", "#ED7D31", "#A5A5A5", "#FFC000", "#5B9BD5", "#70AD47"]

fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, polar=True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
ax.axis("off")

n = len(depts)
width = 2 * np.pi / n
theta = np.arange(n) * width
radii = np.sqrt(shares) * 10

bars = ax.bar(theta, radii, width=width * 0.92, bottom=0,   # 0.92 制造扇区缝隙
              color=colors, edgecolor="white", linewidth=1.2, alpha=0.92)

for t, r, v in zip(theta, radii, shares):
    ax.text(t, r * 0.72, f"{v:.1%}", ha="center", va="center",
            fontsize=11, color="white", fontweight="bold")

ax.legend(bars, depts, loc="center left", bbox_to_anchor=(1.05, 0.5),
          frameon=False, fontsize=12)
ax.set_ylim(0, max(radii) + 1.2)
ax.set_title("各部门人数占比南丁格尔圆饼图（PPT 版）", fontsize=15, pad=22)
save(fig, "21_南丁格尔圆饼图_PPT版")
