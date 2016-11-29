#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
The Python Programming Language: Functions
November 28, 2016
Coded by Meen Chul Kim
'''

# Assign and print variables
x = 1
y = 2
print '{} + {} = {}'.format(x, y, x + y)

# Define a function that takes two numbers and adds them together
def add_nums(x, y):
	return '{} + {} = {}'.format(x, y, x + y)

print add_nums(x, y)

# Update add_nums to take an optional 3rd parameter
def add_nums(x, y, z=None):
	if z != None:
		return '{} + {} + {} = {}'.format(x, y, z, x + y + z)
	return '{} + {} = {}'.format(x, y, x + y)

print add_nums(x, y)
print add_nums(x, y, x + y)

# Update add_nums to take an optional flag parameter
def add_nums(x, y, z=None, flag=False):
	if flag:
		print 'Flag is {}'.format(flag)
	if z != None:
		return '{} + {} + {} = {}'.format(x, y, z, x + y + z)
	return '{} + {} = {}'.format(x, y, x + y)

print add_nums(x, y, flag=True)

# Assign function add_nums to a variable
sum = add_nums(x, y)
print sum 
