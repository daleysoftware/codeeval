import sys

def compute_column_sum_prefix_matrix(matrix):
    prefix_matrix = []
    for i in range(len(matrix)):
        prefix_matrix.append([0] * len(matrix[i]))
    for c in range(len(matrix[0])):
        for r in range(len(matrix)):
            prefix_matrix[r][c] = prefix_matrix[r-1][c] + matrix[r][c]
    return prefix_matrix

def compute_column_sums_for_rows(prefix_matrix, r1, r2):
    sums = prefix_matrix[r2]
    if r1 != 0:
        for c in range(len(prefix_matrix[r1-1])):
            sums[c] -= prefix_matrix[r1-1][c]
    return sums

def compute_max_sub_sequence_in_array(array):
    max_sum = array[0]
    max_start, max_end = 0, 0
    current_start, current_max_sum = 0, 0
    for current_end in range(0, len(array)):
        current_max_sum += array[current_end]
        if current_max_sum > max_sum:
            max_sum = current_max_sum
            max_start = current_start
            max_end = current_end
        if current_max_sum < 0:
            current_max_sum = 0
            current_start = current_end + 1
    return max_sum, max_start, max_end

def print_matrix(matrix):
    print_sub_matrix(matrix, 0, 0, len(matrix)-1, len(matrix[0])-1)

def print_sub_matrix(matrix, r1, c1, r2, c2):
    for r in range(r1, r2+1):
        line = []
        for c in range(c1, c2+1):
            line.append(str(matrix[r][c]))
        print(' '.join(line))

def main():
    with open(sys.argv[1], 'r') as fh:
        text = fh.read().strip()
    matrix = []
    for line in text.split('\n'):
        row = []
        for value in line.split(' '): row.append(int(value))
        matrix.append(row)
    prefix_matrix = compute_column_sum_prefix_matrix(matrix)
    max_sum = matrix[0][0]
    for r1 in range(0, len(matrix)):
        for r2 in range(r1, len(matrix)):
            sums = compute_column_sums_for_rows(prefix_matrix, r1, r2)
            s, c1, c2 = compute_max_sub_sequence_in_array(sums)
            if s > max_sum: max_sum = s
    print(max_sum)

if __name__ == '__main__':
    main()
