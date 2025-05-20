#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 20 08:36:22 2025

@author: ironman
"""

from googletrans import Translator

matn_uz = "Assalomu alaykum"

tarjimon = Translator()

tarjima = tarjimon.translate(matn_uz)

print(tarjima)
