'''
Created on 12/01/2015

@author: richard
'''

from datetime import datetime
from datetime import timedelta

class rate():    
    def __init__(self,day,night):
        assert(day>0 and night>0)
        self._day=day
        self._night=night
    
    def rateCompute(self,dateI,dateO):
        assert(dateI<dateO)
        assert(dateO>=dateI+timedelta(minutes=15))
        assert(dateO<=dateI+timedelta(days=3))
        print("Listo, tío")
        totalH=(dateO-dateI)/3600
        temp=0
        if dateI.hour<6 and dateO.hour>6:
            temp=datetime(dateI.year,dateI.month,dateI.day,6,0,0,0)
        elif dateI.hour>18 and dateO.hour>6:
            temptemp=dateI+timedelta(days=1)
            temp=datetime(temptemp.year,temptemp.month,temptemp.day,6,0,0,0)
        elif dateI.hour<18 and dateO.hour>18:
            temp=datetime(dateI.year,dateI.month,dateI.day,18,0,0,0)
        partialH=(temp-dateI)/3600
dateA=datetime(2014,12,31,8,57,0,0)
dateB=datetime(2015,1,3,8,57,0,0)

r=rate(64,128)
r.rateCompute(dateA,dateB)