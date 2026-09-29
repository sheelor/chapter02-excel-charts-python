"""22 仪表盘图：270° 刻度仪表盘，指针指向当前数值 76"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge, Circle
from common import save

value, vmin, vmax = 76, 50, 150   # 指针数值与刻度范围（对应 Excel 数据）
TOTAL = 270                        # 表盘总角度
START = 135                        # 起始角（左下 225° 位置逆时针度量为 135°）

def val2ang(v):
    """数值 -> 表盘角度（度，逆时针从 +x 轴计）"""
    return START - (v - vmin) / (vmax - vmin) * TOTAL

fig, ax = plt.subplots(figsize=(7.5, 6.5))
ax.set_aspect("equal")
ax.axis("off")

R, w = 1.0, 0.22
zones = [(50, 90, "#70AD47"), (90, 120, "#FFC000"), (120, 150, "#C00000")]
for a, b, c in zones:
    ax.add_patch(Wedge((0, 0), R, val2ang(b), val2ang(a), width=w,
                       facecolor=c, edgecolor="white", lw=1.5))

# 刻度与标签
for v in range(vmin, vmax + 1, 10):
    ang = np.deg2rad(val2ang(v))
    r0, r1 = R - w - 0.04, R - w - 0.10
    ax.plot([r0 * np.cos(ang), r1 * np.cos(ang)],
            [r0 * np.sin(ang), r1 * np.sin(ang)], color="#555555", lw=1.2)
    ax.text((R + 0.10) * np.cos(ang), (R + 0.10) * np.sin(ang), str(v),
            ha="center", va="center", fontsize=10, color="#555555")

# 指针
ang = np.deg2rad(val2ang(value))
ax.plot([0, (R - w - 0.16) * np.cos(ang)], [0, (R - w - 0.16) * np.sin(ang)],
        color="#333333", lw=3.5, solid_capstyle="round", zorder=5)
ax.add_patch(Circle((0, 0), 0.05, color="#333333", zorder=6))

ax.text(0, -0.35, str(value), ha="center", va="center",
        fontsize=30, fontweight="bold", color="#2E75B6")
ax.text(0, -0.55, "当前指标值", ha="center", va="center", fontsize=12, color="#888888")
ax.set_xlim(-1.35, 1.35)
ax.set_ylim(-1.15, 1.35)
ax.set_title("指标仪表盘", fontsize=15, pad=12)
save(fig, "22_仪表盘图")
