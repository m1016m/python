# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 11:55:19 2018
A_ch10_001_coin.py
"""
import numpy as np
import pandas as pd
import matplotlib.pylab as plt

results=[] #empty list "results"
for throws_num in range(1,10001):
    throws=np.random.randint(low=0,high=2,size=throws_num)
    probability_of_throws=throws.sum() / throws_num
    results.append(probability_of_throws)

#將list "results" 轉成 DataFrame "df"
df=

