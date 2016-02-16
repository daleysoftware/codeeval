import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        print(' '.join(["{0:.3f}".format(x) for x in sorted([float(i) for i in test.strip().split(' ')])]))
    test_cases.close()

if __name__ == '__main__':
    main()
