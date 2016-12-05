#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Querying a Series
December 5, 2016
Coded by Meen Chul Kim
'''

import pandas as pd
import numpy as np
import timeit

# Prepare querying series
sports = {
	'Archery': 'Bhutan',
	'Golf': 'Scotland',
	'Sumo': 'Japan',
	'Taekwondo': 'South Korea'}
s = pd.Series(sports)

# Use indexing operators (attributes) to query
print s.iloc[3] == s[3] == 'South Korea'
print s.loc['Golf'] == s['Golf'] == 'Scotland'

# Use iterator with series data
s = pd.Series([100.00, 120.00, 101.00, 3.00])
print sum(item for item in s) == np.sum(s)

# Create a big series of random numbers
s = pd.Series(np.random.randint(0, 1000, 10000))
print s.head()

# Time a small function
stmt = 'sum(item for item in s)'
setup = '''
import pandas as pd
import numpy as np

s = pd.Series(np.random.randint(0, 1000, 10000))
'''

print timeit.timeit(stmt, setup, number=100)

# Add two to each item in s using broadcasting or iterator
s += 2 
print s.head()

for index, value in s.iteritems():
	s.set_value(index, value + 2)
print s.head()

for index in s.keys():
	s[index] += 2
print s.head()

# Append series data to series data
original_sports = pd.Series({
	'Archery': 'Bhutan',
	'Golf': 'Scotland',
	'Sumo': 'Japan',
	'Taekwondo': 'South Korea'})

cricket_loving_countries = pd.Series(
	['Australia', 'Barbados', 'Pakistan', 'England'], 
	index=['Cricket', 'Cricket', 'Cricket', 'Cricket'])
all_countries = original_sports.append(cricket_loving_countries)

# Appending does not affect the original data
print original_sports

# Values pair up with indexes
print cricket_loving_countries

print all_countries

# Query series data with index
print all_countries.loc['Cricket']