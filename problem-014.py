# The following iterative sequence is defined for the set of positive integers:

# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13  40  20  10  5  16  8  4  2  1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

import time

def step_seq(num):
	if num % 2 == 0:
		return num/2
	else:
		return (3*num)+1

def steps_in_seq(num, solns):
	count = 1
	orig = num
	seq = [num]
	while num != 1:
		num = step_seq(num)
		if num in soln:
			count += solns[num]
			break
		else:
			count += 1
			seq.append(num)
	solns[orig] = count
	return count, seq

mark = time.time()
soln = {}
max_count = [1,1]
for num in xrange(1, 5000):
	count, seq = steps_in_seq(num, soln)
	#print num, count, seq
	if max_count[1] < count:
		max_count[0] = num
		max_count[1] = count
print time.time()-mark
print count
