"""15 水球图：圆形水波填充表示完成率 65%"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from common import save

rate = 0.65

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect("equal")
ax.axis("off")

R = 1.0
# 外圈
ax.add_patch(Circle((0, 0), R + 0.06, fill=False, lw=3, color="#5B9BD5"))
# 背景圆
bg = Circle((0, 0), R, facecolor="#EAF2FA", edgecolor="none")
ax.add_patch(bg)

# 波浪水面：正弦曲线以下区域填充
xx = np.linspace(-R, R, 500)
level = 2 * R * rate - R            # 水位高度（圆内 y 坐标）
wave = level + 0.07 * np.sin(2 * np.pi * xx / 0.9)
ax.fill_between(xx, -R, wave, color="#5B9BD5", zorder=3)

# 用圆形裁剪波浪
clip = Circle((0, 0), R, transform=ax.transData)
for coll in ax.collections:
    coll.set_clip_path(clip)

ax.text(0, 0, f"{rate:.0%}", ha="center", va="center",
        fontsize=36, fontweight="bold", color="#1F4E79", zorder=5)
ax.set_xlim(-1.25, 1.25)
ax.set_ylim(-1.25, 1.25)
ax.set_title("完成率水球图", fontsize=15, pad=12)
save(fig, "15_水球图")
