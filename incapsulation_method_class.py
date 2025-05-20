#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 20 12:16:43 2025

@author: ironman
"""
from uuid import uuid4

class Auto:
    __num_avto = 0
    def __init__(self, make, model, rang, yil, narh, km = 0):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()
        Auto.__num_avto +=1
        
    def get_km(self):
        return self.__km
    
    def get_id(self):
        return self.__id        
    
    def add_km(self, val):
        if val >= 0:
            self.__km += val
        else:
            print("Mashina kilometrini orqaga aylantirib bo`lmaydi")
            
    @classmethod
    def get_auto_num(cls):
        return cls.__num_avto
    
    def __str__(self): # print ishlatganda tushunarsiz bo`lmasligi uchun
        return f" Auto: {self.make} {self.model} {self.rang} {self.yil} {self.narh}"
    
    def __repr__(self): # __str__ga o`xshaydi, ammo yaxshiroq
        return f" Auto: {self.make} {self.model} {self.rang} {self.yil} {self.narh}"
    
    def __eq__(self, y):
        return self.narh == y.narh
    
    def __lt__(self, y):
        return self.narh < y.narh
    
        
        
    
avto1 = Auto("GM", "Gentra", "oq", "2016", "$18000", 36000)
avto2 = Auto("GM", "cobalt", "qora", "2024", "$19000", 9000)
print(avto1)


