#!/usr/bin/env python

# Let d(n) be defined as the sum of proper divisors of n
# (numbers less than n which divide evenly into n).

# If d(a) = b and d(b) = a, where a != b,
# then a and b are an amicable pair and
# each of a and b are called amicable numbers.

# For example, 
# the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
# therefore d(220) = 284. 
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.


divisors = {}

def find_divisors(num):

    if num in divisors:
        return divisors[num]

    divs = []
    div_range = range(1, num)
    div_range.reverse()

    for div in div_range:

        if num % div == 0:

            divs.append(div)
    
    divisors[num] = sum(divs)


for num in range(1,10000):
    find_divisors(num)


total = 0
for div in divisors:

    try:
        if div == divisors[divisors[div]] and div != divisors[div]:
            print div, divisors[div]
            total += div
    except:
        pass

print 'total: ', total
