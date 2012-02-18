#!/usr/bin/env python

# By starting at the top of the t below and moving to adjacent
# numbers on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom in triangle.txt
# (right click and 'Save Link/Target As...'), a 15K text file
# containing a triangle with one-hundred rows.

# NOTE: This is a much more difficult version of Problem 18.
# It is not possible to try every route to solve this problem,
# as there are 2^99 altogether! If you could check one trillion (10^12)
# routes every second it would take over twenty billion years to
# check them all. There is an efficient algorithm to solve it. ;o)

triangle = []
fid = open('problem-067.txt', 'r')
for line in fid.readlines():
    row = line[:-2].split(' ')
    triangle.append(map(int, row))


def all_paths(triangle):

    paths = [[(0,triangle[0][0])]]

    for index, row in enumerate(triangle[1:]):

        new_paths = []
        for path in paths:

            index = path[-1][0]
            new_paths.append(path + [(index, row[index])])
            new_paths.append(path + [(index+1,row[index+1])])
        
        paths = new_paths

    clean_paths = []
    for path in paths:
        clean_paths.append([num[1] for num in path])

    return clean_paths


print max([sum(path) for path in all_paths(triangle[:20])])
