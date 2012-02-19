#!/usr/bin/env python

# A perfect number is a number for which the sum of its proper
# divisors is exactly equal to the number. For example, the sum
# of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
# which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors
# is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
# the smallest number that can be written as the sum of two abundant
# numbers is 24. By mathematical analysis, it can be shown that all
# integers greater than 28123 can be written as the sum of two
# abundant numbers. However, this upper limit cannot be reduced
# any further by analysis even though it is known that the greatest
# number that cannot be expressed as the sum of two abundant numbers
# is less than this limit.

# Find the sum of all the positive integers which cannot be written
# as the sum of two abundant numbers.

import math

def divisors(num):

    divs = []
    for i in range(1, int(math.sqrt(num))+1):
        if num % i == 0:
            if not i in divs:
                divs.append(i)
            if not num/i in divs and num/i != num:
                divs.append(num/i)

    return divs

def check_abundant(num):

    divs = divisors(num)
    div_sum = 0
    for div in divs:
        div_sum += div

    return div_sum > num

for i in range(1,29000):
    print i, check_abundant(i)

