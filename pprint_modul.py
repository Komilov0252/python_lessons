#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 20 07:58:30 2025

@author: ironman
"""

from pprint import pprint
import json
import requests

filename = "file_info.txt"

with open(filename) as f:
    text = json.load(f)
pprint(text)

r = requests.get('https://api.github.com')
pprint(r.json())

