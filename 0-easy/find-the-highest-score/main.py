import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0: continue
        table = [[int(r) for r in row.split(' ')] for row in test.split(' | ')]
        maxes = [None] * len(table[0])
        for column in range(len(maxes)):
            for row in range(len(table)):
                v = table[row][column]
                maxes[column] = v if maxes[column] is None else max(v, maxes[column])
        print(' '.join([str(m) for m in maxes]))
    test_cases.close()

if __name__ == '__main__':
    main()