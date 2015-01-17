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
        totalRate=0
        tempA=dateI
        while tempA<dateO:
            tempB=tempA+timedelta(hours=1)
            if (tempA.hour<6 and tempB.hour>6) or (tempA.hour<18 and tempB.hour>18):
                totalRate+=max(self._day,self._night)
            else:
                if tempA.hour<6 and tempA.hour>=18:
                    totalRate+=self._night
                else:
                    totalRate+=self._day
            tempA=tempA+timedelta(hours=1)
        print(totalRate)

dateA=datetime(2015,7,5,16,57,0,0)
dateB=datetime(2015,7,5,18,57,0,0)

r=rate(64,128)
r.rateCompute(dateA,dateB)