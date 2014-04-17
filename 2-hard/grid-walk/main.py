
def key_for_x_y(x, y):
    return str(x) + "," + str(y)

def can_visit(x, y):
    x = abs(x)
    y = abs(y)

    value = 0

    for digit in str(x):
        value += int(digit)
    for digit in str(y):
        value += int(digit)

    return value <= 19

def is_visited(x, y, visited):
    return key_for_x_y(x, y) in visited

def count_accessible_coordinates(x, y, visited):
    if not can_visit(x, y) or is_visited(x, y, visited):
        return 0

    visited.add(key_for_x_y(x, y))

    result = 1

    result += count_accessible_coordinates(x+1, y,   visited)
    result += count_accessible_coordinates(x,   y+1, visited)
    result += count_accessible_coordinates(x-1, y,   visited)
    result += count_accessible_coordinates(x,   y-1, visited)

    return result

visited = set()
print count_accessible_coordinates(0, 0, visited)
