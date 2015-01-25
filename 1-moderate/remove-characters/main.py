import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0:
            continue
        words = test.split(',')[0].strip()
        chars = test.split(',')[1].strip()
        for c in chars:
            words = words.replace(c, '')
        print words
    test_cases.close()

if __name__ == '__main__':
    main()
