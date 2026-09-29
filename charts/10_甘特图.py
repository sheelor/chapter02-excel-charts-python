"""10 甘特图：项目计划（含完成度）"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
from common import save, PALETTE

projects = ["制定计划", "方案设计", "资源调配", "第一阶段", "第二阶段", "第三阶段", "项目总结"]
starts = [datetime(2022, 3, 1), datetime(2022, 3, 13), datetime(2022, 3, 22),
          datetime(2022, 4, 2), datetime(2022, 4, 16), datetime(2022, 5, 11),
          datetime(2022, 5, 26)]
days = [11, 8, 10, 13, 24, 14, 7]
progress = [0.51, 0.32, 0.21, 0.85, 0.36, 0.68, 0.68]
done_days = [5.61, 2.56, 2.10, 11.05, 8.64, 9.52, 4.76]

fig, ax = plt.subplots(figsize=(10, 5.5))
y = np.arange(len(projects))[::-1]  # 第一个项目在最上方
start_nums = mdates.date2num(starts)

ax.barh(y, days, left=start_nums, height=0.55, color="#D6DCE4", zorder=3, label="计划工期")
ax.barh(y, done_days, left=start_nums, height=0.55, color=PALETTE[0], zorder=4, label="已完成")

for yi, p, s, d in zip(y, progress, start_nums, days):
    ax.text(s + d + 1, yi, f"{p:.0%}", va="center", fontsize=10, color=PALETTE[0])

ax.set_yticks(y)
ax.set_yticklabels(projects, fontsize=11)
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=2))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%m月%d日"))
ax.set_xlim(mdates.date2num(datetime(2022, 2, 25)), mdates.date2num(datetime(2022, 6, 15)))
ax.set_title("项目进度甘特图", fontsize=15, pad=12)
ax.legend(loc="upper right", frameon=False)
ax.grid(axis="x", ls="--", alpha=0.3)
ax.set_axisbelow(True)
for side in ("top", "right", "left"):
    ax.spines[side].set_visible(False)
save(fig, "10_甘特图")
