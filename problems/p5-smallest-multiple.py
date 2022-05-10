"""
Problem 5 - Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""
import math


def run():
    start, end = 1, 20
    nums = [i for i in range(start, end)]
    lcm = nums[0]
    for i in nums[1:]:
        # Know that Least Common Multiple, LCM = (n1*n2)/gcd(n1, n2), where gcd is Greatest Common Divisor
        lcm = int(lcm*i/math.gcd(lcm, i))
    return lcm


if __name__ == "__main__":
    print(run())
