"""
Problem 15 - Lattice Path

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
"""


def run():
    # use combinatorics - binomial coefficients
    # https://www.mathblog.dk/project-euler-15/

    grid_size = 20
    paths = 1

    for i in range(grid_size):
        paths *= (2 * grid_size) - i
        paths /= i + 1
    return int(paths)


if __name__ == "__main__":
    print(run())
