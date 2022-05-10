"""
Problem 6 - Sum square difference

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def run():
    # sum of squares, and sum
    sum_sq, sum = 0, 0
    start, end = 1, 100

    for i in range(start, end+1):
        sum_sq += i**2
        sum += i

    # square of sums
    sq_sum = sum ** 2
    return sq_sum - sum_sq


if __name__ == "__main__":
    print(run())
