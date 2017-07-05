import sys


l1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
l2 = ['u', 'v', 'w', 'x', 'y', 'z', 'n', 'o', 'p', 'q', 'r', 's', 't']


def decode(s):
    result = []
    for char in s:
        if char in l1:
            result.append(l2[l1.index(char)])
        else:
            result.append(l1[l2.index(char)])
    return ''.join(result)


def main(input_filename):
    test_cases = open(input_filename, 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0:
            continue
        print(decode(test))
    test_cases.close()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python %s <input_filename>" % sys.argv[0])
        sys.exit(1)
    main(sys.argv[1])