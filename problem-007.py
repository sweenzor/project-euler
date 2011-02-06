# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10001st prime number?



# borrowed sieve code from wikipedia

def euler_sieve(n):
	# Create a candidate list within which non-primes will
	# marked as None, noting that only candidates below
	# sqrt(n) need be checked. 
	candidates = range(n+1)
	fin = int(n**0.5)
 
	# Loop over the candidates, marking out each multiple.
	# If the current candidate is already checked off then
	# continue to the next iteration.
	for i in xrange(2, fin+1):
		if not candidates[i]:
			continue
 
		candidates[2*i::i] = [None] * (n//i - 1)
 
	# Filter out non-primes and return the list.
	return [i for i in candidates[2:] if i]

	
primes = euler_sieve(10000000)

print primes[3-1]
print primes[6-1]
print primes[10001-1]
