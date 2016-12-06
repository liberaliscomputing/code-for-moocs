#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Indexing DataFrames
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

# Use index function to create a new colmumn
df['Country'] = df.index

# Use set_index and reset_index
# print df.set_index('Gold')
# print df.reset_index()

# Read in ocensus.csv
path = '../data/census.csv'
df = pd.read_csv(path)

# Use unique to return unique values in a specified column
print df['SUMLEV'].unique()

# Choose a subset of columns
selected_columns = [
	'STNAME',
	'CTYNAME',
	'BIRTHS2010',
	'BIRTHS2011',
	'BIRTHS2012',
	'BIRTHS2013',
	'BIRTHS2014',
	'BIRTHS2015',
	'POPESTIMATE2010',
	'POPESTIMATE2011',
	'POPESTIMATE2012',
	'POPESTIMATE2013',
	'POPESTIMATE2014',
	'POPESTIMATE2015']
print df[selected_columns].head()

# Set two indexes
df = df.set_index(['STNAME', 'CTYNAME'])
print df.head()

# Query a DataFrame with two indexes
key_1 = 'Michigan', 'Washtenaw County'
print df.loc[key_1]

# Query a DataFrame with multiple keys
key_2 = 'Michigan', 'Wayne County'
print df.loc[[key_1, key_2]]

# Exercise
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

df['Location'] = df.index
df = df.set_index(['Location', 'Name'])
df = df.append(pd.Series(data={
	'Cost': 3.00, 
	'Item Purchased': 'Kitty Food'}, 
	name=('Store 2', 'Kevyn')))
print df

# Another solution
# df = df.set_index([df.index, 'Name'])
# df.index.names = ['Location', 'Name']