def run():
    # use bit shift to compute 2**1000
    digits = [int(u) for u in str(1 << 1000)]
    return sum(digits)


if __name__ == "__main__":
    print(run())
