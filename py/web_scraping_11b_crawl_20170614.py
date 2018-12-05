# -*- coding: utf-8 -*-
"""
web_scraping_11b_crawl_20170614.py
python recursive function 說明範例
Created on Wed Jun 14 22:48:55 2017

@author: zzjack
"""
#n! = n * (n-1)!, if n > 1 and 1! = 1, f(n)=n*f(n-1) if n>1 and f(1)=1
#example: 4!=4*3!
#         3!=3*2!
#         2!=2*1
#                4!=4*3*2*1

#def function factorial()
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
#4! factorial(4)
r=factorial(4)
r

