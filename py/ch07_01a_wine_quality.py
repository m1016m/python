# -*- coding: utf-8 -*-
"""
ch07_01a_wine_quality.py
Selection By Label
Created on Fri Feb 24 14:28:19 2017

@author: zzjack
"""
import pandas as pd
from pandas import DataFrame,Series
import numpy as np

#Selection By Label
df1 = pd.DataFrame(np.random.randn(5,4), columns=list('ABCD'),
                   index=pd.date_range('20160101',periods=5))

#DataFrame.loc[],以index切值 ['2016-01-02':'2016-01-04']　
df1.loc['2016-01-02':'2016-01-04']
#DataFrame.loc[],以 df1['A']>=0 計算的布林值 當index切值, 取 column ['A','B']
df1.loc[df1['A']>=0,['A','B']]

