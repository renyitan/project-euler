"""
Problem 9 - Special Pythagorean Triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def run():
    nums = [num for num in range(1001)]
    target = 1000
    a, b, c = None, None, None
    for i in range(len(nums)):
        a, b, c = find_triplets(nums, i, target)
        if a and b and c:
            return a*b*c


def find_triplets(nums, i, target):
    left, right = i+1, len(nums)-1
    while left < right:
        if nums[i] + nums[left] + nums[right] == target and is_pythagorean_triplets(nums[i], nums[left], nums[right]):
            return (nums[i], nums[left], nums[right])
        elif nums[i] + nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1
    # default values
    return None, None, None


def is_pythagorean_triplets(a, b, c):
    return a**2 + b**2 == c**2


if __name__ == "__main__":
    print(run())
