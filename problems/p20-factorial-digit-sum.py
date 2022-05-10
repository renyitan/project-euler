"""
Problem 20 - Factorial Digit Sum

n! means n × (n − 1) × ... × 3 × 2 × 1
For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Find the sum of the digits in the number 100!
"""


def run():
    fac = 1
    for i in range(2, 100+1):
        fac *= i
    sum = 0
    while fac > 0:
        sum += fac % 10
        fac //= 10
    return sum


if __name__ == "__main__":
    print(run())
