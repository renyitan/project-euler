"""
Problem 16 - Power digit sum

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
"""


def run():
    # use bit shift to compute 2**1000
    digits = [int(u) for u in str(1 << 1000)]
    return sum(digits)


if __name__ == "__main__":
    print(run())
