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
    visited = []
    for i in range(rows):
        grid.append([])
        visited.append([])
        for j in range(cols):
            grid[i].append(elements[i * cols + j])
            visited[i].append(False)

    row = 0
    col = 0
    result = [grid[0][0]]
    visited[0][0] = True
    more_to_do = True

    counter = 0
    while more_to_do:
        counter += 1
        if counter > 10:
            break

        more_to_do = False

        # Left to right.
        while col+1 < cols and not visited[row][col+1]:
            col += 1
            result.append(grid[row][col])
            visited[row][col] = True
            if not more_to_do:
                more_to_do = True

         # Top to bottom.
        while row+1 < rows and not visited[row+1][col]:
            row += 1
            result.append(grid[row][col])
            visited[row][col] = True
            if not more_to_do:
                more_to_do = True

        # Right to left.
        while col-1 >= 0 and not visited[row][col-1]:
            col -= 1
            result.append(grid[row][col])
            visited[row][col] = True
            if not more_to_do:
                more_to_do = True

         # Bottom to top.
        while row-1 >= 0 and not visited[row-1][col]:
            row -= 1
            result.append(grid[row][col])
            visited[row][col] = True
            if not more_to_do:
                more_to_do = True

    print " ".join(result)

test_cases.close()