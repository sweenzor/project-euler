#!/usr/bin/env python

# You are given the following information, but you may prefer
# to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September, April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.

# A leap year occurs on any year evenly divisible by 4,
# but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month
# during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

import datetime

sunday_count = 0
d = datetime.date(1901,1,1)

while d != datetime.date(2000,12,31):
    # check if current day is a sunday, and the 1st
    if d.weekday() == 6 and d.day == 1:
        sunday_count += 1
    
    # increment the day
    d += datetime.timedelta(1)

print 'number of Sundays: ', sunday_count
