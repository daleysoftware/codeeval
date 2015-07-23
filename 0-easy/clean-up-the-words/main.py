import sys
import re

ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0: continue
        result = []
        for char in test:
            result.append(' ' if char not in ALPHABET else char)
        print(re.sub(' +', ' ', ''.join(result).lower()).strip())
    test_cases.close()

if __name__ == '__main__':
    main()
