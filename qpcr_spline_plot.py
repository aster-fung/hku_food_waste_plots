import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('qpcr_3set.csv', delimiter=',')
print(df.head(5))
ax1 = sns.lineplot(x="Digestion Time(hours)", y="Log CFU/mg biomass on biocarrier",
                   hue= "Species-consortium",data=df, err_style="bars",ci="sd", 
                   palette="Set1", markers=True, style="Species-consortium",
                   dashes=False)
ax1.legend(loc="upper right", fontsize=8, fancybox=False)
ax1.set_ylim(0,4)
ax2 = plt.gcf()
plt.draw()
ax2.savefig("qpcr_redo.tiff", dpi=500)


'''
https://www.dataforeverybody.com/seaborn-legend-change-location-size/
'''
