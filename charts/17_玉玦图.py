"""17 玉玦图：环形放射条形（带缺口的圆环条形图）"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
from common import save, PALETTE

ages = ["[20,30)", "[30,40)", "[40,50)", ">=50"]
shares = [0.375, 0.2917, 0.2083, 0.125]   # 已按从大到小排序
colors = ["#2E75B6", "#5B9BD5", "#9DC3E6", "#C9DCF0"]

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, polar=True)
ax.set_theta_zero_location("N")   # 从正上方开始
ax.set_theta_direction(-1)        # 顺时针
ax.axis("off")

span = np.deg2rad(300)            # 每环最多铺 300°，留出 60° 缺口（玉玦之"玦"）
ring_w = 0.62                     # 环宽
gap = 0.35                        # 环间距
vmax = max(shares)

for i, (label, v) in enumerate(zip(ages, shares)):
    bottom = 1 + (len(ages) - 1 - i) * (ring_w + gap)   # 最大占比在最外环
    # 背景轨道
    ax.bar(0, ring_w, width=span, bottom=bottom,
           color="#EAEFF5", edgecolor="none")
    # 数值弧
    ang = v / vmax * span
    bar = ax.bar(0, ring_w, width=ang, bottom=bottom,
                 color=colors[i], edgecolor="none",
                 label=f"{label}  {v:.1%}")

# 右侧图例标注类别与占比
ax.legend(loc="center left", bbox_to_anchor=(1.08, 0.5),
          frameon=False, fontsize=12, handlelength=1.2)

ax.set_ylim(0, 1 + len(ages) * (ring_w + gap))
ax.set_title("用户年龄分布玉玦图", fontsize=15, pad=20)
save(fig, "17_玉玦图")
