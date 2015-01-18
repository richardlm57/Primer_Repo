'''
Created on 12/01/2015

@author: richard
'''

from decimal import Decimal
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
            if (tempA.hour<6 and tempB.hour>=6) or (tempA.hour<18 and tempB.hour>=18):
                totalRate+=max(self._day,self._night)
            else:
                if tempA.hour<6 or tempA.hour>=18:
                    totalRate+=self._night
                else:
                    totalRate+=self._day
            tempA=tempA+timedelta(hours=1)
        return totalRate

dateA=datetime(2015,7,5,5,56,0,0)
dateB=datetime(2015,7,5,7,57,0,0)

r=rate(Decimal(5),Decimal(7))
print(r.rateCompute(dateA,dateB))