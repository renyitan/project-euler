"""
Sieve of Eratosthenes
- Find all prime numbers within range [1,n]
https://www.geeksforgeeks.org/sieve-of-eratosthenes/
"""


def eratosthenes(n):
    # create boolean array and assume all values are prime
    prime = [True for _ in range(n+1)]
    p = 2

    while (p*p <= n):
        # if prime[p] is not changed, then it is a prime
        if prime[p]:
            # update all multiples of p
            for i in range(p*p, n+1, p):
                prime[i] = False
        p += 1
    
    return [i for i, is_prime in enumerate(prime) if is_prime and i >= 2]
