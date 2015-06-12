import sys
import math

# N.B. there are lots of good solutions to this problem available on
# http://stackoverflow.com/questions/42519/how-do-you-rotate-a-two-dimensional-array

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0: continue
        test = test.split(' ')
        n = int(math.sqrt(len(test)))
        matrix = [test[i:i+n] for i in range(0, len(test), n)]
        rotated = zip(*matrix[::-1])
        print(' '.join([' '.join(row) for row in rotated]))
    test_cases.close()

if __name__ == '__main__':
    main()
