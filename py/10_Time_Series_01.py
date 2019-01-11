# -*- coding: utf-8 -*-
"""
10_Time_Series_01.py
"""
import pandas as pd
import numpy as np
#date_range(), 起始時間'2017/7/1', 週期 30, 單位 d (day)
exp_rng=pd.date_range('2017/7/1',periods=30,freq='d')

#產生一Series, 以exp_rng 為index
exp_data=pd.Series(np.random.randint(0,500,len(exp_rng)),index=exp_rng)
#
exp_data
exp_data.cumsum().plot()
