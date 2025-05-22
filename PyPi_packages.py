#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 22 13:44:05 2025

@author: ironman
"""

import requests
from bs4 import BeautifulSoup

url = "https://kun.uz/news/main"

response = requests.get(url)

if response.status_code == 200:
    
    result = response.text
    soup = BeautifulSoup(result, 'html.parser')
    
    news = soup.find_all(class_="")
    
    print(news)
else:
    print(f"error {response.status_code}")