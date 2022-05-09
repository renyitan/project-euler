import math


def run():
    target = 10001
    # determine upper_bound, N that contains nth prime
    upper_bound = math.ceil(target*math.log(target*math.log(target)))
    res = sieve(upper_bound)
    return res[target-1]

# use Sieve of Eratosthenes to find nth prime
def sieve(upper_bound):
    prime = [True for i in range(upper_bound+1)]
    prime[0] = False
    prime[1] = False
    p = 2
    while (p*p <= upper_bound):
        # if prime[p] is not changed, then it is a prime
        if prime[p]:
            # update all multiples of p
            for i in range(p*p, upper_bound+1, p):
                prime[i] = False
        p += 1

    res = [i for i, is_prime in enumerate(prime) if is_prime and i >= 2]
    return res


if __name__ == "__main__":
    print(run())
