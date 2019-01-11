# -*- coding: utf-8 -*-
"""
ch12_ALS_52.py

@author: zzjack
"""
import pandas as pd

df1=pd.read_csv('u.data',names=['user_id','item_id','rating','timestamp'],
                delimiter='\t')
                
