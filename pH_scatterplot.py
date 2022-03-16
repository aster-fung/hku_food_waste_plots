
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('pH_profile_plot.csv', delimiter=';')
print(df.head(5))
#ax1 = sns.scatterplot(x='Digestion Hours (h)', y='pH', hue='consortium', data=df, palette='Set1')
#plt.legend(loc='upper left')
#plt.show()
#plt.savefig('veg_biomass_scatterplot_aster.png', dpi=300)
ax2 = sns.boxplot(x='Digestion Time (h)',y='pH', hue='consortium', width=0.4, flierprops = dict(marker='o', markersize=2),data=df, palette='Set1')
plt.legend(loc='upper left')
plt.show()
#plt.savefig('veg_biomass_scatterplot_aster_1.pdf', dpi=600)