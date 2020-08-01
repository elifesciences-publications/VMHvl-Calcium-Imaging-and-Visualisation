# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 17:49:41 2019

@author: Krzywy
"""
'''This script creates venn diagram from previously pre-calculated overlaps'''

import matplotlib as m
import matplotlib.pyplot as plt
import matplotlib_venn as vplt
import seaborn as sns
 

sns.set_style('white')
#input number of neurons overlapping between 3 classes of choice (see venn3 documentation fro details).
v=vplt.venn3(subsets = (67, 23, 24, 63, 0, 10, 0), set_labels = ('Label 1', 'Label 2', 'label 3'))

#for t in v.set_labels: t.set_fontsize(20)
c=vplt.venn3_circles(subsets = (67, 23, 24, 63, 0, 10, 0), linestyle='dashed', linewidth=1, color="grey")
v.get_patch_by_id('100').set_color('lightsalmon')
v.get_patch_by_id('010').set_color('red')
v.get_patch_by_id('001').set_color('lightgrey')
v.get_patch_by_id('100').set_alpha(1)
v.get_patch_by_id('010').set_alpha(1)
v.get_patch_by_id('001').set_alpha(1)
for t in v.subset_labels: t.set_fontsize(18)
plt.show()
