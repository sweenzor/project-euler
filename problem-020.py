#!/usr/bin/env python

import math

fact = math.factorial(100)

total = 0
for digits in str(fact):
    total += int(digits)

print total
