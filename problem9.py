# Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.



potential = []
for a in range(1,1001)[::-1]:
	print a
	for b in range(1,1001-a):
		for c in range(1,1001-a-b):
			if a+b+c == 1000:
				# print c
				potential.append([a,b,c])

# print potential
print len(potential)

for a,b,c in potential:
	if a**2 + b**2 == c**2:
		print a,b,c