import sys
from datetime import datetime

FMT = '%H:%M:%S'

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0:
            continue
        test = test.split(' ')
        t1 = test[0]
        t2 = test[1]

        if t1 > t2:
            delta = datetime.strptime(t1, FMT) - datetime.strptime(t2, FMT)
        else:
            delta = datetime.strptime(t2, FMT) - datetime.strptime(t1, FMT)

        print "%.2d:%.2d:%.2d" % (delta.seconds/3600, (delta.seconds/60)%60, delta.seconds%60)

    test_cases.close()

if __name__ == '__main__':
    main()