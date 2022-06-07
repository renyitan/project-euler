"""
Problem 35 - Circular Primes

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
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


def run():
    max_limit = 1000000
    circular_primes = set()
    for n in range(max_limit):
        if is_prime(n):
            digits = [ch for ch in str(n)]
            is_circular = True
            for _ in range(len(digits)):
                if not is_prime(int("".join(digits))):
                    is_circular = False
                    break
                rotate(digits)
            if is_circular:
                circular_primes.add(n)
    return len(circular_primes)
    
    
def reverse(digits, start, end):
    while start < end:
        digits[start], digits[end] = digits[end], digits[start]
        start, end = start+1, end-1


def rotate(digits, k=1):
    n = len(digits)
    k %= n
    reverse(digits, 0, n-1)
    reverse(digits, 0, k-1)
    reverse(digits, k, n-1)
    


if __name__ == "__main__":
    print(run())
