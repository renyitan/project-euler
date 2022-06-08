"""
Problem 41 - Pandigital Prime

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

def is_n_pandigital(n):
    digits = [ch for ch in str(n)]
    nums = {str(k):1 for k in range(1,len(digits)+1)}
    for ch in digits:
        nums[ch] = nums.get(ch, 0) - 1
        if nums[ch] < 0:
            return False
    return all(x == 0 for x in nums.values())

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
        print(p)
        

    return [i for i, is_prime in enumerate(prime) if is_prime and i >= 2]

def run():
    primes = sieve(987654321)
    for n in range(len(primes)-1, -1, -1):
        if is_n_pandigital(n):
            return n
    
    


if __name__ == "__main__":
    print(run())
