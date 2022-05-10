def run():
    n = 2000000
    # use of sieve of erathosthenes to find prime in range(1,n+1)
    return sieve_and_sum(n)


"""
Problem 10 - Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

"""


def sieve_and_sum(n):
    prime = [True for _ in range(n+1)]
    p = 2

    while (p*p <= n):
        # if prime[p] is not changed, it is a prime

        if prime[p]:

            # update all multiples of p
            for i in range(p**2, n+1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    return sum([i for i, is_prime in enumerate(prime) if is_prime and i >= 2])


if __name__ == "__main__":
    print(run())
