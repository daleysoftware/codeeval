import sys

ways = {1: 1, 2: 2}
def count_ways_to_climb(stairs):
    if stairs in ways:
        return ways[stairs]

    result = count_ways_to_climb(stairs-1) + count_ways_to_climb(stairs-2)
    ways[stairs] = result
    return result

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    print count_ways_to_climb(int(test))

test_cases.close()