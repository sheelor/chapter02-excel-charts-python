"""通用绘图设置与工具函数。

所有图表脚本共用：中文字体、统一配色、渐变柱 / 圆角渐变柱、图片保存等。
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import FancyBboxPatch

# 中文字体回退列表（Windows / macOS / Linux 均可找到可用字体）
plt.rcParams["font.sans-serif"] = [
    "Microsoft YaHei", "PingFang SC", "Noto Sans CJK SC", "Noto Sans CJK JP",
    "WenQuanYi Zen Hei", "SimHei", "Arial Unicode MS",
]
plt.rcParams["axes.unicode_minus"] = False
# SVG 使用文字引用模式（体积更小，GitHub README 可直接渲染）
plt.rcParams["svg.fonttype"] = "none"
plt.rcParams["font.family"] = "sans-serif"

# 项目统一配色（贴近 Excel 商务配色）
PALETTE = ["#4472C4", "#ED7D31", "#A5A5A5", "#FFC000", "#5B9BD5", "#70AD47"]

IMG_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "images")
os.makedirs(IMG_DIR, exist_ok=True)


def save(fig, name):
    """同时保存 PNG（本地查看）与 SVG（矢量，可直接在 GitHub 渲染）"""
    for ext in ("png", "svg"):
        path = os.path.join(IMG_DIR, f"{name}.{ext}")
        fig.savefig(path, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
        print(f"已保存 -> {path}")
    plt.close(fig)


def gradient_bars(ax, x, heights, width, color=("#7F9CF5", "#2B4C9B")):
    """垂直渐变柱：imshow 渐变色带 + 矩形裁剪。color=(底部色, 顶部色)"""
    cmap = LinearSegmentedColormap.from_list("grad", list(color))
    grad = np.linspace(0, 1, 256).reshape(-1, 1)
    for xi, h in zip(x, heights):
        im = ax.imshow(grad, cmap=cmap, origin="lower", aspect="auto",
                       extent=(xi - width / 2, xi + width / 2, 0, h), zorder=3)
        clip = plt.Rectangle((xi - width / 2, 0), width, h)
        ax.add_patch(clip)
        clip.set_visible(False)
        im.set_clip_path(clip)


def rounded_gradient_bars(ax, x, heights, width, color=("#F8A5C2", "#C2185B"), rounding=0.10):
    """圆角垂直渐变柱：FancyBboxPatch 圆角矩形作为裁剪路径"""
    cmap = LinearSegmentedColormap.from_list("grad", list(color))
    grad = np.linspace(0, 1, 256).reshape(-1, 1)
    for xi, h in zip(x, heights):
        patch = FancyBboxPatch((xi - width / 2, 0), width, h,
                               boxstyle=f"round,pad=0,rounding_size={rounding}",
                               linewidth=0, facecolor="none")
        ax.add_patch(patch)
        im = ax.imshow(grad, cmap=cmap, origin="lower", aspect="auto",
                       extent=(xi - width / 2, xi + width / 2, 0, h), zorder=3)
        im.set_clip_path(patch)


def strip_axes(ax, keep=()):
    """隐藏多余边框，仅保留 keep 指定的边"""
    for side in ("top", "right", "left", "bottom"):
        ax.spines[side].set_visible(side in keep)
