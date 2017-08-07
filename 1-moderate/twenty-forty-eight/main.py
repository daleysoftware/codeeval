import sys
from enum import Enum


class Direction(Enum):
    UP = 1
    LEFT = 2
    DOWN = 3
    RIGHT = 4


class Board(object):
    def __init__(self, length, board_status):
        self.length = length
        self.board_status = board_status

    def move(self, direction):
        # TODO
        return self

    def __str__(self):
        return '|'.join(' '.join(str(y) for y in x) for x in self.board_status)


def main(input_filename):
    test_cases = open(input_filename, 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0:
            continue
        direction = Direction[test.split(';')[0].strip()]
        length = int(test.split(';')[1].strip())
        board_status = [[int(y) for y in x.strip().split(' ')] for x in test.split(';')[2].split('|')]
        print(Board(length, board_status).move(direction))
    test_cases.close()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python %s <input_filename>" % sys.argv[0])
    main(sys.argv[1])
