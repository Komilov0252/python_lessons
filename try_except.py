#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 20 07:34:44 2025

@author: ironman
"""
try:
    with open(filena) as f:
        text = f.read()
except NameError:
    print("bunday file mavjud emas")
    