# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import time

check = 1
count = 1

for divisor in range(3,100):
	mark = time.time()

	while True:
		divisor_count = 0
		dividors = range(1,divisor+1)
		dividors.reverse()
		for div in dividors:
			if count % check != 0:
				break
			if count % div == 0:
				divisor_count = divisor_count + 1
			else:
				break
		if divisor_count == divisor:
			break
		count = count + check # wooo! increment by the previous solution

	check = count
	print divisor,'\t','%5f' % (time.time()-mark),'\t',count