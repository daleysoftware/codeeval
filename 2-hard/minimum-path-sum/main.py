import sys

class Matrix:
    def __init__(self, array):
        self.rows = len(array)
        self.cols = len(array[0])
        self.array = array

    def calculate_min_top_down_path(self):
        return self.calculate_min_top_down_path_impl(0, 0)

    def calculate_min_top_down_path_impl(self, row, col):
        if row >= self.rows or row < 0:
            return 0
        if col >= self.cols or col < 0:
            return 0

        if row+1 == self.rows and col+1 == self.cols:
            return self.array[row][col]

        result1 = self.calculate_min_top_down_path_impl(row+1, col)
        result2 = self.calculate_min_top_down_path_impl(row, col+1)

        if row+1 == self.rows:
            return result2 + self.array[row][col]
        if col+1 == self.cols:
            return result1 + self.array[row][col]

        return min(result1, result2) + self.array[row][col]

def parse_matrix(n, input_stream):
    matrix = []

    for i in range(n):
        line = input_stream.readline().split(',')

        row = []
        for r in line:
            row.append(int(r))

        matrix.append(row)

    return Matrix(matrix)

test_cases = open(sys.argv[1], 'r')
while True:
    line = test_cases.readline()
    if len(line) == 0:
        break

    n = int(line)
    matrix = parse_matrix(n, test_cases)

    print matrix.calculate_min_top_down_path()

test_cases.close()