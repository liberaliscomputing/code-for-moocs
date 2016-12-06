#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Mising Values
December 5, 2016
Coded by Meen Chul Kim
'''

import pandas as pd

# Read in log.csv
path = '../data/log.csv'
df = pd.read_csv(path)

# Set multiple indexes
df = df.set_index(['time', 'user'])

# Use fillna to impute missing data
df = df.fillna(method='ffill')
print df