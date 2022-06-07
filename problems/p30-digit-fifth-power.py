"""
P-30 Digit Fifth Power

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

def run():
    power = 5
    limit = (9**power) * (power-1)
    res = 0
    for n in range(limit, 2, -1):
        digits = [ch for ch in str(n)]
        print(digits)
        if sum([int(d)**power for d in digits]) == n:
            
            res+=int("".join(digits))
      
    return res


if __name__ == "__main__":
    print(run())
