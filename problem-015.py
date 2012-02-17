#!/usr/bin/env python

# Starting in the top left corner of a 2x2 grid, 
# there are 6 routes (without backtracking) 
# to the bottom right corner.

# How many routes are there through a 20x20 grid?




# I'm assuming movement only to the right and downward:
# looks like pascals triangle, yo

from math import factorial

def pascals(n, k):

    return factorial(n) / (factorial(k) * factorial(n - k))


def solve_grid(x,y):
    """the row of the triangle you need is
    double the edge length of the grid

    for instance, on a 2x2 grid the nodes map to pascals:

        x            x
       x x          x x
      x x x        x x x
     x x x x        x x
    x x o x x        o

    and four rows down (or the total edge length)
    you've got the number of routes for that grid!"""

    if x != y:
        print 'needs to be a square grid'
        return

    return pascals(2*x,y)


print '2x2 grid: %i routes' %solve_grid(2,2)
print '20x20 grid: %i routes' %solve_grid(20,20)
