# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

divisor = 10

count = 1
while True:
	divisor_count = 0
	for div in range(1,divisor+1):
		if count % div == 0:
			divisor_count = divisor_count + 1
	if divisor_count == divisor:
		print count
		break
	count = count + 1