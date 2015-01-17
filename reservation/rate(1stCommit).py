'''
Created on 12/01/2015

@author: richard
'''

import datetime
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
        
dateA=datetime.datetime(2014,12,31,8,57,0,0)
dateB=datetime.datetime(2015,1,3,8,57,0,0)

r=rate(64,128)
r.rateCompute(dateA,dateB)
