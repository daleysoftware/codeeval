import sys

class Matrix:
    def __init__(self, rows, cols, array):
        self.rows = rows
        self.cols = cols
        self.array = array

    def count_adjacent_mines(self, row, col):
        result = 0
        # Upper row
        result += self.is_mine(row-1, col-1)
        result += self.is_mine(row-1, col)
        result += self.is_mine(row-1, col+1)
        # Lower row
        result += self.is_mine(row+1, col-1)
        result += self.is_mine(row+1, col)
        result += self.is_mine(row+1, col+1)
        # Left side
        result += self.is_mine(row, col-1)
        # Right side
        result += self.is_mine(row, col+1)
        return result

    def is_mine(self, row, col):
        if row < 0 or row >= self.rows:
            return False
        if col < 0 or col >= self.cols:
            return False
        return self.array[row][col]

def parse_matrix(line):
    rows = int(line.split(';')[0].split(',')[0])
    cols = int(line.split(';')[0].split(',')[1])
    line = line.split(';')[1].strip()
    array = []
    for r in range(rows):
        sub_array = []
        for c in range(cols):
            sub_array.append(True if line[r * cols + c] == '*' else False)
        array.append(sub_array)
    return Matrix(rows, cols, array)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue
    m = parse_matrix(test)
    result = ""
    for r in range(m.rows):
        for c in range(m.cols):
            if m.array[r][c]:
                result += '*'
            else:
                result += str(m.count_adjacent_mines(r, c))
    print(result)

test_cases.close()
