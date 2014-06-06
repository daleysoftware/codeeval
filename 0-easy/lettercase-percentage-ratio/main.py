import sys
test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    lower = 0
    upper = 0
    for character in test:
        if character.islower():
            lower += 1
        else:
            upper += 1

    lower = float(lower) / len(test) * 100
    upper = float(upper) / len(test) * 100
    print "lowercase: %.2f uppercase: %.2f" % (lower, upper)

test_cases.close()
