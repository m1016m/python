# -*- coding: utf-8 -*-
"""
A433_10_01_Time_Series_20161114.py
Created on Mon Nov 14 09:48:30 2016

@author: zzjack
"""
#Date and Time Data Types and Tools
from datetime import datetime
now=datetime.now()
now #datetime.datetime(2016, 11, 14, 10, 51, 11, 277880)
now.year, now.month, now.day #(2016, 11, 14)
now.date() # datetime.date(2016, 11, 14)
now.time() # datetime.time(11, 21, 9, 75024)

#datetime stores both the date and time down to the microsecond.
#datetime.timedelta() represents the temporal difference between two datetime objects:
delta2=datetime(2016,11,14,12)-datetime(2016,11,14,10,30) #相差90分鐘
delta2 # datetime.timedelta(0, 5400),相差0天5400秒

#另一個例子:
delta3=datetime(2017,12,25)-datetime.now() #離耶誕節還有多久
delta3 #datetime.timedelta(108, 26697, 495440), 108天又26697秒又495440 microseconds
delta3.days #108天
delta3.second #又26697秒
delta3.microsecond #又495400 microseconds

#----timedelta object------------------------------------------------------
#A timedelta object represents a duration, 
#the difference between two dates or times.
#class datetime.timedelta()

from datetime import timedelta
#example1:
start=datetime(2016,1,1)
start+timedelta(10) #datetime.datetime(2016, 1, 11, 0, 0), 單位為day
start+timedelta(10,5400) #往後10天又5400秒, 注意!參數是day,second,microsecond
                         #datetime.datetime(2016, 1, 11, 1, 30), 5400秒-->1小時30分

#example2:
now=datetime.now() #datetime.now()
now #datetime.datetime(2016, 11, 14, 11, 29, 14, 11294)
now+timedelta(1) #1天後, datetime.datetime(2016, 11, 15, 11, 29, 14, 11294)
now-timedelta(3,5400) #往前3天又5400秒(1 hour 30 minutes)
                      #datetime.datetime(2016, 11, 11, 9, 59, 14, 11294)

#example3:
delta5=timedelta(7,7200) #delta5為 7天又兩小時(7200 sec)的時間差
now-3*delta5 #3倍delta5















