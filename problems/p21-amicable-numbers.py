"""
Problem 21 - Amicable Numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.
"""
import math


def run():

    num_range = 10000
    amicable = set()
    for i in range(num_range+1):
        sum_i_divisors = sum_proper_divisors(i)
        sum_other_divisors = sum_proper_divisors(sum_i_divisors)
        if i == sum_other_divisors and i != sum_i_divisors:
            amicable.add(i)
            amicable.add(sum_i_divisors)

    return sum(list(amicable))


def sum_proper_divisors(n):
    if n == 0:
        return 0
    total = 0
    i = 1
    while (i <= math.sqrt(n)):
        if n % i == 0:
            if n / i == i:
                total += i
            else:
                total += i
                total += int(n/i)
        i += 1
    # remove n from the sum, since we're looking for proper divisors (which excludes n)
    total -= n
    return total


if __name__ == "__main__":
    print(run())

    # print(562, sum(get_proper_divisors(562)))
