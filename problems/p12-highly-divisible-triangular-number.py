import math


def run():

    i = 0
    triangle_num = 0
    longest = 0

    while True:
        triangle_num += i
        num_divisors = get_num_divisors(triangle_num)
        longest = max(longest, num_divisors)
        print(
            f'i: {i}, number: {triangle_num}, divisors: {num_divisors}, longest: {longest}')

        if num_divisors > 500:
            return triangle_num
        i += 1


def get_num_divisors(n):
    """
    Finds divisors of a number, n in O(sqrt(n)) time
    # https://www.geeksforgeeks.org/find-divisors-natural-number-set-1/
    """
    num_divisors = 0
    i = 1
    while (i <= math.sqrt(n)):
        if n % i == 0:
            if n / i == i:
                num_divisors += 1
            else:
                num_divisors += 2
        i += 1

    return num_divisors


if __name__ == "__main__":
    print(run())
    # print(get_num_divisors(100))
