import sys

test_cases = open(sys.argv[1], 'r')

def is_overlapping(x1, x2, y1, y2):
    return max(x1, y1) < min(x2, y2)

for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    streets = list(map(int, test.split(' ')[0]
                           .replace('(', '').replace(')', '')
                           .split(',')))
    avenues = list(map(int, test.split(' ')[1]
                           .replace('(', '').replace(')', '')
                           .split(',')))

    max_street = streets[-1] # run
    max_avenue = avenues[-1] # rise

    slope = float(max_avenue) / float(max_street)
    count = 0

    for s in range(0, len(streets)-1):
        for a in range(0, len(avenues)-1):
            x1 = streets[s]
            x2 = streets[s+1]
            y1 = avenues[a]
            y2 = avenues[a+1]

            if is_overlapping(x1, x2, y1/slope, y2/slope):
                count += 1

    print(count)

test_cases.close()
