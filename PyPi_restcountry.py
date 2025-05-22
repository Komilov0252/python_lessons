#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 22 14:14:58 2025

@author: ironman
"""

import requests
import json
from pprint import pprint

country = "Uzbekistan"

response = requests.get(f"https://restcountries.com/v3.1/name/{country}")
if response.status_code == 200:
    
    json_str = response.json()
    pprint(json_str[0].get('name').get('nativeName').get('rus').get('official'))
    pprint(json_str)
    print(type(json_str[0]))    
else:
    print(response.status_code)