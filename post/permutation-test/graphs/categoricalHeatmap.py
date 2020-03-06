import numpy as np
import matplotlib.pyplot as plt

def showCategoricalHeatmap(ySize_in, xSize_in, categoriesSize_in, title_in):
    # construct figure and axes
    fig = plt.figure(figsize=(ySize_in, xSize_in))
    ax = plt.subplot()

    im = ax.imshow(categoriesSize_in)

    # We want to show all ticks...
    ax.set_xticks(np.arange(len(list(categoriesSize_in))))
    ax.set_yticks(np.arange(len(categoriesSize_in.index)))
    # ... and label them with the respective list entries
    ax.set_xticklabels(list(categoriesSize_in))
    ax.set_yticklabels(categoriesSize_in.index)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

    
    # Loop over data dimensions and create text annotations.
    for plIn, plat in enumerate(categoriesSize_in):
        platforms = categoriesSize_in[plat]
        for caIn, cat in enumerate(platforms):
            text = ax.text(plIn, caIn, cat,
            ha="center", va="center", color="w")
    
    
    ax.set_title(title_in)
    fig.tight_layout()
    plt.show()
