# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pandas as pd
import matplotlib.pyplot as plt

oc_1 = [] # raw data censored
c1_1 = [] # raw data censored
hours = [1,4,7,27,48]

oc_ph_hours = [] # raw data censored
c1_ph_hours = [] # raw data censored
dfoc = pd.DataFrame(oc_ph_hours, columns = ['pH', 'hours'])
dfc1 = pd.DataFrame (c1_ph_hours, columns = ['pH','hours'])
df = dfoc.merge(dfc1, on="hours")
df.plot.scatter(x='hours', y='pH')
plt.show()
