import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    a = int(test.split(' ')[0])
    n = int(test.split(' ')[1])
    an = str(a**n)

    digits = {}
    for c in an:
        c = int(c)
        if c in digits:
            digits[c] += 1
        else:
            digits[c] = 1

    result = []
    for i in range(10):
        x = 0 if i not in digits else digits[i]
        result.append("%i: %i" % (i, x))

    print ", ".join(result)

test_cases.close()