import sys

# Hard-coded input grid:
# [
#  [ABCE],
#  [SFCS],
#  [ADEE]
# ]
grid = [['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']]

print len(grid)

def has_matching_word(grid, word, row, col):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print grid[i][j]
    return True

def has_matching_word(grid, word):
    return has_matching_word(grid, word, 0, 0)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    print has_matching_word(grid, test)

test_cases.close()
