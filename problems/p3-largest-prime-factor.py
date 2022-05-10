"""
Problem 3 - Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""


def run():
    n = 600851475143
    factor = 1
    while factor < n:
        factor += 2
        while n % factor == 0:
            n /= factor
    return factor


if __name__ == "__main__":
    print(run())
