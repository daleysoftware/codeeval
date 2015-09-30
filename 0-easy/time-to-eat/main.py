import sys
import datetime

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0: continue
        times = []
        for t in test.split(' '):
            times.append((t, datetime.datetime.strptime(t, "%H:%M:%S")))
        print(' '.join([x[0] for x in sorted(times, key=lambda x: x[1], reverse=True)]))
    test_cases.close()

if __name__ == '__main__':
    main()