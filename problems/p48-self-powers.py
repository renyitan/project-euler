
"""
Problem 48 - Self Powers

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

def run():
    res = 0
    for i in range(1,1001):
        res += (i**i)
    digits = [ch for ch in str(res)]
    return "".join(digits[-1:-1])


if __name__ == "__main__":
    print(run())
