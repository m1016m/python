# -*- coding: utf-8 -*-
"""
07_Data_Wrangling_07_20170109.py
Created on Mon Jan  9 15:48:29 2017
@author: zzjack
"""
#Import Conventions
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
from pandas import DataFrame,Series

#Reshaping with Hierarchical Indexing
#stack / unstack

data=DataFrame(np.arange(6).reshape(2,3),
               index=pd.Index(['高雄','台北'],name='都'),
               columns=pd.Index(['一','二','三'],name='區'))
              
#Using the stack method: -->結果是一個具層次化索引的 Series
stack_result=data.stack()
stack_result

type(stack_result) #pandas.core.series.Series

#From a hierarchically-indexed Series, you can rearrange the data back into a DataFrame
#with unstack:
stack_result.unstack()

#stack/unstack 預設是以最內層操作 (level=-1)
stack_result
stack_result.unstack() #預設是 -1
stack_result.unstack(-1)
stack_result.unstack(0) #改為 level=0

