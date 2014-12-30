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
        print cube

        # TODO finish this...

    test_cases.close()

if __name__ == '__main__':
    main()