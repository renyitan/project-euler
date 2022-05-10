"""
Problem 25 - 1000-digit Fibonacci Number

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?


"""


def run():
    # find nth term using memoization
    fib = []
    fib.append(0)  # fib[0]
    fib.append(1)  # fib[1]
    fib.append(1)  # fib[2]

    n = 3
    while True:
        fib_n = fib[n-1] + fib[n-2]
        # check for num digits
        if len(str(fib_n)) >= 1000:
            return n
        fib.append(fib_n)
        n += 1


if __name__ == "__main__":
    print(run())
