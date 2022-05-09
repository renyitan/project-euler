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
