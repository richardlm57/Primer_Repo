'''
Created on Jan 18, 2015

@author: Patty
'''

import unittest
from rate import *
from decimal import Decimal
from datetime import datetime
from datetime import timedelta


class testRate(unittest.TestCase):
    
    def testAnyDate(self):
        self.assertEqual(rateCompute(datetime(2015,7,5,5,56,0,0), datetime(2015,7,5,7,57,0,0), rate(15,20)), 50)
        
        
    # Extremos en la salida
    
    # Pago minimo: Tiempo minimo durante el momento del dia con la tarifa mas barata
    
    def testMinPay(self):
        
        myrate = rate(15,20)
        dateA = datetime(2015,7,5,7,25,0,0)
        dateB = datetime(2015,7,5,7,40,0,0)
        
        self.assertEqual(rateCompute(dateA, dateB, myrate), 15, "Pago minimo incorrecto")
    
    # Pago maximo: Tiempo maximo (3 dias) independiente de la hora de entrada
        
    def testMaxPay(self):
        
        myrate = rate(15,20)
        dateA = datetime(2015,7,5,19,25,0,0)
        dateB = datetime(2015,7,8,19,25,0,0)
        
        self.assertEqual(rateCompute(dateA, dateB, myrate), 15*33 + 20*33 + 6*20, "Pago maximo incorrecto")
        
    
    # Extremos en la entrada
    
    # Minimo de la entrada
    
    # Minimo tiempo (15 min) durante el dia
    
    def testMinTimeDay(self):
    
        myrate = rate(15,20)
        dateA = datetime(2015,7,5,7,25,0,0)
        dateB = datetime(2015,7,5,7,40,0,0)
        
        self.assertEqual(rateCompute(dateA, dateB, myrate), 15, "Pago de tiempo minimo incorrecto")
    
    # Minimo tiempo (15 min) durante la noche
    
    def testMinTimeNight (self):
    
        myrate = rate(15,20)
        dateA = datetime(2015,7,5,20,25,0,0)
        dateB = datetime(2015,7,5,20,40,0,0)
                
        self.assertEqual(rateCompute(dateA, dateB, myrate), 20, "Pago de tiempo minimo incorrecto")
    
    # Minimo tiempo (15 min) entre el dia y la noche
    
    
    def testMinTimeDayNight1(self):
    
        myrate = rate(15,20)
        dateA = datetime(2015,7,5,5,55,0,0)
        dateB = datetime(2015,7,5,6,10,0,0)
        
        self.assertEqual(rateCompute(dateA, dateB, myrate), 20, "Pago de tiempo minimo incorrecto")

    
    def testMinTimeDayNight2(self):
    
        myrate = rate(20,15)
        dateA = datetime(2015,7,5,5,55,0,0)
        dateB = datetime(2015,7,5,6,10,0,0)
        
        self.assertEqual(rateCompute(dateA, dateB, myrate), 20, "Pago de tiempo minimo incorrecto")
        
        
    def testMinTimeDayNight3(self):
    
        myrate = rate(15,20)
        dateA = datetime(2015,7,5,17,55,0,0)
        dateB = datetime(2015,7,5,18,10,0,0)
        
        self.assertEqual(rateCompute(dateA, dateB, myrate), 20, "Pago de tiempo minimo incorrecto")

    
    def testMinTimeDayNight4(self):
    
        myrate = rate(20,15)
        dateA = datetime(2015,7,5,17,55,0,0)
        dateB = datetime(2015,7,5,18,10,0,0)
        
        self.assertEqual(rateCompute(dateA, dateB, myrate), 20, "Pago de tiempo minimo incorrecto")

    def testMinTimeDayNight5(self):
    
        myrate = rate(7 ,5)
        dateA = datetime(2015,7,5,5,44,0,0)
        dateB = datetime(2015,7,5,5,59,0,0)
        
        self.assertEqual(rateCompute(dateA, dateB, myrate), 5, "Pago de tiempo minimo incorrecto")

