#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
The Python Programming Language: Dates and Times
November 29, 2016
Coded by Meen Chul Kim
'''

import datetime as dt
import time as tm

# Display the Epoch time
epoch = tm.time()
print 'The current time in Epoch is \'{}\''.format(epoch)

# Convert the Epoch time to datetime
dtnow = dt.datetime.fromtimestamp(epoch)
print 'The datetime of \'{}\' is \'{}\''.format(epoch, dtnow)

# Create a timedelta expressing the difference between two dates
delta = dt.timedelta(days=100)
#today = dt.date.today()
print '100 days ago from {} is {}'.format(dtnow, dtnow - delta)
