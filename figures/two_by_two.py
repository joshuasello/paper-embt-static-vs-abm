"""Figure fig:two_by_two: the selected designs (a) and their outcomes in both models (b).

Values from tab:two_by_two (main.tex) and tab:hubs (appendix.tex). Run with
    uv run --no-project --with matplotlib python two_by_two.py
which writes two_by_two.pdf and two_by_two.png next to this script.
"""
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerTuple
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

OUT = Path(__file__).with_suffix("")

COMMUNITIES: dict[str, dict[str, Any]] = {
    "Khayelitsha": dict(
        colour="#2a78d6", hubs=("Rank", "Terminus", "Stop"), bound=(20, 8, 6),
        xR=(3, 1, 1), xA=(5, 6, 2), kW=(250, 650),
        stranded=(0.570, 0.551), dev=(-0.181, -0.061), se=(0.004, 0.004),
        diff=-0.119, cost_xy=(0.462, -12.5), cost_ha="left"),
    "Bellville": dict(
        colour="#eb6834", hubs=("Rank", "Stop", "Terminus"), bound=(8, 12, 4),
        xR=(1, 3, 0), xA=(0, 4, 0), kW=(200, 200),
        stranded=(0.226, 0.329), dev=(-0.069, -0.034), se=(0.005, 0.009),
        diff=-0.035, cost_xy=(0.728, -9.0), cost_ha="center"),
    "Wynberg": dict(
        colour="#1baf7a", hubs=("Terminus", "Rank", "Station"), bound=(4, 4, 6),
        xR=(1, 1, 0), xA=(2, 0, 0), kW=(100, 100),
        stranded=(0.490, 0.673), dev=(-0.264, -0.161), se=(0.008, 0.006),
        diff=-0.103, cost_xy=(0.395, -24.0), cost_ha="center"),
}

INK, MUTED, GRID = "#222222", "#6b6b6b", "#e6e6e6"
YMAX = 9
DIAMOND_AREA, STAR_AREA = 45, 120  # marker areas (pt^2); a star covers less of its box

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 7, "axes.labelsize": 7,
    "axes.edgecolor": INK, "axes.labelcolor": INK, "xtick.color": INK,
    "ytick.color": INK, "text.color": INK, "axes.linewidth": 0.6,
    "xtick.major.width": 0.6, "ytick.major.width": 0.6, "hatch.linewidth": 0.6,
    "pdf.fonttype": 42,
})

fig = plt.figure(figsize=(510 / 72, 3.15))
gs = fig.add_gridspec(1, 2, width_ratios=(1.05, 1), wspace=0.26)
gs_a = gs[0].subgridspec(1, 3, wspace=0.12)

# (a) Connectors per hub: x_R hatched outline, x_A solid; the 2N-hat bound as a dashed tick.
axes_a = [fig.add_subplot(gs_a[i]) for i in range(3)]
w = 0.36
abbrev = {"Terminus": "Term.", "Station": "Stn."}
for ax, (name, c) in zip(axes_a, COMMUNITIES.items()):
    for i in range(3):
        ax.bar(i - w / 2 - 0.01, c["xR"][i], w, facecolor="white",
               edgecolor=c["colour"], hatch="////", linewidth=0.8)
        ax.bar(i + w / 2 + 0.01, c["xA"][i], w, color=c["colour"])
        b = c["bound"][i]
        if b <= YMAX:
            ax.hlines(b, i - 0.42, i + 0.42, color=INK, lw=0.9, ls=(0, (2.2, 1.4)))
        else:
            # Off the scale: an arrow at the top edge with the bound as a label.
            ax.annotate(str(b), xy=(i, YMAX), xytext=(i, YMAX - 1.15), ha="center",
                        va="center", fontsize=6, color=INK,
                        arrowprops=dict(arrowstyle="-|>", color=INK, lw=0.8,
                                        mutation_scale=6, shrinkA=3, shrinkB=0))
    ax.set_xticks(range(3), [f"{i + 1}\n{abbrev.get(t, t)}" for i, t in enumerate(c["hubs"])],
                  fontsize=6)
    ax.set_xlim(-0.6, 2.6)
    ax.set_ylim(0, YMAX)
    ax.set_yticks(range(0, YMAX + 1, 2))
    ax.grid(axis="y", color=GRID, linewidth=0.5)
    ax.set_axisbelow(True)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.set_title(name, fontsize=7, pad=13)
    kr, ka = c["kW"]
    ax.text(0.5, 1.01, f"{kr} → {ka} kW", transform=ax.transAxes,
            ha="center", va="bottom", fontsize=6, color=MUTED)
    if ax is not axes_a[0]:
        ax.tick_params(labelleft=False)
axes_a[0].set_ylabel("Connectors (50 kW)")
axes_a[1].set_xlabel("Candidate hub")
axes_a[0].text(-0.45, 1.12, "(a)", transform=axes_a[0].transAxes, fontweight="bold", fontsize=8)

# (b) Each design in both models; the cost of x_R by each arrow.
ax = fig.add_subplot(gs[1])
for name, c in COMMUNITIES.items():
    ns = [1 - s for s in c["stranded"]]
    dev = [100 * d for d in c["dev"]]
    ax.annotate("", xy=(ns[1], dev[1]), xytext=(ns[0], dev[0]),
                arrowprops=dict(arrowstyle="-|>", color=c["colour"], lw=1.3,
                                shrinkA=7, shrinkB=9, mutation_scale=8))
    for j in range(2):
        ax.errorbar(ns[j], dev[j], yerr=200 * c["se"][j], fmt="none",
                    ecolor=c["colour"], elinewidth=0.8, capsize=0, zorder=2)
    ax.scatter(ns[0], dev[0], s=DIAMOND_AREA, marker="D", facecolor="white",
               edgecolor=c["colour"], linewidth=1.3, zorder=3)
    ax.scatter(ns[1], dev[1], s=STAR_AREA, marker="*",
               facecolor=c["colour"], edgecolor="white", linewidth=0.5, zorder=3)
    ax.text(ns[1], dev[1] + 2.4, name, ha="center", va="bottom", fontsize=7, color=INK)
    ax.text(*c["cost_xy"], f"{-100 * c['diff']:.1f} pp", ha=c["cost_ha"], va="center",
            fontsize=6.5, color=INK)

ax.set_xlim(0.25, 0.85)
ax.set_ylim(-30, 2)
ax.set_xlabel(r"Vehicle-days not stranded in $M_R$ (share)")
ax.set_ylabel(r"EV passenger change in $M_A$ (%)")
ax.grid(color=GRID, linewidth=0.5)
ax.set_axisbelow(True)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
ax.text(0.84, -29.3, "better in $M_R$ →", ha="right", va="bottom", fontsize=6, color=MUTED)
ax.text(0.26, 1.4, "↑ better in $M_A$", ha="left", va="top", fontsize=6, color=MUTED)
ax.text(-0.17, 1.12, "(b)", transform=ax.transAxes, fontweight="bold", fontsize=8)

handles = [
    (Patch(facecolor="white", edgecolor=MUTED, hatch="////"),
     Line2D([], [], marker="D", ls="", mfc="white", mec=MUTED, mew=1.2, ms=5)),
    (Patch(facecolor=MUTED),
     Line2D([], [], marker="*", ls="", mfc=MUTED, mec="white", ms=9)),
    Line2D([], [], color=INK, lw=0.9, ls=(0, (2.2, 1.4))),
]
labels = [r"$\mathbf{x}_R^\star$, selected by the replay model",
          r"$\mathbf{x}_A^\star$, selected by the agent-based model",
          r"Connector bound $2\hat{N}_j$"]
fig.legend(handles, labels, handler_map={tuple: HandlerTuple(ndivide=None, pad=0.8)},
           loc="lower center", ncol=3, frameon=False, fontsize=7,
           bbox_to_anchor=(0.5, -0.01), handlelength=3.2, columnspacing=2.5)
fig.subplots_adjust(left=0.07, right=0.99, top=0.85, bottom=0.26)

fig.savefig(OUT.with_suffix(".pdf"))
fig.savefig(OUT.with_suffix(".png"), dpi=300)
print(OUT.with_suffix(".png"))
