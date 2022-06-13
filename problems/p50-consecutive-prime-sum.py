"""
Problem 50 - Consecutive Prime sum

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

def sieve(n: int) -> list[int]:
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

def run():
    limit = 1000000
    primes = sieve(limit)
    longest=0
    left = 0
    current = 0
    prime_sum = 0

    for right in range(len(primes)):
        while current+primes[right] >= limit:
            is_prime = current in primes
            
            if is_prime and len(primes[left:right]) >= longest:
                longest = len(primes[left:right])
                prime_sum = current
            
            current-= primes[left]
            left+=1

        current+= primes[right]

        if current in primes:
            if len(primes[left:right+1]) < longest:
                break
            longest = len(primes[left:right+1])
            prime_sum = current

    return prime_sum, longest
        
if __name__ == "__main__":
    print(run())
