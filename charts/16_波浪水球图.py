"""16 波浪水球图：多层波浪 + 渐变水面的水球图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.colors import LinearSegmentedColormap
from common import save

rate = 0.65

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect("equal")
ax.axis("off")

R = 1.0
ax.add_patch(Circle((0, 0), R + 0.07, fill=False, lw=3, color="#2E75B6"))
ax.add_patch(Circle((0, 0), R, facecolor="#EAF3FB", edgecolor="none"))

clip = Circle((0, 0), R, transform=ax.transData)

xx = np.linspace(-R, R, 600)
level = 2 * R * rate - R

# 渐变水体（在波浪之下整体着色）
cmap = LinearSegmentedColormap.from_list("water", ["#9DC3E6", "#2E75B6"])
grad = np.linspace(0, 1, 256).reshape(-1, 1)
im = ax.imshow(grad, cmap=cmap, origin="lower", aspect="auto",
               extent=(-R, R, -R, level), zorder=2)
im.set_clip_path(clip)

# 三层波浪，相位与透明度不同，营造涌动效果
for amp, phase, alpha, color in [
    (0.08, 0.0, 1.0, "#2E75B6"),
    (0.06, 1.6, 0.55, "#5B9BD5"),
    (0.05, 3.1, 0.35, "#9DC3E6"),
]:
    wave = level + amp * np.sin(2 * np.pi * xx / 0.8 + phase)
    coll = ax.fill_between(xx, -R, wave, color=color, alpha=alpha, zorder=3)
    coll.set_clip_path(clip)

ax.text(0, 0, f"{rate:.0%}", ha="center", va="center",
        fontsize=36, fontweight="bold", color="white", zorder=5)
ax.set_xlim(-1.28, 1.28)
ax.set_ylim(-1.28, 1.28)
ax.set_title("完成率波浪水球图", fontsize=15, pad=12)
save(fig, "16_波浪水球图")
