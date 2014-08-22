import sys

def main():
    with open(sys.argv[1], 'r') as test_cases:
        for test in test_cases:
            # TODO finish this.
            print test.strip()

if __name__ == '__main__':
    main()
