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

import time

triangle = []
fid = open('problem-067.txt', 'r')
for line in fid.readlines():
    row = line[:-2].split(' ')
    triangle.append(map(int, row))


def path_sum(path):

    total = 0
    for entry in path:
        total += entry[1]
    return total


def all_paths(triangle):

    paths = [[(0,triangle[0][0])]]

    for index, row in enumerate(triangle[1:]):

        print 'row: ', index+2, '\t',
        new_paths = []
        for path in paths:

            index = path[-1][0]
            new_paths.append(path + [(index, row[index])])
            new_paths.append(path + [(index+1,row[index+1])])
        
        paths = new_paths
        print 'num paths: ', len(paths)

        if len(paths) > 16384:

            sums = [path_sum(path) for path in paths]
            sums.sort()
            drop = sums[int(len(sums)*(0.5))]

            good_paths = []
            for path in paths:
                if path_sum(path) > drop:
                    good_paths.append(path)
            
            paths = good_paths

    clean_paths = []
    for path in paths:
        clean_paths.append([num[1] for num in path])

    return clean_paths

mark = time.time()
total = max([sum(path) for path in all_paths(triangle)])
print '\nlargest sum: ', total
print 'elapsed: ', time.time()-mark
