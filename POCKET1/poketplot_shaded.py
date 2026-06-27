#!/usr/bin/env python
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
import numpy as np



plt.rcParams.update({

    "font.size": 24,
    "axes.labelsize": 24,
    "axes.titlesize": 22,

    "xtick.labelsize": 18,
    "ytick.labelsize": 18,

    "legend.fontsize": 20,

    #"axes.linewidth": 1.5,

    "xtick.major.width": 2.5,
    "ytick.major.width": 2.5,

    "xtick.major.size": 8,
    "ytick.major.size": 8,

    "font.family": "sans-serif"
})



colors = {
    "WT": "limegreen",
    "ATP": "crimson",
    "CRYO": "cornflowerblue",
}

display_names = {
    "WT": "ATP-",
    "ATP": "ATP+out",
    "CRYO": "ATP+",
}


df = pd.read_csv("all_pocket_volumes.csv")

df = df.dropna(subset=["volume_A3"])



plt.figure(figsize=(7, 5))

for label, group in df.groupby("type"):

    volumes = group["volume_A3"].values

    kde = gaussian_kde(volumes)

    x = np.linspace(
        volumes.min(),
        volumes.max(),
        500
    )

    y = kde(x)

    color = colors.get(label, "black")

    plt.plot(
        x,
        y,
        color=color,
        linewidth=3.5,
        label=display_names.get(label, label)
    )

    plt.fill_between(
        x,
        y,
        color=color,
        alpha=0.25
    )



plt.xlabel(
    r"Volume ($\mathrm{\AA^3}$)",
    fontsize=28
)

plt.ylabel(
    "Probability density",
    fontsize=28
)

plt.title(
    "Pocket1 volume distribution",
    fontsize=22
)



plt.tick_params(
    axis="both",
    labelsize=18,
    direction="in",
    length=8,
    width=2.0
)


plt.legend(
    frameon=False,
    fontsize=20
)


plt.tight_layout()

plt.savefig(
    "pocket_volume_density.png",
    dpi=600,
    bbox_inches="tight"
)

plt.savefig(
    "pocket_volume_density.pdf",
    bbox_inches="tight"
)

plt.show()
