import sys
import time
import operator

def is_range_overlapping(x1, x2, y1, y2):
    return x1 <= y2 and y1 <= x2

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    pattern = '%b %Y'
    ranges = []
    for date_range in test.split(';'):
        date1 = date_range.strip().split('-')[0]
        date2 = date_range.strip().split('-')[1]

        epoch1 = int(time.mktime(time.strptime(date1, pattern)))
        epoch2 = int(time.mktime(time.strptime(date2, pattern)))

        ranges.append([epoch1, True])
        ranges.append([epoch2, False])

    ranges = sorted(ranges, key=operator.itemgetter(0))
    queue = [ranges[0][0]]
    result = 0

    for i in range(1, len(ranges)):
        epoch = ranges[i][0]
        starting = ranges[i][1]

        if starting:
            queue.append(epoch)
        else:
            if len(queue) == 1:
                months_diff = round(((epoch - queue[0]) * 12 / 3.15569e7) + 1)
                result += int(months_diff)

            queue.pop()

    print int(result / 12)

test_cases.close()