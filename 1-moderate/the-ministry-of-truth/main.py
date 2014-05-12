import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    # TODO finish
    utterance1 = test.split(';')[0]
    utterance2 = test.split(';')[1]

    print '---'
    print utterance1
    print utterance2

test_cases.close()
