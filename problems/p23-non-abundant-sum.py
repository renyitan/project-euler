"""
Problem 23 - Non-abundant sums

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
import math


def run():
    limit = 28123
    abundant = []
    for i in range(2, limit+1):
        if sum_proper_divisors(i) > i:
            abundant.append(i)

    total = 0
    sums_of_abundant = [False for _ in range(limit+1)]

    for i in range(len(abundant)):
        for j in range(i, len(abundant)):
            if abundant[i] + abundant[j] <= limit:
                sums_of_abundant[abundant[i]+abundant[j]] = True
            else:
                break
            

    total = 0
    print(sum([i for i, x in enumerate(sums_of_abundant) if not x]))
    # for i in range(i, limit+1):
    #     if not sums_of_abundant[i]:
    #         total += i

    return total


def sum_proper_divisors(n):
    total = 0
    i = 1
    while (i < math.sqrt(n)):
        if n % i == 0:
            if n / i == i:
                total += i
            else:
                total += i
                total += int(n/i)
        i += 1
    total -= n
    return total


if __name__ == "__main__":
    print(run())
    # print(sum_proper_divisors(0))
