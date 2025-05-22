#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 21 18:44:08 2025

@author: ironman
"""

import pickle

talaba1 = {"familiyasi": "Komilov", "ismi":"Abrorbek", "yil":2002}
talaba2 = {"familiyasi": "Asadov", "ismi":"Sardor", "yil":1965}

with open("write_binary", 'wb') as f:
    pickle.dump(talaba1, f)
    pickle.dump(talaba2, f)