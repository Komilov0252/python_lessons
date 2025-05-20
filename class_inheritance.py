#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 20 11:45:06 2025

@author: ironman
"""
import datetime as dt

class Shaxs:
    def __init__(self, first_name, last_name, passport, dt):
        self.first_name = first_name
        self.last_name = last_name
        self.passport = passport
        self.dt = dt
        
    def get_info(self):
        info = f"{self.first_name} {self.last_name}.  "
        info += f"  Passport:{self.passport} tug`ilgan yil : {self.dt}"
        return info
    
    def get_age(self):
        n = dt.date.today().year
        return n - self.dt  

class Talaba(Shaxs):
    def __init__(self,first_name, last_name, passport, dt, t_id, manzil):
        super().__init__(first_name, last_name, passport, dt)
        self.t_id = t_id
        self.bosqich = 1
        self.manzil = manzil
        
    def get_id(self):
        return self.t_id
    
    def get_bosqich(self):
        return self.bosqich
    
    def get_info(self):
        info = f"{self.first_name} {self.last_name}. "
        info += f"id : {self.t_id} bosqichi : {self.bosqich}"
        return info

class Manzil:
    def __init__(self, uy, kocha, tuman, viloyat):
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat
    
    def get_manzil(self):
        manzil = f" {self.viloyat} viloyati {self.tuman} tumani "
        manzil += f"{self.kocha} kochasi {self.uy}-uy "
        return manzil
        
        
        
        
        
        
        