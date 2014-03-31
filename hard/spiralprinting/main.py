import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    rows = int(test.split(";")[0])
    cols = int(test.split(";")[1])
    elements = test.split(";")[2].split(' ')

    grid = []
    for i in range(rows):
        grid.append([])
        for j in range(cols):
            grid[i].append(elements[i * cols + j])

    top = 0
    right = cols-1
    bottom = rows-1
    left = 0

    more_to_do = True
    current_row = 0
    current_col = 0

    result = []
    while more_to_do:
        more_to_do = False

        # Left to right.
        while current_col < right:
            result.append(grid[current_row][current_col])
            current_col += 1
            if not more_to_do:
                more_to_do = True
        right -= 1

         # Top to bottom.
        while current_row < bottom:
            result.append(grid[current_row][current_col])
            current_row += 1
            if not more_to_do:
                more_to_do = True
        bottom -= 1

        # Right to left.
        while current_col > left:
            result.append(grid[current_row][current_col])
            current_col -= 1
            if not more_to_do:
                more_to_do = True
        left += 1

         # Bottom to top.
        while current_row > top:
            result.append(grid[current_row][current_col])
            current_row -= 1
            if not more_to_do:
                more_to_do = True
        top += 1

    result.append(grid[current_row][current_col])
    print " ".join(result)

test_cases.close()