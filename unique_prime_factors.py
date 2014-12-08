#!/usr/bin/python
import sys
import math
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

integer = int(sys.argv[1])
i = 2
prime_factors = []
while i * i < integer:
  if integer % i == 0:
    if is_prime(i):
      prime_factors.append(i)
  i += 1
print "Number of prime factors: ",  len(prime_factors)
print "Prime factors: ", prime_factors
