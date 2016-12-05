#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
DataFrame Indexing and Loading
December 5, 2016
Coded by Meen Chul Kim
'''

import pandas as pd

# Create DataFrame
purchase_1 = pd.Series({
	'Name': 'Chris',
	'Item Purchased': 'Dog Food',
	'Cost': 22.50})
purchase_2 = pd.Series({
	'Name': 'Kevyn',
	'Item Purchased': 'Kitty Litter',
	'Cost': 2.50})
purchase_3 = pd.Series({
	'Name': 'Vinod',
	'Item Purchased': 'Bird Seed',
	'Cost': 5.00})
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], 
	index=['Store 1', 'Store 1', 'Store 2'])

# Extract a column as series data
costs = df['Cost']
print type(costs)

# In-memory manipulation
costs += 2
print df

# Read in olympics.csv
path = '../data/olympics.csv'
df = pd.read_csv(path)
print df.head()

# Set index column (int) and number of rows skipped (int)
df = pd.read_csv(path, index_col=0, skiprows=1)
print df.head()

# Print column names
print df.columns

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
print df.head()