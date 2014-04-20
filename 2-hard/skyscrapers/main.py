import sys
import re

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    heights = {}

    def note_height(index, ma):
        if index in heights:
            heights[index] = max(heights[index], ma)
        else:
            heights[index] = ma

    for coord in test.split(';'):
        m = re.match("\(([0-9]+),([0-9]+),([0-9]+)\)", coord.strip())
        l = int(m.group(1))
        h = int(m.group(2))
        r = int(m.group(3))

        # Going up!
        note_height(l, h)
        # Going down!
        note_height(r, 0)

        for i in xrange(l+1, r):
            note_height(i, h)

    previous_height = 0
    result = []

    for i in sorted(heights.keys()):
        height = heights[i]

        if height != previous_height:
            previous_height = height
            result.append(str(i))
            result.append(str(height))

    print " ".join(result)

test_cases.close()
