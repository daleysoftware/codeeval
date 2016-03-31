import sys


def find_smallest_sub_matrix_size_with_equal_number_of_ones(grid):
    for length in range(1, len(grid)):
        previous_one_count = -1
        success = True
        for i in range(0, len(grid) + 1 - length):
            for j in range(0, len(grid) + 1 - length):
                one_count = 0
                for k in range(0, length):
                    one_count += sum(grid[i+k][j : j+length])
                if previous_one_count == -1:
                    previous_one_count = one_count
                if previous_one_count != one_count:
                    success = False
                    break
            if not success:
                break
        if success:
            return length, previous_one_count
    return len(grid), sum([sum(row) for row in grid])


def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0: continue
        grid = [[int(i) for i in list(s.strip())] for s in test.split('|')]
        l, s = find_smallest_sub_matrix_size_with_equal_number_of_ones(grid)
        print("%ix%i, %i" % (l, l, s))
    test_cases.close()


if __name__ == '__main__':
    main()
