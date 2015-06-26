grid = [[False, False, False, False],
        [False, False, False, False],
        [False, False, False, False],
        [False, False, False, False]]

def count_paths(grid, current_x, current_y, end_x, end_y):
    if current_x < 0 or current_x > 3 or current_y < 0 or current_y > 3:
        return 0

    if grid[current_x][current_y]:
        return 0

    if current_x == end_x and current_y == end_y:
        return 1

    grid[current_x][current_y] = True

    result = 0

    result += count_paths(grid, current_x+1, current_y,   end_x, end_y)
    result += count_paths(grid, current_x,   current_y+1, end_x, end_y)
    result += count_paths(grid, current_x-1, current_y,   end_x, end_y)
    result += count_paths(grid, current_x,   current_y-1, end_x, end_y)

    grid[current_x][current_y] = False

    return result

print(count_paths(grid, 0, 0, 3, 3))
