#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
The DataFrame Data Structure
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
print df

# Query rows by loc and cols by indexing opeartor
print df.loc['Store 1']
print df['Item Purchased']
print df.loc['Store 1']['Item Purchased'] == df['Item Purchased']['Store 1']
# Slice DataFrame
# print df.loc[:, ['Name', 'Cost']]
# print df.loc[['Store 1'], :]

# Drop rows not in memory
print df.drop('Store 1')
print df