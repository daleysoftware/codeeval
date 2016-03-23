import sys


mersenne = [3, 7, 31, 127, 2047]


def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0:
            continue
        test = int(test)
        result = []
        for m in mersenne:
            if test > m:
                result.append(m)
        print(', '.join([str(r) for r in result]))
    test_cases.close()


if __name__ == '__main__':
    main()
