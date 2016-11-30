#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
The Python Programming Language: Lambda and List Comprehensions
November 29, 2016
Coded by Meen Chul Kim
'''

# Lambda takes in three parameters and adds the first two
f = lambda x, y, z : x + y
print f(1, 2, 3)

# Iterate from 0 to 999 and return the even numbers
evens_for = []
for num in range(0, 1000):
	if num % 2 == 0:
		evens_for.append(num)

# Do the same task with list comprehentsion
evens_comp = [num for num in range(0, 1000) if num % 2 ==0]
print evens_for == evens_comp
