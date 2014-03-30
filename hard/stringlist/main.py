import sys
import itertools

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    length = int(test.split(',')[0])
    chars = test.split(',')[1]

    triple_chars = []
    for c in chars:
        for i in range(length):
            triple_chars.append(c)

    result = []
    for i in itertools.permutations(triple_chars, length):
        result.append("".join(i))

    result = list(set(result))
    result.sort()
    print ",".join(result)

test_cases.close()
