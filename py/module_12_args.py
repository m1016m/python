# -*- coding: utf-8 -*-
"""
module_12_args.py
@author: zzjack
"""
import sys
for s in sys.argv: #sys.argv 是一個list
    print(s)
    
print('total argv:',len(sys.argv)) #*argv 包含程式本身    
