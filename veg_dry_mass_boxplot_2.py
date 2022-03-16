# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 15:29:40 2020

@author: Aster
"""


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('veg_dry_mass.csv', delimiter=';')
print(df.head(5))
ax1 = sns.boxplot(x='Digestion Time (h)',y='Biomass(mg)', hue='consortium', width = 0.4, flierprops = dict(marker='o', markersize = 2),data= df, palette='Set1')
plt.ylim(0,80)
plt.legend(loc='upper left')
plt.show()
#plt.savefig('veg_biomass_boxplot_aster.pdf', dpi=300)
ax2 = sns.catplot(x='Digestion Time (h)',y='Biomass(mg)', hue='consortium', data= df, palette='Set1')
plt.show()
#plt.savefig('veg_biomass_catplot_aster.pdf', dpi=300)
