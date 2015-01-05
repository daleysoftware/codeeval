import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0: continue
        # TODO
        print test
    test_cases.close()

if __name__ == '__main__':
    main()
