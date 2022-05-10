"""
Finds divisors of a natural number, n in O(sqrt(n)) time
https://www.geeksforgeeks.org/find-divisors-natural-number-set-1/
"""
import math


def get_divisors(n):
    divisors = []
    i = 1
    while (i <= math.sqrt(n)):
        if n % i == 0:
            if n / i == i:
                divisors.append(i)
            else:
                divisors.append(i)
                divisors.append(int(n/i))
        i += 1
    return divisors
