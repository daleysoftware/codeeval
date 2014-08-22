import sys

def do_bubble_sort_n_times(l, n):
    n = min(n, len(l)-1)
    while n > 0:
        n -= 1
        for i in xrange(len(l)-1):
            if l[i] > l[i+1]:
                temp = l[i]
                l[i] = l[i+1]
                l[i+1] = temp
    return l

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0: continue
        l = [int(x) for x in test.split(' | ')[0].split(' ')]
        n = int(test.split(' | ')[1])
        result = do_bubble_sort_n_times(l, n)
        print ' '.join([str(x) for x in result])
    test_cases.close()

if __name__ == '__main__':
    main()
