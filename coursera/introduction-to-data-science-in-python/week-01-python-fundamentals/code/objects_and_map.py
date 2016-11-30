#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
The Python Programming Language: Dates and Times
November 29, 2016
Coded by Meen Chul Kim
'''

# An example of a class
class Person(object):
	# Class variable
	department = 'School of Information'

	def set_name(self, name):
		self.name = name

	def set_location(self, location):
		self.location = location

	def get_name(self):
		return self.name

	def get_location(self):
		return self.location

person = Person()
person.set_name('Christopher Brooks')
person.set_location('Ann Arbor, MI, USA')
print person.get_name()

# Map the min function between two lists
store1 = [10.00, 11.00, 12.34, 2.34]
store2 = [9.00, 11.10, 12.34, 2.01]
cheapest = map(min, store1, store2)
print cheapest
