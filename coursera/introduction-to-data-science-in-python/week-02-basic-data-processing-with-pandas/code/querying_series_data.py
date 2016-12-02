#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
The Series Data Structure
December 1, 2016
Coded by Meen Chul Kim
'''

import pandas as pd

# Explore series data structure
animals = ['Tiger', 'Bear', 'Moose']
print pd.Series(animals)

numbers = [1, 2, 3]
print pd.Series(numbers, dtype='f')

sports = {
	'Archery': 'Bhutan',
	'Golf': 'Scotland',
	'Sumo': 'Japan',
	'Taekwondo': 'South Korea'}
df = pd.Series(sports, index=['Golf', 'Sumo', 'Hockey'])
print df