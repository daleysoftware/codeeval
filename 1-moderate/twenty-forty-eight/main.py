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
        # Shift such that we only have to handle LEFT-ward movement.
        {
            Direction.UP: lambda: self._rotate(3),
            Direction.RIGHT: lambda: self._rotate(2),
            Direction.DOWN: lambda: self._rotate(1),
            Direction.LEFT: lambda: None
        }[direction]()
        # Handle only LEFT-ward movement.
        for row in range(self.length):
            last_unmerged_col = 0
            for col in range(1, self.length):
                value = self.board_status[row][col]
                if value != 0:
                    if self.board_status[row][last_unmerged_col] == 0:
                        self.board_status[row][last_unmerged_col] = value
                        self.board_status[row][col] = 0
                    elif self.board_status[row][last_unmerged_col] == value:
                        self.board_status[row][last_unmerged_col] *= 2
                        self.board_status[row][col] = 0
                        last_unmerged_col += 1
                    elif last_unmerged_col+1 != col:
                        # Values are not equal, both non-zero, and not adjacent
                        self.board_status[row][last_unmerged_col+1] = self.board_status[row][col]
                        self.board_status[row][col] = 0
                        last_unmerged_col += 1
                    else:
                        # Values are not equal, both non-zero, and are adjacent
                        pass
                        last_unmerged_col += 1
        # Shift back to original orientation.
        {
            Direction.UP: lambda: self._rotate(1),
            Direction.RIGHT: lambda: self._rotate(2),
            Direction.DOWN: lambda: self._rotate(3),
            Direction.LEFT: lambda: None
        }[direction]()
        return self

    def _rotate(self, count=1):
        """
        Rotate the board 90 degrees clockwise.
        """
        new_board_status = [[0 for _ in range(self.length)] for _ in range(self.length)]
        for i in range(self.length):
            for j in range(self.length):
                new_board_status[j][self.length-i-1] = self.board_status[i][j]
        self.board_status = new_board_status
        if count > 1:
            self._rotate(count-1)

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
