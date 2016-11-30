#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
The Python Programming Language: Numerical Python (NumPy)
November 30, 2016
Coded by Meen Chul Kim
'''

import numpy as np

# Create a list and covert in to a numpy array
#		or pass in it directly
my_list = [1, 2, 3]
x = np.array(my_list)
y = np.array([4, 5, 6])
print 'Numpy array of {}: {}'.format(my_list, x)

# Pass in a list of lists to create a multidimensional array
multi_list = [[1, 2, 3], [4, 5, 6]]
m = np.array(multi_list)
print 'Numpy array of {}: {}'.format(multi_list, m)

# Use the shape method to find the dimensions of the array
rows, cols = m.shape
print '{} has {} rows and {} columns'.format(m, rows, cols)

# Use arange to return evenly spaced values 
#		within a given interval
n = np.arange(0, 30, 2)
print n

# Use reshape returns an array 
#		with the same data with a new shape
n = n.reshape(3, 5)
print n

# Use linspace to return evenly spaced numbers 
#		over a specified interval
o = np.linspace(0, 4, 9)
print o

# Use resize to change the shape and size of array in-place
o.resize(3, 3)
print o

# Use ones, zeros, and eye to return 
#		a new array of given shape and type,
#		filled with ones, zeros, and diagonal zeros
print np.ones((3, 2))
print np.zeros((2, 3))
print np.eye(3)

# Use diag to construct a diagonal array
print np.diag(my_list)

# Create an array using repeating list
print np.array([1, 2, 3] * 3)

# Repeat elements of an array using repeat
print np.repeat([1, 2, 3], 3)

print np.array([1, 2, 3] * 3) == np.repeat([1, 2, 3], 3)

## Combine arrays
p = np.ones([2, 3], float)
print p

# Use vstack to stack arrays vertically (row-wise)
print np.vstack([p, 2 * p])

# Use hstack to stack arrays horizontally (column-wise)
print np.hstack([p, 2 * p])

## Operations
# Use +, -, *, / and ** to perform element wise addition, 
#		subtraction, multiplication, division and power
print x + y
print x - y
print x * y
print x / y
print x ** 2

# Doc product
print x.dot(y) == sum(x * y.T)

# Transposing arrays
z = np.array([y, y ** 2])
print z
print 'The shape before transposing: {}'.format(z.shape)
z_T = z.T
print z_T
print 'The shape after transposing: {}'.format(z_T.shape)

# Use dtype to see the data type
print 'The type of data before type-casting: {}'.format(z.dtype)

# Use astype for type-casting
z = z.astype('f')
print 'The type of data after type-casting: {}'.format(z.dtype)

## Math functions
vec = np.array([-4, -2, 1, 3, 5])
# many built-in math functions: sum, max, min, mean, std
print 'The std of {}: {}'.format(vec, vec.std())

# Use argmax and argmin to return 
#		the index of the maximum and minimum values in the array
print 'The index of the max in {}: {}'.format(vec, vec.argmax())
print 'The index of the min in {}: {}'.format(vec, vec.argmin())

## Indexing/slicing
s = np.arange(13)**2
print s

# Use bracket notation to get the value at a specific index
print s[0], s[4], s[-1]

# Use : to indicate a range. array[start:stop]
#		Leaving start or stop empty will default 
#		to the beginning/end of the array
print s[1:5], s[-4:]

# A second : can be used to indicate step-size
#		array[start:stop:stepsize]
print s[-5::-2]

r = np.arange(36)
r.resize((6, 6))
print r

# Use bracket notation to slice: array[row, column]
print r[2, 2] == 14

# Use : to select a range of rows or columns
print r[3, 3:6] == [21, 22, 23]

# Select all the rows up to (and not including) row 2, 
#		and all the columns up to (and not including) the last column
print r[:2, :-1]

# Slice the last row and only every other element
print r[-1, ::2]

# Perform conditional indexing
print r[r > 30]

# Assign all values in the array 
#		that are greater than 30 to the value of 30
r[r > 30] = 30
print r

## Copying data
# Referencing and modifying data in NumPy changes the original data
#		To aviud this, use copy
r_copy = r.copy()
r_copy[:] = 10
print r_copy
print r

## Iterating over arrays
test = np.random.randint(0, 10, (4, 3))

# Iterate by row
for row in test:
	print row

# Iterate by index
for i in range(len(test)):
	print test[i]

# Iterate by row and index
for i, row in enumerate(test):
	print 'row', i, 'is', row

# Use zip to iterate over multiple iterables
test2 = test ** 2

for i, j in zip(test, test2):
	print i, '+', j, '=', i + j
