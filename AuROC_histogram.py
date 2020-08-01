# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 23:51:01 2018

@author: Krzywy
"""

'''This script generates AuROC histogram given dataframe containing AuROC scores and
boolean value indicating if socore is 3 sigma away from mean determined by bootstraping'''

#FinalHistauROC

import matplotlib as m
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

Final = pd.read_excel('Path_to_your_dataframe.xlsx')

#preapre 2 DF one with all AuROC scores for given behavior and second for 3sigma away from bootstraping mean
AllAuROC = Final.dropna()
Bootstrapped_AuROC = Final.loc[Final['BS'] == 1]

#graph part (historgams are overlapped last one 2 times for color saturation reasons)
sns.set_style('ticks')
bins = (0.01,0.04,0.07,0.1,0.13,0.16,0.19,0.22,0.25,0.28,0.31,0.34,0.37,0.4,0.43,0.46,0.49,0.52,0.55,0.58,0.61,0.64,0.67,0.7,0.73,0.76,0.79,0.82,0.85,0.88,0.91,0.94,0.97,1)
a = sns.distplot(AllAuROC['auROC'], bins=bins, kde=False, color=['grey'])
a.set(xlim=(0,1))
a.set(ylim=(0, 14))
plt.axvline(x=0.3501, color='grey', dashes=(3,1), linewidth=1.8)
#plt.text(0.32, 38.1,'0.35',rotation=0, fontsize=15, weight='bold')
plt.axvline(x=0.6499, color='grey', dashes=(3,1), linewidth=1.8)
#plt.text(0.62, 38.1,'0.65',rotation=0, fontsize=15, weight='bold')
a.axvline(linewidth=2, color='black') 
a.axhline(linewidth=2, color='black') 
a.spines['right'].set_visible(False)
a.spines['top'].set_visible(False)
a.set_xlabel('auROC', fontsize=25)
a.set_ylabel('Neuron count', fontsize=25)
a.tick_params(labelsize=25)
a = sns.distplot(Bootstrapped_AuROC['auROC'], bins=bins, kde=False, color=['sandybrown'])
a = sns.distplot(Bootstrapped_AuROC['auROC'], bins=bins, kde=False, color=['sandybrown'])

plt.show(a)
