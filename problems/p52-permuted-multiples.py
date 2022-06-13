"""
Problem 52 - Permuted Multiples

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

import collections
def run():
    n = 1
    multiple = 6
    is_perm = False
    
    while not is_perm:
        print(n)
        res = []
        counter = collections.Counter(str(n))
        
        for i in range(2, multiple+1):
            num = n*i
            res.append(collections.Counter(str(num)))
        
        is_perm = all(obj == counter for obj in res)
            
        if is_perm:
            break

        n+=1

if __name__ == "__main__":
    print(run())
