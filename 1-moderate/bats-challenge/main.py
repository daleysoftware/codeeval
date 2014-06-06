import sys

def use(bat, used, d):
    for i in xrange(max(0, bat-d+1), min(len(used), bat+d)):
        used[i] = True

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    l = int(test.split(' ')[0])
    d = int(test.split(' ')[1])
    n = int(test.split(' ')[2])
    bats = map(int, test.split(' ')[3:])

    used = [False] * (l+1)

    for i in xrange(0, 6):
        used[i] = True
    for i in xrange(len(used)-6, len(used)):
        used[i] = True
    for bat in bats:
        use(bat, used, d)

    additional_bats = 0
    for i in range(0, l):
        if not used[i]:
            additional_bats += 1
            use(i, used, d)

    print additional_bats

test_cases.close()