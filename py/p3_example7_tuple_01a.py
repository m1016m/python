# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 15:43:47 2018
p3_example7_tuple_01a.py
@author: zzjack
"""
import csv

with open('kmrt3.txt','r') as fin:
    list_of_kmrt=[x for x in csv.reader(fin)]
    tuple_of_kmrt=tuple(list_of_kmrt[0])
   
tuple_of_kmrt    

