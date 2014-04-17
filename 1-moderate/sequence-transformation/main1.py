import sys
import re

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    pattern = test.split(' ')[0]
    search = test.split(' ')[1]

    regex = ""
    for c in pattern:
        if c == '0':
            regex += "A+"
        else:
            regex += "[A+|B+]"

    if re.match(regex, search):
        print 'Yes'
    else:
        print 'No'

test_cases.close()