# -*- coding: utf-8 -*-
"""
09_Aggregation_and_Group_04_20160919.py
Created on Wed Sep 14 21:10:23 2016

@author: zzjack
"""
#Grouping with Dicts and Series
import pandas as pd
from pandas import DataFrame,Series
import numpy as np
import matplotlib.pyplot as plt
# %pylab

#A final convenience for hierarchically-indexed data sets is the ability to aggregate using
#one of the levels of an axis index. To do this, pass the level number or name using the
#level keyword:

columns = pd.MultiIndex.from_arrays([['US', 'US', 'US', 'JP', 'JP'],
                                     [1, 3, 5, 1, 3]], names=['cty', 'tenor'])

hier_df = DataFrame(np.random.randn(4, 5), columns=columns)

hier_df
         
hier_df.groupby(level='cty', axis=1).count()






