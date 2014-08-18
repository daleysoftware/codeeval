import sys

def is_string_all_x(string, x):
    return len(string) > 0 and len(string.replace(x, '')) == 0

def matches(pattern, match):
    if pattern == '0':
        return 'B' not in match
    if pattern == '1':
        a = 'A' in match
        b = 'B' in match
        return not (a and b)
    else:
        raise Exception('pattern to long for matching function')

def check_matching(pattern, match, matching_matrix, row=0, col=0):
    if row >= len(matching_matrix) or col >= len(matching_matrix[row]): return
    if matching_matrix[row][col]: return
    for c in xrange(col, len(match)):
        matching_matrix[row][c] = False
        if matches(pattern[row], match[col:c+1]):
            matching_matrix[row][c] = True
            check_matching(pattern, match, matching_matrix, row+1, c+1)

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        pattern, match = test.strip().split(' ')
        lm, lp = len(match), len(pattern)
        matching_matrix = [[None for m in xrange(lm)] for p in xrange(lp)]
        check_matching(pattern, match, matching_matrix)
        print 'Yes' if matching_matrix[-1][-1] else 'No'
    test_cases.close()

if __name__ == '__main__':
    main()
