import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    binary =  "{0:b}".format(int(test))
    total = 0

    for b in binary:
        if b == "1":
            total += 1

    print total % 3

test_cases.close()
