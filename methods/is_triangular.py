"""
Determines if a number, n is a triangular number
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1);
"""
import math


def is_triangular(n):
    if (n < 0):
        return False

    # Considering the equation n*(n+1)/2 = num
    # The equation is : a(n^2) + bn + c = 0
    c = (-2 * n)
    b, a = 1, 1
    d = (b * b) - (4 * a * c)

    if (d < 0):
        return False

    # Find roots of equation
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)

    # checking if root1 is natural
    if (root1 > 0 and math.floor(root1) == root1):
        return True

    # checking if root2 is natural
    if (root2 > 0 and math.floor(root2) == root2):
        return True

    return False
