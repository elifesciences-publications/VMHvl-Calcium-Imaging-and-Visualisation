# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 17:10:20 2018

@author: Krzywy
"""
'''Short script generating Heatmaps showing fixed period before and after 
initaition of chosen bahaviour'''

import seaborn as sns
import numpy as np
import pandas as pd
Final = pd.read_csv('Path_to_dataframe_with calcium_trace_and_behaviour', delimiter=';')
events = []
#Set how many frames before and after behaviour start
val = np.arange(-40,40)
z = 0
e = 1
#select bahaviour of interest
prev = 'bahaviour_of_interest'
#loop creating a list of short dataframes containing chosed period of behaviour and calcium trace
for i in (Final['Beh'].iteritems()):
    if i[1] == 'Behaviour_of_interest' and i[1] != prev:
        Start = Final[z-40:z+40]
        Start.loc[:,'Frames'] = val
        Start.loc[:,'event'] = e
        events.append(Start)
        prev = i[1]
        z += 1  
        e += 1
        
    else:
        z += 1
        prev = i[1]
eventss = pd.DataFrame()
for i in events:
    event = pd.DataFrame(data=i)
    eventss = pd.concat([eventss, event])

#This part plots all events and it's mean as a heatmap
import matplotlib.pyplot as plt

m = eventss.groupby('Frames', as_index=False).mean()
m = m.iloc[:,1:-1].transpose()


ax = sns.clustermap(m, col_cluster=False)
ax = ax.ax_heatmap
ax.axvline(x=39, color='Black')
ax.set_title("bahviour x heatmap")
