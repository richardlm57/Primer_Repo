'''
Created on 19/01/2015

@author: richard
'''

import unittest
from rate import *

class testRate(unittest.TestCase):

    # Extremo: Mínimo tiempo, un minuto antes del cambio de tarifa nocturna a diurna

    def testDayNightChange1(self):
        
        myrate = rate(15,20)
        dateA = datetime(2015,7,5,5,44,0,0)
        dateB = datetime(2015,7,5,5,59,0,0)
        
        self.assertEqual(rateCompute(dateA, dateB, myrate), Decimal(20), "Pago incorrecto")
      
    # Extremo: Mínimo tiempo, un minuto antes del cambio de tarifa diurna a nocturna  
        
    def testDayNightChange2(self):
        
        myrate = rate(15,20)
        dateA = datetime(2015,7,5,17,44,0,0)
        dateB = datetime(2015,7,5,17,59,0,0)
        
        self.assertEqual(rateCompute(dateA, dateB, myrate), Decimal(15), "Pago incorrecto")
       
    # Extremo: Minimo tiempo, con cambio de tarifa nocturna a diurna
            
    def testDayNightChange3(self):
        
        myrate = rate(15,20)
        dateA = datetime(2015,7,5,5,45,0,0)
        dateB = datetime(2015,7,5,6,0,0,0)
        
        self.assertEqual(rateCompute(dateA, dateB, myrate), Decimal(20), "Pago incorrecto")
    
    # Extremo: Minimo tiempo, con cambio de tarifa diurna a nocturna  
        
    def testDayNightChange4(self):
        
        myrate = rate(15,20)
        dateA = datetime(2015,7,5,17,45,0,0)
        dateB = datetime(2015,7,5,18,0,0,0)
        
        self.assertEqual(rateCompute(dateA, dateB, myrate), Decimal(20), "Pago incorrecto")
        
    # Esquina: Fechas sobre el cambio de tarifa, excepto la de terminación (1 minuto antes del cambio) 
        
    def testBeforeRateChange(self):
        
        myrate = rate(15,20)
        dateA = datetime(2015,7,5,6,0,0,0)
        dateB = datetime(2015,7,5,17,59,0,0)
        
        self.assertEqual(rateCompute(dateA, dateB, myrate), Decimal(180), "Pago incorrecto")
        
    # Esquina: Fechas sobre el cambio de tarifa
        
    def testOnRateChange1(self):
        
        myrate = rate(15,20)
        dateA = datetime(2015,7,5,6,0,0,0)
        dateB = datetime(2015,7,5,18,0,0,0)
        
        self.assertEqual(rateCompute(dateA, dateB, myrate), Decimal(185), "Pago incorrecto")
      
    # Esquina: Fechas sobre el cambio de tarifa con 1 minuto más  
        
    def testOnRateChange2(self):
        
        myrate = rate(15,20)
        dateA = datetime(2015,7,5,6,0,0,0)
        dateB = datetime(2015,7,5,18,1,0,0)
        
        self.assertEqual(rateCompute(dateA, dateB, myrate), Decimal(205), "Pago incorrecto")
        
    # Extremo: Sobre el inicio de la tarifa diurna
        
    def testDay(self):
        
        myrate = rate(15,20)
        dateA = datetime(2015,7,5,6,0,0,0)
        dateB = datetime(2015,7,5,13,17,0,0)
        
        self.assertEqual(rateCompute(dateA, dateB, myrate), Decimal(120), "Pago incorrecto")
        
    # Extremo: Sobre el inicio de la tarifa nocturna
        
    def testNight(self):
        
        myrate = rate(15,20)
        dateA = datetime(2015,7,5,18,0,0,0)
        dateB = datetime(2015,7,6,4,17,0,0)
        
        self.assertEqual(rateCompute(dateA, dateB, myrate), Decimal(220), "Pago incorrecto")
        
    # Inválido: Tiempo menor al mínimo de tiempo
    
    def testLessThanMin(self):
        
        myrate = rate(15,20)
        dateA = datetime(2015,7,5,18,0,0,0)
        dateB = datetime(2015,7,5,18,10,0,0)
        
        self.assertRaises(AssertionError,rateCompute,dateA,dateB,myrate)
        
    def testGreaterThanMax(self):
        
        myrate = rate(15,20)
        dateA = datetime(2015,7,5,18,0,0,0)
        dateB = datetime(2015,7,8,18,10,0,0)
        
        self.assertRaises(AssertionError,rateCompute,dateA,dateB,myrate)