#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Reading and Writing CSV files
November 28, 2016
Coded by Meen Chul Kim
'''

'''
Data description
mpg : miles per gallon
class : car classification
cty : city mpg
cyl : # of cylinders
displ : engine displacement in liters
drv : f = front-wheel drive, r = rear wheel drive, 4 = 4wd
fl : fuel (e = ethanol E85, d = diesel, r = regular, p = premium, c = CNG)
hwy : highway mpg
manufacturer : automobile manufacturer
model : model of car
trans : type of transmission
year : model year
'''

import csv

# Read in csv as dictionary
with open('../data/mpg.csv') as csvfile:
	mpg = list(csv.DictReader(csvfile))

# Check lenth and keys
length = len(mpg)
print 'The length of the csv is {}'.format(length)
print 'Keys: {}'.format(mpg[-1].keys())

# Calculate the average cty fuel
avg_cty = sum(float(car['cty']) for car in mpg) / length
print 'The average cty fuel is %.2f' % avg_cty

# Caculate the average hwy fule
avg_hwy = sum(float(car['hwy']) for car in mpg) / length
print 'The average hwy fuel is %.2f' % avg_hwy

# Return the unique values for the number of cylinders
cyls = set(car['cyl'] for car in mpg)
print 'Types of cylinders: {}'.format(cyls)

# Group the cars by number of cylinder
#		and find the average cty mpg for each group
avg_cty_cyl = []
for cyl in cyls:
	total = 0
	count = 0
	for car in mpg:
		if car['cyl'] == cyl:
			total += float(car['cty'])
			count += 1
	avg_cty_cyl.append((cyl, round(total / count, 2)))

# Sort the result
avg_cty_cyl.sort(key=lambda (cyl, cty): cyl)
print 'The average cty fuel by cylnder is {}'.format(avg_cty_cyl)

# Return the unique values for the class types
clss = set(car['class'] for car in mpg)
print 'Types of classes: {}'.format(clss)

# Find the average hwy mpg for each class of vehicle
avg_hwy_cls = []
for cls in clss:
	total = 0
	count = 0
	for car in mpg:
		if car['class'] == cls:
			total += float(car['hwy'])
			count += 1
	avg_hwy_cls.append((cls, round(total / count, 2)))

# Sort the result
avg_hwy_cls.sort(key=lambda (cls, hwy): hwy, reverse=True)
print 'The average hwy fuel by class is {}'.format(avg_hwy_cls)
