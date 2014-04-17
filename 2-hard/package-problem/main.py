import sys
import re

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    max_weight = float(test.split(':')[0].strip())

    for package in test.split(':')[1].strip().split(' '):
        m = re.match("\((.*),(.*),.(.*)\)", package)

        index = int(m.group(1))
        weight = int(float(m.group(2))*100)
        price = int(m.group(3))

test_cases.close()