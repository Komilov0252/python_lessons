#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 21 18:52:51 2025

@author: ironman
"""

import json
import googlemaps

x = 10
x_json = json.dumps(x)
print(x_json)

sonlar = (12, 23, 34, 45)
json_sonlar = json.dumps(sonlar)
print(json_sonlar)

sonlar2 = json.loads(json_sonlar)

data = {"name": "Alice", "age": 25}
json_str = json.dumps(data, indent=4)
print(json_str)

with open("new_json_file.txt", 'r') as f:
    new = json.load(f)
    
print(new)
print(type(new[3]))