import sys
import re
import operator
import copy

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0: continue
    # Capacity.
    W = int(test.split(':')[0].strip())#*100
    packages = []
    for package in test.split(':')[1].strip().split(' '):
        m = re.match("\((.*),(.*),.(.*)\)", package)
        i = int(m.group(1))
        w = int(float(m.group(2)))#*100
        v = int(m.group(3))
        packages.append((i, w, v))
    packages.sort(key=operator.itemgetter(1))
    # We use the 0/1 knapsack problem dynamic programming solution. See Wiki.
    m = [[0] * (W+1) for i in xrange(len(packages))]
    used = [[list()] * (W+1) for i in xrange(len(packages))]
    def weight(us):
        r = 0
        for x in us: r += packages[x][1]
        return r
    for i in xrange(len(packages)):
        wi = packages[i][1]
        vi = packages[i][2]
        for j in xrange(W+1):
            def use_o2():
                m[i][j] = o2
                s = copy.deepcopy(used[i-1][j-wi])
                s.append(i)
                used[i][j] = s
            def use_o1():
                m[i][j] = o1
                used[i][j] = copy.copy(used[i-1][j])
            o1 = m[i-1][j]
            if wi <= j:
                o2 = m[i-1][j-wi] + vi
                if o1 < o2:
                    use_o2()
                elif o1 == o2:
                    w1 = weight(used[i-1][j])
                    w2 = weight(used[i-1][j-w1]) + wi
                    if w1 < w2:
                        use_o1()
                    else:
                        use_o2()
                else:
                    use_o1()
            else:
                use_o1()
    # Print the result, sorted and pretty.
    result = [str(i) for i in sorted([packages[u][0] for u in used[-1][-1]])]
    print '-' if len(used[-1][-1]) == 0 else ','.join(result)

test_cases.close()