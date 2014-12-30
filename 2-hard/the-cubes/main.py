import sys
import enum
import collections

class Element(enum.Enum):
    WALL = 1
    HOLE = 2
    FLOOR = 3

CHAR_TO_ELEMENT_ENUM = {
    '*': Element.WALL,
    'o': Element.HOLE,
    ' ': Element.FLOOR
}

class Point(object):
    def __init__(self, level, row, col):
        self.level = level
        self.row = row
        self.col = col

    def adjacent_to(self, point):
        return abs(self.level-point.level) + abs(self.row-point.row) + abs(self.col-point.col) == 1

    @property
    def adjacent_points(self):
        return [
            Point(self.level-1, self.row,   self.col),
            Point(self.level+1, self.row,   self.col),
            Point(self.level,   self.row-1, self.col),
            Point(self.level,   self.row+1, self.col),
            Point(self.level,   self.row,   self.col-1),
            Point(self.level,   self.row,   self.col+1)
        ]

    def __eq__(self, other):
        return self.level == other.level and self.row == other.row and self.col == other.col

    def __str__(self):
        return "(%i,%i,%i)" % (self.level, self.row, self.col)

class Cube(object):
    def __init__(self, levels):
        self.levels = levels

    @property
    def length(self):
        return len(self.levels)

    def __str__(self):
        result = []
        counter = 0
        for level in self.levels:
            result.append("Level %i" % counter)
            counter += 1
            for row in level: result.append(''.join(row))
            result.append("")
        return "\n".join(result).strip()

    def _find_empty_cell_in_border(self, level):
        # Top row.
        for i in range(0, self.length):
            if self.levels[level][0][i] == ' ': return Point(level, 0, i)
        # Bottom row.
        for i in range(0, self.length):
            if self.levels[level][self.length-1][i] == ' ': return Point(level, self.length-1, i)
        # Sides.
        for i in range(1, self.length-1):
            if self.levels[level][i][0] == ' ': return Point(level, i, 0)
            if self.levels[level][i][self.length-1] == ' ': return Point(level, i, self.length-1)
        # Should never reach here if there is an empty cell in the border.
        return None

    @property
    def entrance(self):
        return self._find_empty_cell_in_border(0)

    @property
    def exit(self):
        return self._find_empty_cell_in_border(self.length-1)

    def _element(self, point):
        if point.level < 0 or point.row < 0 or point.col < 0 or \
           point.level >= self.length or point.row >= self.length or point.col >= self.length:
            return Element.WALL
        return CHAR_TO_ELEMENT_ENUM[self.levels[point.level][point.row][point.col]]

    def _can_travel(self, point_from, point_to):
        # Precondition.
        if self._element(point_from) == Element.WALL or self._element(point_to) == Element.WALL:
            return False

        # Adjacency.
        if not point_from.adjacent_to(point_to):
            return False

        # Various semantic cases, depending on levels.
        if point_from.level == point_to.level:
            return True
        elif point_from.level == point_to.level + 1:
            # "from" is one level above "to", i.e. we are moving down.
            return self._element(point_from) == Element.HOLE
        elif point_from.level + 1 == point_to.level:
            # "from" is one level below "to", i.e. we are moving up.
            return self._element(point_to) == Element.HOLE
        else:
            return False

    def _compute_min_steps(self, visited, current):
        if current == self.exit: return 1
        visited[(current.level, current.row, current.col)] = True
        result = []
        for possible_next in current.adjacent_points:
            if not visited[(possible_next.level, possible_next.row, possible_next.col)] and self._can_travel(current, possible_next):
                result.append(self._compute_min_steps(visited, possible_next))
        visited[(current.level, current.row, current.col)] = False
        result = [x for x in result if x > 0]
        if len(result) == 0: return 0
        return 1 + min(result)

    @property
    def min_steps(self):
        visited = collections.defaultdict(lambda: False)
        return self._compute_min_steps(visited, self.entrance)

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0: continue
        length = int(test.split(';')[0])
        levels = list(zip(*[iter(zip(*[iter(test.split(';')[1])]*length))]*length))
        cube = Cube(levels)
        print(cube.min_steps)
    test_cases.close()

if __name__ == '__main__':
    main()