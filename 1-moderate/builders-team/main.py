import sys
import collections


class PipeGrid(object):
    def __init__(self):
        self.laid_pipes = collections.defaultdict(set)

    @staticmethod
    def _int_to_xy(i):
        return (i-1)//5, (i-1)%5

    def connect(self, i1, i2):
        i1 = PipeGrid._int_to_xy(i1)
        i2 = PipeGrid._int_to_xy(i2)
        self.laid_pipes[i1].add(i2)
        self.laid_pipes[i2].add(i1)

    def _is_connected(self, c1, c2):
        return c2 in self.laid_pipes[c1]

    def _is_connected_square(self, c1, c2):
        # Top
        for c in range(c1[1], c2[1]):
            if not self._is_connected((c1[0], c), (c1[0], c+1)):
                return False
        # Bottom
        for c in range(c1[1], c2[1]):
            if not self._is_connected((c2[0], c), (c2[0], c+1)):
                return False
        # Left side
        for r in range(c1[0], c2[0]):
            if not self._is_connected((r, c1[1]), (r+1, c1[1])):
                return False
        # Right side
        for r in range(c1[0], c2[0]):
            if not self._is_connected((r, c2[1]), (r+1, c2[1])):
                return False
        return True

    def count_complete_squares(self):
        result = 0
        for length in [1, 2, 3, 4]:
            for r in range(0, 5-length):
                for c in range(0, 5-length):
                    if self._is_connected_square((r, c), (r+length, c+length)):
                        result += 1
        return result


def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0: continue
        pg = PipeGrid()
        for i1, i2 in [[int(i) for i in t.strip().split(' ')] for t in test.split("|")]:
            pg.connect(i1, i2)
        print(pg.count_complete_squares())
    test_cases.close()


if __name__ == '__main__':
    main()
