import sys
import re

def matches(pattern, case):
    pattern = re.sub('\.', '\.', pattern)
    pattern = re.sub('\*', '.*', pattern)
    pattern = re.sub('\?', '.', pattern)
    return re.match('^' + pattern + '$', case) is not None

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0:
            continue
        test = test.split()
        pattern = test[0]
        cases = test[1:]
        results = []
        for case in cases:
            if matches(pattern, case):
                results.append(case)
        print '-' if len(results) == 0 else ' '.join(results)
    test_cases.close()

if __name__ == '__main__':
    main()
