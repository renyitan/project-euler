def run():
    n = 600851475143
    factor = 1
    while factor < n:
        factor += 2
        while n % factor == 0:
            n /= factor
    return factor


if __name__ == "__main__":
    print(run())
