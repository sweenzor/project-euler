#!/usr/bin/env python

# Using names.txt (right click and 'Save Link/Target As...'),
# a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order. Then working out 
# the alphabetical value for each name, multiply this value by
# its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order,
# COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th
# name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.

# What is the total of all the name scores in the file?

import string

# alphabet values
alpha = {}
for index, letter in enumerate(string.ascii_uppercase):
    alpha[letter] = index+1

# read list of names
fid = open('problem-022.txt', 'r')
lines = fid.readline()
names = lines.split(',')

# clean up some formatting
new_names = []
for name in names:
    new_names.append(name.replace("\"",""))
names = new_names

# alphabetical order
names.sort()

def name_value(name):
    total = 0
    for letter in name:
        total += alpha[letter]
    return total

total = 0
for index, name in enumerate(names):
    total += (index+1) * name_value(name)

print 'total name score: ', total

