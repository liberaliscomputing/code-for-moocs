#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Querying a DataFrame
December 5, 2016
Coded by Meen Chul Kim
'''

import pandas as pd

# Read in olympics.csv
path = '../data/olympics.csv'
df = pd.read_csv(path)

# Set index column (int) and number of rows skipped (int)
df = pd.read_csv(path, index_col=0, skiprows=1)

# Convert columns
for col in df.columns:
	if col[:2] == '01':
		df.rename(columns={col: 'Gold' + col[4:]}, inplace=True)
	elif col[:2] == '02':
		df.rename(columns={col: 'Silver' + col[4:]}, inplace=True)
	elif col[:2] == '03':
		df.rename(columns={col: 'Bronze' + col[4:]}, inplace=True)
	elif col[:1] == '№':
		df.rename(columns={col: '#' + col[1:]}, inplace=True)

# Boolean masking is overlaid on top of either series or DataFrame 
#		having each of the values are either true or false
threshold = 0
print 'Counturies having more than {} gold medals:\n{}'.format(
	threshold, df['Gold'] > threshold)

# Use where function taking a Boolean mask 
#		to convert false to NaN
only_gold = df.where(df['Gold'] > threshold)
print only_gold['Gold'].count()
print df['Gold'].count()

# Drop NaN rows
print only_gold.dropna()

# Use indexing operator to filter
print df[df['Gold'] > 0]