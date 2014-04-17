import sys
import re

def is_balanced(message):
    minOpen = 0
    maxOpen = 0
 
    for i in xrange(len(message)):
        if message[i] == '(':
            maxOpen += 1
            if i == 0 or message[i-1] != ':':
                minOpen += 1
        elif message[i] == ')':
            minOpen = max(0, minOpen-1)
            if i == 0 or message[i-1] != ':':
                maxOpen -= 1
                if maxOpen < 0:
                    break
 
    if maxOpen >= 0 and minOpen == 0:
        return "YES"
    else:
        return "NO"

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    print is_balanced(test)

test_cases.close()
