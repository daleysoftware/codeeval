import sys


class GridSize(object):
    def __init__(self, xy):
        self.x, self.y = xy


class Point(object):
    def __init__(self, xy):
        self.x, self.y = xy


def count_nuts(grid_size, destination):
    #grid = [[0 for y in range(grid_size.y)] for x in range(grid_size.x)]
    # TODO finish this.
    return 0


def main(input_filename):
    test_cases = open(input_filename, 'r')
    for test in test_cases:
        test = test.strip()
        grid_size = GridSize([int(x) for x in test.split('|')[0].strip().split('x')])
        destination = Point([int(x) for x in test.split('|')[1].strip().split(' ')])
        print(count_nuts(grid_size, destination))
    test_cases.close()


if __name__ == '__main__':
    main(sys.argv[1])

