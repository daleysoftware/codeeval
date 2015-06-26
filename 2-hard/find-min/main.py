import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue
    test_split = test.split(',')
    n = int(test_split[0])
    k = int(test_split[1])
    a = int(test_split[2])
    b = int(test_split[3])
    c = int(test_split[4])
    r = int(test_split[5])
    m = [a]
    for i in range(1, k):
        m.append((b * m[i-1] + c) % r)
    for i in range(k, n):
        s = sorted(m)
        found = False
        smallest = 0
        while not found:
            if smallest not in s:
                break
            else:
                smallest += 1
        m.append(smallest)
        m.pop(0)
    print(m[-1])
test_cases.close()
