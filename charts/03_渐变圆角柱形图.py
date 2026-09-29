"""03 渐变圆角柱形图：商品销量"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
from common import save, rounded_gradient_bars, strip_axes

items = ["口红", "面膜", "隔离", "防晒", "精华", "面霜"]
sales = [653, 523, 648, 856, 714, 785]

fig, ax = plt.subplots(figsize=(8, 5))
x = np.arange(len(items))
rounded_gradient_bars(ax, x, sales, width=0.45,
                      color=("#F6C1D9", "#C2185B"), rounding=0.09)

for xi, v in zip(x, sales):
    ax.text(xi, v + 20, str(v), ha="center", va="bottom", fontsize=11)

ax.set_xticks(x)
ax.set_xticklabels(items, fontsize=11)
ax.set_ylim(0, 950)
ax.set_title("商品销量", fontsize=15, pad=12)
ax.grid(axis="y", ls="--", alpha=0.3)
ax.set_axisbelow(True)
strip_axes(ax, keep=("left", "bottom"))
save(fig, "03_渐变圆角柱形图")
