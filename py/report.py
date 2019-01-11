# -*- coding: utf-8 -*-
# module reprot.py, 從python 標準隨機模組(random)匯入choice函數 
def get_description(): #定義 get_description() 
    """Return random weather""" #function 說明文件
    from random import choice #from std. module 'random' import method choice(self,seq)
    possibilities=['下雨','下雪','颳風','起霧','大太陽','天曉得']
    return choice(possibilities)
# 另一種import寫法
#  import random
#  ...
#  retrun random.choice(...)
import random # import module random,匯入整個 random 模組,使用時 random.choice() 
def get_description2(): #定義 get_description2()
    'Return random weather 2'
    possibilities2=['下雨','下雪','颳風','起霧','大太陽','天曉得']
    return random.choice(possibilities2)