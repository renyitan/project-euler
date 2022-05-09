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
