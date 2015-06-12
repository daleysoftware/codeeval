import sys

fibonacci_cache = {}
def fibonacci_at_position(p):
    if p in fibonacci_cache:
        return fibonacci_cache[p]
    if p == 0:
        result = 0
    elif p == 1:
        result = 1
    else:
        result = fibonacci_at_position(p-1) + fibonacci_at_position(p-2)
    fibonacci_cache[p] = result
    return result

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue
    print(fibonacci_at_position(int(test)))

test_cases.close()
