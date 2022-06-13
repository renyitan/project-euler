"""
Check if number, n is prime using 6k+1 optimization
All primes greater than 3 are of the form 6k ± 1, where k is any integer greater than 0.
https://en.wikipedia.org/wiki/Primality_test
"""

import math


def is_prime(n: int) -> list[int]:
    if n <= 3:
        return n > 1
    # check if n is a multiple of 2 or 3
    if not n % 2 or not n % 3:
        return False
    i = 5
    stop = int(math.sqrt(n))
    while i <= stop:
        if not n % i or not n % (i+2):
            return False
        i += 6
    return True
