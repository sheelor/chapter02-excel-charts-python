"""28 复合柱形图：季度宽柱（背景） + 月度窄柱（前景）"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
from common import save, PALETTE, strip_axes

months = [f"{m}月" for m in range(1, 13)]
monthly = [2354, 1902, 3524, 2698, 2896, 2563, 3156, 2896, 3621, 2635, 2963, 2789]
# 对应 Excel 公式 =SUM(每 3 个月)
quarterly = [sum(monthly[i:i + 3]) for i in range(0, 12, 3)]

fig, ax = plt.subplots(figsize=(10, 5))
x = np.arange(12)
qx = np.arange(4) * 3 + 1  # 每季度中心位置

ax.bar(qx, quarterly, width=2.8, color="#D6DCE4", zorder=2, label="季度销量")
ax.bar(x, monthly, width=0.6, color=PALETTE[0], zorder=3, label="月度销量")

for xi, v in zip(x, monthly):
    ax.text(xi, v + 120, str(v), ha="center", va="bottom", fontsize=8.5)
for xi, v in zip(qx, quarterly):
    ax.text(xi, v + 160, str(v), ha="center", va="bottom", fontsize=10,
            fontweight="bold", color="#555555")

ax.set_xticks(x)
ax.set_xticklabels(months, fontsize=10)
ax.set_ylim(0, 11000)
ax.set_title("月度销量与季度销量复合柱形图", fontsize=15, pad=12)
ax.legend(frameon=False, loc="upper right")
ax.grid(axis="y", ls="--", alpha=0.3)
ax.set_axisbelow(True)
strip_axes(ax, keep=("left", "bottom"))
save(fig, "28_复合柱形图")
