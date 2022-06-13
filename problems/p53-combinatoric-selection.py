"""
[Problem Title]

There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, (5 3) = 10

In general, 
(n r) = n! / r!(n-r)!, where r<= n, n! = n * (n-1) * ... * 3 * 2 * 1 and 0! = 1

It is not until n = 23, that a value exceeds one-million: 

How many, not necessarily distinct, values of (n r) for 1 <= n <= 100 are greater than one-million?
"""
import math


def combinations(n, r):
    return (math.factorial(n))/(math.factorial(r) * (math.factorial(n-r)))


def run():
    n_limit = 100
    count = 0

    for n in range(1, n_limit+1):
        
        for r in range(n+1):
            print(n,r)
            if combinations(n,r) > 1000000:
                count+=1
    print(count)
    


if __name__ == "__main__":
    print(run())
