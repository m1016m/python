# -*- coding: utf-8 -*-
#report2.py, import 模組時使用別名
import random #import standart module 'random'
def get_description():
    possibilities=['rain','snow','sum','who knows']
    return random.choice(possibilities)