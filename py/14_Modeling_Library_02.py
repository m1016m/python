# -*- coding: utf-8 -*-
"""
14_Modeling_Library_02.py
"""
import pandas as pd
import numpy as np

#create DataFrame data
data = pd.DataFrame({
             'x0': [1, 2, 3, 4, 5],
             'x1': [0.01, -0.01, 0.25, -4.1, 0.],
             'y': [-1.5, 0., 3.6, 1.3, -2.]})

data #display 

#import patsy
import patsy
#patsy.dmatrices(), patsy’s formulas: y ~ x0 + x1
y, X = patsy.dmatrices('y ~ x0 + x1', data)
y #DesignMatrix with shape (5, 1)
X #DesignMatrix with shape (5, 3)
