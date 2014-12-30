import sys

ROOM_SIZE = 10

class Point(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col

class Element(object):
    WALL = '#'
    HOLE = 'o'
    PRISM = '*'
    EMPTY = ' '
    LIGHT_X = 'X'
    LIGHT_BACK = '\\'
    LIGHT_FORWARD = '/'

class Room(object):
    def __init__(self, schematic):
        self.schematic = schematic

    def __str__(self):
        return '\n'.join(''.join(x) for x in self.schematic)

    def _element(self, point):
        return self.schematic[point.row][point.col]

    @property
    def hole(self):
        # TODO
        return Point(0, 0)

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0: continue
        room = Room(zip(*[iter(test)]*ROOM_SIZE))
        print room
        # TODO
    test_cases.close()

if __name__ == '__main__':
    main()