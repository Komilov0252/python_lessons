#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 20 08:10:15 2025

@author: ironman
"""

import re 

filename = '/home/ironman/Downloads/google-10000-english.txt'

with open(filename) as file:
    text = []
    text = list(file.readlines())
    
print(text)
print(type(text))

word1 = 'assalomu'
word2 = 'allaykuu'
word3 = 'allaqachon'

andoza = "^a......u$"

print(re.match(andoza, word1))
print(re.match(andoza, word2))
print(re.match(andoza, word3))