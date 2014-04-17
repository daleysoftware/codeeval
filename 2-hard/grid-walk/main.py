import collections

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n /= 10
    return s

def can_visit(p):
    value = sum_digits(abs(p[0])) + sum_digits(abs(p[1]))
    return value <= 19

def is_visited(p, visited):
    return p in visited

def neighbors(p):
    x, y = p
    return [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]

def count_accessible_coordinates():
    visited = {(0, 0)}
    queue = collections.deque([(0, 0)])

    while len(queue) > 0:
        p = queue.pop()

        for n in neighbors(p):
            if not is_visited(n, visited) and can_visit(n):
                visited.add(n)
                queue.append(n)

    return len(visited)

print count_accessible_coordinates()
