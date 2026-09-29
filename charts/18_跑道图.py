"""18 跑道图：各部门人数（半圆环跑道）"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
from common import save

depts = ["销售部", "采购部", "工程部", "财务部", "行政部", "人力部"]
counts = [451, 326, 293, 238, 226, 130]
colors = ["#C00000", "#ED7D31", "#FFC000", "#70AD47", "#5B9BD5", "#4472C4"]

fig = plt.figure(figsize=(9, 5.5))
ax = fig.add_subplot(111, polar=True)
ax.set_theta_zero_location("W")   # 0° 指向左侧
ax.set_theta_direction(-1)        # 顺时针
ax.set_thetamin(0)                # 只保留上半圆
ax.set_thetamax(180)
ax.axis("off")

ring_w = 0.6
gap = 0.4
vmax = max(counts)

for i, (label, v) in enumerate(zip(depts, counts)):
    bottom = 1 + (len(depts) - 1 - i) * (ring_w + gap)
    ax.bar(0, ring_w, width=np.pi, bottom=bottom,
           color="#EFF2F6", edgecolor="none")                    # 跑道底色
    arc = v / vmax * np.pi
    ax.bar(0, ring_w, width=arc, bottom=bottom,
           color=colors[i], edgecolor="none",
           label=f"{label} {v}人")                               # 实际弧

# 右侧图例标注部门与人数
ax.legend(loc="center left", bbox_to_anchor=(1.02, 0.5),
          frameon=False, fontsize=12, handlelength=1.2)

ax.set_ylim(0, 1 + len(depts) * (ring_w + gap))
ax.set_title("各部门人数跑道图", fontsize=15, pad=20)
save(fig, "18_跑道图")
