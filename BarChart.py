# data from https://allisonhorst.github.io/palmerpenguins/

import matplotlib.pyplot as plt
import numpy as np

Plastics = ("PLA", "BPA-PC", "PET")
conversion_stats = {
    'Monomer Yield': (99,97,95),
    'Monomer Yield w/o DMAc': (21,87,5.2),
    'Conversion Time': (3.2,0.6,3.3),
    'Conversion time w/o DMAc':(17,11,92),
}
x = np.arange(len(Plastics))  # the label locations
width = 0.15  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='constrained')
count = 0
colors = ["#238934","#4378AC","#F0657A","#A93379"]
for attribute, measurement in conversion_stats.items():
    print(attribute)
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute,color = colors[count])
    ax.bar_label(rects, padding=3,fontsize = "18")
    multiplier += 1
    count = count+1


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Conversion Time(Hours)',fontsize = "18")
ax.set_title('')
ax.set_xticks(x + width, Plastics,fontsize = "18")
ax.legend(loc='upper left', ncols=3,fontsize = "18")
ax.set_ylim(0, 115)
secax = ax.secondary_yaxis('right')
secax.set_ylim(0,115)
secax.set_ylabel('Monomer Yield by 1HNMR(%)',fontsize = "18")
plt.show()