def run():
    sum = 0
    # space-optimized dynamic programming
    n1, n2 = 1, 2
    while n1 <= 4000000:
        if n1 % 2 == 0:
            sum += n1
        n1, n2 = n2, n1+n2
    return sum


if __name__ == "__main__":
    print(run())
