#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 21 18:44:21 2025

@author: ironman
"""

import pickle

with open("write_binary", 'rb') as f:
    talaba1 = pickle.load(f)
    talaba2 = pickle.load(f)
    
print(type(talaba1))
print(talaba2)
print(talaba1['familiyasi'])
print(talaba1.get('yil'))