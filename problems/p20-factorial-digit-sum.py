def run():
    fac = 1
    for i in range(2, 100+1):
        fac *= i
    sum = 0
    while fac > 0:
        sum += fac % 10
        fac //= 10
    return sum


if __name__ == "__main__":
    print(run())
