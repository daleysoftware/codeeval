import sys
test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    elements = (test.split(','))
    elements.sort(key=int)

    freq = 0
    previous = 0
    found = False

    for i in elements:
        if freq == 0 or i == previous:
            freq += 1
        else:
            freq = 1

        previous = i

        if freq > (len(elements)/2):
            found = True
            print i
            break

    if not found:
        print None

test_cases.close()
