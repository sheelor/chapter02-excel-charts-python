"""20 南丁格尔圆环图：年龄分布（带内孔的玫瑰图）"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
from common import save

ages = ["[20,30)", "[30,40)", "[40,50)", ">=50"]
shares = [0.375, 0.2917, 0.2083, 0.125]
colors = ["#2E75B6", "#5B9BD5", "#9DC3E6", "#C9DCF0"]

fig = plt.figure(figsize=(7.5, 7.5))
ax = fig.add_subplot(111, polar=True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
ax.axis("off")

n = len(ages)
width = 2 * np.pi / n
theta = np.arange(n) * width
inner = 2.2                                    # 内孔半径
radii = np.sqrt(shares) * 10                   # 半径取平方根，面积代表占比

ax.bar(theta, radii, width=width, bottom=inner,
       color=colors, edgecolor="white", linewidth=1.5, alpha=0.92)

for t, r, label, v in zip(theta, radii, ages, shares):
    ax.text(t, inner + r + 0.7, f"{label}\n{v:.1%}",
            ha="center", va="center", fontsize=12)

ax.text(0, 0, "年龄\n分布", ha="center", va="center", fontsize=16,
        fontweight="bold", color="#2E75B6")
ax.set_ylim(0, inner + max(radii) + 2.4)
ax.set_title("用户年龄分布南丁格尔圆环图", fontsize=15, pad=22)
save(fig, "20_南丁格尔圆环图")
