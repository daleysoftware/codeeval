import sys

# TODO finish
mapping = {
    'r': 't',
    'b': 'h',
    'c': 'e',
    'v': 'p'
}

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    print test

test_cases.close()
