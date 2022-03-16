# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pandas as pd
import matplotlib.pyplot as plt

oc_1 = [7.01, 7.02, 7.18, 8.05, 8.44]
c1_1 = [6.88,7.26, 7.64, 8.28, 8.40]
hours = [1,4,7,27,48]

oc_ph_hours = [[7.01, 1], [7.02,4], [7.18, 7], [8.05,27], [8.44,48]]
c1_ph_hours = [6.88,1], [7.26,4], [7.64, 7], [8.28,27], [8.40,48]
dfoc = pd.DataFrame(oc_ph_hours, columns = ['pH', 'hours'])
dfc1 = pd.DataFrame (c1_ph_hours, columns = ['pH','hours'])
df = dfoc.merge(dfc1, on="hours")
df.plot.scatter(x='hours', y='pH')
plt.show()