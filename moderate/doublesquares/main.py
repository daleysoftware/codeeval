import sys

def count_double_squares(x):
    result = 0
    for b in range(0, int(x ** 0.5)):
        a = int((x - (b ** 2)) ** 0.5)

        if a < b:
            break
        if x == a ** 2 + b ** 2:
            result += 1

    return result

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    x = int(test)

    if x == 0:
        print 1
    else:
        print count_double_squares(x)

test_cases.close()