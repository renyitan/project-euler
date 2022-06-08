"""
Problem 38 - Pandigital Multiples

Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""


def is_pandigital(n):
    nums = {"1": 1, "2": 1, "3": 1, "4": 1,
            "5": 1, "6": 1, "7": 1, "8": 1, "9": 1}
    digits = [ch for ch in str(n)]
    for ch in digits:
        nums[ch] = nums.get(ch, 0) - 1
        if nums[ch] < 0:
            return False
    return all(x == 0 for x in nums.values())


def run():

    for n in range(9387, 9233, -1):
        result = str(n) + str(2*n)
        if is_pandigital(int(result)):
            print(result)
            break


if __name__ == "__main__":
    print(run())
