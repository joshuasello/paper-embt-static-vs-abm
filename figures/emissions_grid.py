"""Figure fig:emissions_grid: avoided well-to-wheel CO2 of the selected designs against the grid factor.

Avoided CO2 is a share of the diesel well-to-wheel CO2 of the electrified vehicles; it is linear
in the grid emission factor, so each line is drawn through its values at 0 and 0.906 kg CO2e/kWh.
M_A: mean (and standard error) over the ten fresh seeds, with the diesel counterfactual distance
from the travel logs of the five representation ICE runs. M_R: the replayed term weekdays, with
stranded vehicle-days kept diesel. Values from results/tables/synthesis/tab17_emissions.csv of
the emanalysis project embt_replay_vs_abm (src/synthesis/emissions.py; decisions D175 to D178,
finding F116), columns ma_avoided_pct, ma_avoided_se and mr_avoided_pct. Run with
    uv run --no-project --with matplotlib python emissions_grid.py
which writes emissions_grid.pdf and emissions_grid.png next to this script.
"""
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.legend_handler import HandlerTuple
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

OUT = Path(__file__).with_suffix("")

GRID_2023 = 0.906  # kg CO2e/kWh, South African grid 2023
BREAK_EVEN = 0.835  # grid factor at which an electric km emits as much as a diesel km

# Avoided CO2 (% of the EVs' diesel CO2) at grid factors 0 and 0.906: (at 0, at 0.906, SE at 0, SE at 0.906).
COMMUNITIES: dict[str, dict[str, Any]] = {
    "Khayelitsha": dict(colour="#2a78d6",
                        MA=dict(xR=(97.43, 13.59, 2.42, 2.43), xA=(100.39, 4.14, 2.28, 2.36)),
                        MR=dict(xR=(33.52, -2.86), xA=(35.40, -3.02))),
    "Bellville": dict(colour="#eb6834",
                      MA=dict(xR=(98.02, -5.97, 3.22, 3.35), xA=(104.07, -4.78, 3.17, 3.18)),
                      MR=dict(xR=(70.65, -6.04), xA=(60.94, -5.21))),
    "Wynberg": dict(colour="#1baf7a",
                    MA=dict(xR=(96.28, -11.67, 4.74, 5.07), xA=(96.72, -22.99, 5.13, 5.58)),
                    MR=dict(xR=(41.50, -3.55), xA=(21.72, -1.86))),
}

INK, MUTED, GRID, REPLAY = "#222222", "#6b6b6b", "#e6e6e6", "#8a8a8a"
STYLE = {"xA": "-", "xR": (0, (4, 2))}

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 7, "axes.labelsize": 7,
    "axes.edgecolor": INK, "axes.labelcolor": INK, "xtick.color": INK,
    "ytick.color": INK, "text.color": INK, "axes.linewidth": 0.6,
    "xtick.major.width": 0.6, "ytick.major.width": 0.6, "pdf.fonttype": 42,
})

g = np.linspace(0, 1, 101)


def line(at0: float, at906: float) -> np.ndarray:
    return at0 + (at906 - at0) * g / GRID_2023


fig, axes = plt.subplots(1, 3, figsize=(510 / 72, 2.75), sharey=True)
for ax, (name, c) in zip(axes, COMMUNITIES.items()):
    ax.axhline(0, color=INK, lw=0.6)
    ax.axvline(BREAK_EVEN, color=MUTED, lw=0.7, ls=(0, (1, 1.5)))
    ax.axvline(GRID_2023, color=INK, lw=0.7)
    for design in ("xR", "xA"):
        a0, a1, s0, s1 = c["MA"][design]
        y, se = line(a0, a1), line(s0, s1)
        ax.fill_between(g, y - 2 * se, y + 2 * se, color=c["colour"], alpha=0.13, lw=0)
        ax.plot(g, y, color=c["colour"], lw=1.4, ls=STYLE[design])
        ax.plot(g, line(*c["MR"][design]), color=REPLAY, lw=1.1, ls=STYLE[design])
    ax.set_title(name, fontsize=7)
    ax.set_xlim(0, 1)
    ax.set_ylim(-40, 115)
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1.0], ["0", "0.25", "0.5", "0.75", "1"])
    ax.grid(color=GRID, linewidth=0.5)
    ax.set_axisbelow(True)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
axes[0].set_ylabel("Avoided CO$_2$ (% of the EVs' diesel CO$_2$)")
axes[1].set_xlabel("Grid emission factor (kg CO$_2$e/kWh)")
axes[0].text(GRID_2023 + 0.015, 108, "2023", ha="left", va="top", fontsize=6, color=INK)
axes[0].text(BREAK_EVEN - 0.015, 108, "break-even\nwith diesel", ha="right", va="top", fontsize=6,
             color=MUTED)

handles = [
    Line2D([], [], color=INK, lw=1.3, ls=STYLE["xR"]),
    Line2D([], [], color=INK, lw=1.3, ls=STYLE["xA"]),
    (Patch(facecolor="#2a78d6", alpha=0.25), Line2D([], [], color="#2a78d6", lw=1.4)),
    Line2D([], [], color=REPLAY, lw=1.2),
]
labels = [r"$\mathbf{x}_R^\star$", r"$\mathbf{x}_A^\star$",
          r"$M_A$ ($\pm$ two standard errors; colour of the community)", r"$M_R$"]
fig.legend(handles, labels, handler_map={tuple: HandlerTuple(ndivide=1, pad=0)},
           loc="lower center", ncol=4, frameon=False, fontsize=7,
           bbox_to_anchor=(0.5, -0.01), handlelength=3.0, columnspacing=2.2)
fig.subplots_adjust(left=0.075, right=0.985, top=0.91, bottom=0.25, wspace=0.14)

fig.savefig(OUT.with_suffix(".pdf"))
fig.savefig(OUT.with_suffix(".png"), dpi=300)
print(OUT.with_suffix(".png"))
