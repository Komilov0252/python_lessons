#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 20 13:53:41 2025

@author: ironman
"""
from incapsulation_method_class import Auto

class Avtosalon:
    def __init__(self, name):
        self.name = name
        self.avtolar = []
        
    def __repr__(self):
        return f"{self.name} avtosaloni"
    
    def add_car(self, *args):
        for avto in args:
            if isinstance(avto, Auto):
                self.avtolar.append(avto)
                
    def __getitem__(self, index):
        return self.avtolar[index]
        
    def __setitem__(self, index, qiymat):
        self.avtolar[index] = qiymat
        
    def __len__(self):
        return len(self.avtolar)
    
    def __call__(self):
        return [avto.model for avto in self.avtolar]
    
    def __add__(self, y):
        if isinstance(y, Avtosalon):
            yangi_salon = Avtosalon(f"{self.name} {y.name}")
            yangi_salon.avtolar = self.avtolar + y.avtolar
            return yangi_salon
        elif isinstance(y, Auto):
            self.add_car(y)
    
avtosalon1 = Avtosalon("Kingavto")
avtosalon2 = Avtosalon("Motors")
avtosalon3 = Avtosalon("Leapmotors")

avto1 = Auto("GM", "Gentra", "oq", "2016", "$18000", 36000)
avto2 = Auto("GM", "cobalt", "qora", "2024", "$19000", 9000)
avto3 = Auto("GM", "nexia3", "qora", "2024", "$19000", 9000)
avto4 = Auto("GM", "malibu", "qora", "2024", "$19000", 9000)
avto5 = Auto("GM", "kia", "qora", "2024", "$19000", 9000)
avto6 = Auto("TOYOTA", "CAMARU", "qora", "2024", "$132000", 2000)

avtosalon1.add_car(avto1, avto2)
avtosalon2.add_car(avto3, avto4, avto5)