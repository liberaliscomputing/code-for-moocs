#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
The Python Programming Language: Types and Sequences
November 28, 2016
Coded by Meen Chul Kim
'''

# Use type to return the object's type.
s = 'This is a string'
def add_nums(x, y):
	return x + y

t = (1, 'a', 2, 'b')
l = [1, 'a', 2, 'b']
data = [s, None, 1, 1.0, add_nums, t, l]
form = 'Type of \'{}\' is {}'
for d in data:
	print form.format(d, type(d))

# Append an object to a list
l.append(3.3)
print 'l after append: {}'.format(l)

# Loop through each item in the list
for item in l:
	print '\'{}\' of \'{}\''.format(item, l)

# Use the index operator
i = 0
while i < len(l):
	print '\'{}\'th item of \'l\''.format(i, l)
	i += 1

# Use + to concatenate lists
print [1, 2] + [3, 4]

# Use * to repeat lists.
print [1] * 3

# Use the in operator to check if an item is inside a list
print 1 in [1, 2, 3]

# Use bracket notation to slice a string
s = 'This is a string'
print s[0]
print s[0:1]
print s[0:2]

# Return the last element of the string
print s[-1]

# Return the slice starting 
#		from the 4th element from the end 
#		and stopping before the 2nd element from the end.
print s[-4:-2]

# Return a slice from the beginning of the string 
#		and stopping before the 3rd element
print s[:3]

# Return a slice starting 
#		from the 3rd element of the string 
#		and going all the way to the end
print s[3:]

# Concatenate strings
first_name = 'Christopher'
last_name = 'Brooks'
print first_name + ' ' + last_name
print first_name * 3
print 'Chris' in first_name

# Use split() to string
full_name = 'Christopher Arthur Hansen Brooks'
first_name = full_name.split()[0]
last_name = full_name.split()[-1]
print first_name
print last_name

# Make sure convert objects to strings before concatenating
print first_name + str(2)

# Associate keys with values in a dictionary
d = {'Christopher Brooks': 'brooksch@umich.edu', 
	'Bill Gates': 'billg@microsoft.com'}
print d['Christopher Brooks']

# Iterate over all of the keys
for name in d:
	print d[name]

# Iterate over all of the values
for email in d.values():
	print email

# Iterate over all of the items in the dictionary
for name, email in d.items():
	print name, email

# Unpack a sequence into different variables
contact = ('Christopher', 'Brooks', 'brooksch@umich.edu')
fname, lname, email = contact
print fname
