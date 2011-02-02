# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.

# Find the largest palindrome made from the product of two 3-digit numbers.

multiples = []

for i in range(1000):
	for j in range(1000):
		multiples.append(i*j)

multiples.sort()

# mapping to a string? ugh
for num in multiples[::-1]:
	if num == int(str(num)[::-1]):
		print num