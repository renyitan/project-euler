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
