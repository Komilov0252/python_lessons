#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 20 10:30:38 2025

@author: ironman
"""
import os

print(os.getcwd())

from Talaba_class import Talaba


talaba1 = Talaba("Abrorbek", "Komilov", 2002)
talaba2 = Talaba("Sarvar", "Eshniyozov", 2003)
talaba3 = Talaba("Hafiza", "Amirova", 2001)

class Fan:
    def __init__(self, nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []
        
    def add_student(self, student):
        self.talabalar.append(student)
        self.talabalar_soni += 1
    
    def get_students(self):
        return [x.tanishtir() for x in self.talabalar]
    
    def see_method(self, v):
        return [i for i in dir(v) if not i.startswith('__') ]

matem = Fan('Oliy matematika')
matem.add_student(talaba1)
matem.add_student(talaba2)
matem.add_student(talaba3)


        

