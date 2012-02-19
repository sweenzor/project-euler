#!/usr/bin/env python

# Find the sum of the digits in the number 100!

import math

fact = math.factorial(100)

total = 0
for digits in str(fact):
    total += int(digits)

print total
