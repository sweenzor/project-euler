#!/usr/bin/env python

# By starting at the top of the t below and moving to adjacent
# numbers on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the t below:

# NOTE: As there are only 16384 routes, it is possible to solve this
# problem by trying every route. However, Problem 67, is the same
# challenge with a t containing one-hundred rows; it cannot be
# solved by brute force, and requires a clever method! ;o)

control = []

control.append([3])
control.append([7,4])
control.append([2,4,6])
control.append([8,5,9,3])


t = []

t.append([75])
t.append([95,64])
t.append([17,47,82])
t.append([18,35,87,10])
t.append([20,04,82,47,65])
t.append([19,01,23,75,03,34])
t.append([88,02,77,73,07,63,67])
t.append([99,65,04,28,06,16,70,92])
t.append([41,41,26,56,83,40,80,70,33])
t.append([41,48,72,33,47,32,37,16,94,29])
t.append([53,71,44,65,25,43,91,52,97,51,14])
t.append([70,11,33,28,77,73,17,78,39,68,17,57])
t.append([91,71,52,38,17,14,91,43,58,50,27,29,48])
t.append([63,66,04,68,89,53,67,30,73,16,69,87,40,31])
t.append([04,62,98,27,23,9,70,98,73,93,38,53,60,04,23])

triangle = t


# brute force

from random import randint

def random_paths(triangle):
    best = 0
    while True:

        total = 0
        index = -1
        for row in triangle:
            index = randint(0,index+1)
            total += row[index]

        if total > best:
            best = total
            print best

def all_paths(triangle):

    paths = [[(0,triangle[0][0])]]

    for index, row in enumerate(triangle[1:]):

        new_paths = []
        for path in paths:

            index = path[-1][0]
            new_paths.append(path + [(index, row[index])])
            new_paths.append(path + [(index+1,row[index+1])])
        
        paths = new_paths

    return paths






for path in all_paths(control):
    print path
