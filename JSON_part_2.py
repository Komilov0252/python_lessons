#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 22 09:08:30 2025

@author: ironman
"""

import json
import requests
from pprint import pprint

url = "https://api.github.com/users"

response = requests.get(url)

if response.status_code == 200:
    result_json = response.json()
    pprint(result_json[0])
    print(type(result_json[0]))
else:
    print(f" Error : {response.status_code}")
    
file = "new_json_file.txt"

with open(file, 'w') as f:
    json.dump(result_json, f, indent=4)

with open(file, 'r') as f:

    new_json = json.load(f)

pprint(new_json)
print(type(new_json[0]))    

    