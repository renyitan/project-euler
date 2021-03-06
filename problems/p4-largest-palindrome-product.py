"""
Problem 4 - Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
import math


def run():
    max_palindrome = -math.inf
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            current_max = i * j
            if current_max > max_palindrome and is_palindrome(current_max):
                max_palindrome = current_max
    return max_palindrome


def is_palindrome(n):
    chars = [ch for ch in str(n)]
    return chars == chars[::-1]


if __name__ == "__main__":
    print(run())
