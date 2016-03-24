import sys


def row_matrix_to_col_matrix(row_matrix):
    col_matrix = []
    for c in range(len(row_matrix)): col_matrix.append([])
    for r in range(len(row_matrix)):
        for c in range(len(row_matrix)):
            col_matrix[c].append(row_matrix[r][c])
    return col_matrix


def col_matrix_to_row_matrix(col_matrix):
    row_matrix = []
    for r in range(len(col_matrix)): row_matrix.append([])
    for c in range(len(col_matrix)):
        for r in range(len(col_matrix)):
            row_matrix[r].append(col_matrix[c][r])
    return row_matrix


def matrix_compare(a, b):
    length = min(len(a), len(b))
    index = 0
    while index < length:
        if a[index] != b[index]:
            return a[index] - b[index]
        index += 1
    return 0


def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0: continue
        m = row_matrix_to_col_matrix([[int(i) for i in s.strip().split(' ')] for s in test.split('|')])
        print(' | '.join([' '.join([str(e) for e in r]) for r in col_matrix_to_row_matrix(sorted(m, cmp=matrix_compare))]))
    test_cases.close()


if __name__ == '__main__':
    main()
