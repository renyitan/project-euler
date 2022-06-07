"""
[Problem Title]

[Problem Description]
"""
import math
from collections import deque

def is_prime(n: int) -> list[int]:
    if n <= 3:
        return n > 1
    # check if n is a multiple of 2 or 3
    if not n % 2 or not n % 3:
        return False
    i = 5
    stop = int(math.sqrt(n))
    while i <= stop:
        if not n % i or not n % (i+2):
            return False
        i += 6
    return True


def run():
    res = []
    limit = 12
    n = 11
    while len(res) < limit:
        if is_prime(n):
            digits = [ch for ch in str(n)]
            print(digits)
            is_trunc = True
            left_copy = digits.copy()

            # remove left elements
            while len(left_copy) > 0:
                left_copy.pop()
                if len(left_copy) == 0:
                    break
                
                if not is_prime(int("".join(left_copy))):
                    is_trunc = False
                    break
            
            # remove right elements
            right_copy = digits.copy()
            while len(right_copy) > 0:
                right_copy.pop(0)
                if len(right_copy) == 0:
                    break
                if not is_prime(int("".join(right_copy))):
                    is_trunc = False
                    break

            if is_trunc:
                res.append(n)
        n+=1

    return sum(res)



if __name__ == "__main__":
    print(run())
