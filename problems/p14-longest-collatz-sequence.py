"""
Problem 14 - Longest Collatz Sequence

The following iterative sequence is defined for the set of positive integers:
    n → n/2 (n is even)
    n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
"""


def run():
    n = 1000000
    longest = 0
    longest_term = 0

    while n > 0:
        num_terms = get_num_collatz_terms(n)
        if num_terms > longest:
            longest_term = n
        longest = max(longest, num_terms)
        n -= 1
    return longest_term


def get_num_collatz_terms(n):
    count = 0
    while n > 0:
        if n % 2 == 0:
            n /= 2
            count += 1
        else:
            n = 3*n + 1
            count += 1

        if n == 1:
            count += 1
            break

    return count


if __name__ == "__main__":
    print(run())
