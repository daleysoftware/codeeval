import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    for i in range(1, len(test)+1):
        sub_string = test[:i]

        rejoined = "".join(test.split(sub_string))
        if len(rejoined) == 0:
            print len(sub_string)
            break

test_cases.close()
