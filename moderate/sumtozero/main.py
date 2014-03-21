import sys
import itertools

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    values = map(int, test.split(','))
    combinations = [list(x) for x in itertools.combinations(values, 4)]

    result = 0
    for c in combinations:
        total = 0
        for i in c:
            total += i

        if total == 0:
            result += 1

    print result

test_cases.close()