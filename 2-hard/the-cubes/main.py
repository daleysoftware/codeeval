import sys

class Cube(object):
    def __init__(self, levels):
        self.levels = levels

    @property
    def height(self):
        return len(self.levels)

    def __str__(self):
        result = []
        counter = 0
        for level in self.levels:
            counter += 1
            result.append("Level %i" % counter)
            for row in level: result.append(''.join(row))
            result.append("\n")
        return "\n".join(result)

    def _find_empty_cell_in_border(self, level):
        # Top row.
        for i in xrange(0, self.height):
            if self.levels[level][0][i] == ' ': return 0, i
        # Bottom row.
        for i in xrange(0, self.height):
            if self.levels[level][self.height-1][i] == ' ': return self.height-1, i
        # Sides.
        for i in xrange(1, self.height-1):
            if self.levels[level][i][0] == ' ': return i, 0
            if self.levels[level][i][self.height-1] == ' ': return i, self.height-1
        # Should never reach here if there is an empty cell in the border.
        return None

    @property
    def entrance(self):
        return self._find_empty_cell_in_border(0)

    @property
    def exit(self):
        return self._find_empty_cell_in_border(self.height-1)

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0:
            continue

        height = int(test.split(';')[0])
        levels = zip(*[iter(zip(*[iter(test.split(';')[1])]*height))]*height)

        cube = Cube(levels)

        print "============ %i" % cube.height
        print cube.entrance
        print cube.exit

        # TODO finish this...

    test_cases.close()

if __name__ == '__main__':
    main()