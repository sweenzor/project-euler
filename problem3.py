# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?



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



primes = euler_sieve(10000000) # tee hee, this sould be ~enough primes
for divisor in primes:
	if 600851475143 % divisor == 0:
		print divisor
