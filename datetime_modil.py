#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 20 07:41:23 2025

@author: ironman
"""

import datetime as dt

hozir = dt.datetime.now()
print(hozir)
print(type(hozir))
print(hozir.hour)
print(hozir.minute)
print(hozir.second)

print(dt.date.today())

ertaga = dt.datetime(2025, 7, 24, 00, 00, 00)

print("ertangi sana ", ertaga)

vaqt = dt.datetime.now().time().minute
print(vaqt)
bugun = ertaga - hozir




