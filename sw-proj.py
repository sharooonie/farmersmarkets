# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 17:36:27 2015

@author: sharonwang
"""

import csv

with open('Export.csv') as usdafile:
    markets = csv.reader(usdafile)
    
print(markets)

