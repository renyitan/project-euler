"""
Problem 42 - Coded Triangle Numbers

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""

import math
import string

def is_triangular(n):
    if (n < 0):
        return False

    c,b,a = (-2 * n), 1,1
    d = (b * b) - (4 * a * c)

    if (d < 0):
        return False

    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)

    if (root1 > 0 and math.floor(root1) == root1):
        return True

    if (root2 > 0 and math.floor(root2) == root2):
        return True

    return False

def run():
    with open('p042_words.txt') as f:
        for line in f:
            words = line.split(",")
            words = [word.lower().strip('"') for word in words]
            break
    
    # dict containing letters as key as value from 1-26
    letters = dict(zip(string.ascii_lowercase, range(1,27)))

    count = 0

    for word in words:
        num = sum([letters[char] for char in word])
        if is_triangular(num):
            count+=1


    return count
    


if __name__ == "__main__":
    print(run())
