import sys
import re

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    min_heights = {}
    max_heights = {}

    def note_min(index, min_height):
        if index in min_heights:
            min_heights[index] = max(min_heights[index], min_height)
        else:
            min_heights[index] = min_height

    def note_max(index, max_height):
        if index in max_heights:
            max_heights[index] = max(max_heights[index], max_height)
        else:
            max_heights[index] = max_height

    for coord in test.split(';'):
        m = re.match("\(([0-9]+),([0-9]+),([0-9]+)\)", coord.strip())
        l = int(m.group(1))
        h = int(m.group(2))
        r = int(m.group(3))

        note_min(l, 0)
        note_max(l, h)
        note_min(r, 0)
        note_max(r, h)

        for i in xrange(l+1, r):
            note_min(i, h)
            note_max(i, h)

    previous_height = 0
    result = []
    for i in sorted(min_heights.keys()):
        min_height = min_heights[i]
        max_height = max_heights[i]

        if max_height > previous_height:
            previous_height = max_height
            result.append(str(i))
            result.append(str(max_height))
        elif min_height < previous_height:
            previous_height = min_height
            result.append(str(i))
            result.append(str(min_height))

    print " ".join(result)

test_cases.close()
