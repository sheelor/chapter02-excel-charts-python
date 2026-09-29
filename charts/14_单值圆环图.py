"""14 单值圆环图：完成率 85%"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import matplotlib.pyplot as plt
from common import save, PALETTE

rate = 0.85

fig, ax = plt.subplots(figsize=(6, 6))
wedges, _ = ax.pie(
    [rate, 1 - rate],
    startangle=90, counterclock=False,
    colors=[PALETTE[0], "#E7EBF0"],
    wedgeprops=dict(width=0.28, edgecolor="white"),
)
# 圆角端点
import numpy as np
for ang_deg in (90, 90 - rate * 360):
    ang = np.deg2rad(ang_deg)
    ax.scatter(0.86 * np.cos(ang), 0.86 * np.sin(ang), s=560,
               color=PALETTE[0], zorder=5)

ax.text(0, 0.06, f"{rate:.0%}", ha="center", va="center",
        fontsize=34, fontweight="bold", color=PALETTE[0])
ax.text(0, -0.22, "完成率", ha="center", va="center", fontsize=14, color="#666666")
ax.set_title("目标完成率", fontsize=15, pad=12)
save(fig, "14_单值圆环图")
