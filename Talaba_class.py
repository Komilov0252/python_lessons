#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 20 09:39:12 2025

@author: ironman
"""

class Talaba:
    def __init__(self, first_name, last_name, birth_dt):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_dt = birth_dt
        self.bosqich = 4
        
    def tanishtir(self):
        return(f"{self.first_name} {self.last_name} {2025 - self.birth_dt} yosh ")
    
    def get_age(self, dt):
        return dt - self.birth_dt
    
    def get_bosqich(self):
        return self.bosqich
    
    def update_bosqich(self):
        
        self.bosqich += 1
    
    def set_bosqich(self, yangi_bosqich):
        self.bosqich = yangi_bosqich
        
talaba1 = Talaba('Abrorbek', 'Komilov', 2002)
