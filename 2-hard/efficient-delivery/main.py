import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    barrels = int(test.split(', ')[1].strip())
    tanker_capacities = [int(x) for x in test.split(', ')[0][1:-1].split(',')]

    # TODO
    pass

test_cases.close()
