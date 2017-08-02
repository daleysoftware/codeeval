import sys


def cocktail_sort(l, iterations):
    for i in range(iterations):
        for j in range(i, len(l)-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
        for j in range(len(l)-i-2, i-1, -1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l


def main(input_filename):
    test_cases = open(input_filename, 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0:
            continue
        l = [int(x) for x in test.split('|')[0].strip().split(' ')]
        iterations = int(test.split('|')[1].strip())
        print(' '.join([str(x) for x in cocktail_sort(l, iterations)]))
    test_cases.close()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python %s <input_filename>" % sys.argv[0])
    main(sys.argv[1])
