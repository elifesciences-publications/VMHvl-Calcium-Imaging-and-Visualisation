# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 18:52:30 2020

@author: Krzywy
"""
'''This script takes dataframe with positions of each recording frame(point in LDA graph) in 
LDA space and calculates distances between  all points within and between clusters'''


import numpy as np
import pandas as pd
from scipy.spatial.distance import pdist
from scipy.spatial.distance import cdist


dis = pd.read_csv(r'Path_to_the dataframe', index_col=0)
dis.rename(columns={'0':'dist'}, inplace=True)
#Separeate the 2 clusters into two dataframes
dis1 = dis.loc[dis['target'] == 'F1']
dist1 = dis1['dist'].values
dist1 = dist1.reshape(-1, 1)

dis2 = dis.loc[dis['target'] == 'F2']
dist2 = dis2['dist'].values
dist2 = dist2.reshape(-1, 1)

#calculate distances between points within and between clusters.
distances1 = pdist(dist1, 'cityblock')
Meandist1 = distances1.mean()

distances2 = pdist(dist2, 'cityblock')
Meandist2 = distances2.mean()

distances12 = cdist(dist1, dist2, 'cityblock')
Meandist12 = np.mean(distances12)

import csv
with open(r'Path_to_write_output_file', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Meandist1', Meandist1])
    spamwriter.writerow(['Meandist2', Meandist2])
    spamwriter.writerow(['Meandist12', Meandist12])


"""Version for data from context recordings"""
dis = pd.read_csv(r'Path_to_dataframe_.csv', index_col=0)
dis.rename(columns={'0':'X', '1':'Y'}, inplace=True)
home = dis.loc[dis['Loc'] == 1]
corr = dis.loc[dis['Loc'] == 2]
far = dis.loc[dis['Loc'] == 3]

home_corr = cdist(home, corr, 'euclidean')
Mean_h_c = home_corr.mean()

home_far = cdist(home, far)
Mean_h_f = home_far.mean()

far_corr = cdist(far, corr)
Mean_f_c = far_corr.mean()


