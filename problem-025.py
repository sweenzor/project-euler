#!/usr/bin/env python

# The 12th term, F12, is the first term to contain three digits.

# What is the first term in the Fibonacci sequence to contain 1000 digits?

a = 0
b = 1
count = 1

while len(str(b)) < 1000:

	b = a + b
	a = b - a
	count += 1

print count
