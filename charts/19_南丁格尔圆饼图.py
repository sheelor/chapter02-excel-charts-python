"""19 南丁格尔圆饼图（玫瑰图）：各部门人数占比"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
from common import save

depts = ["销售部", "采购部", "工程部", "财务部", "行政部", "人力部"]
shares = [0.292, 0.227, 0.175, 0.136, 0.103, 0.067]
colors = ["#2E75B6", "#ED7D31", "#70AD47", "#FFC000", "#5B9BD5", "#997300"]

fig = plt.figure(figsize=(7.5, 7.5))
ax = fig.add_subplot(111, polar=True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
ax.axis("off")

n = len(depts)
width = 2 * np.pi / n
theta = np.arange(n) * width
radii = np.sqrt(shares) * 10      # 玫瑰图半径与数值平方根成正比，面积才代表占比

bars = ax.bar(theta, radii, width=width, bottom=0,
              color=colors, edgecolor="white", linewidth=1.5, alpha=0.9)

for t, r, label, v in zip(theta, radii, depts, shares):
    ax.text(t, r + 0.6, f"{label}\n{v:.1%}", ha="center", va="center", fontsize=11)

ax.set_ylim(0, max(radii) + 2.2)
ax.set_title("各部门人数占比南丁格尔圆饼图", fontsize=15, pad=22)
save(fig, "19_南丁格尔圆饼图")
