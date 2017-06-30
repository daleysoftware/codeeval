import sys


def sort_lexicographic(s):
    return sorted(s)


def reverse_burrows_wheeler_transform(s):
    array = sort_lexicographic(list(s))
    for i in range(len(s)-1):
        for j in range(len(s)):
            array[j] = s[j] + array[j]
        array = sort_lexicographic(array)
    for a in array:
        if a[-1] == '$':
            return a
    return None


def main(input_filename):
    test_cases = open(input_filename, 'r')
    for test in test_cases:
        test = test.strip().strip('|')
        if len(test) == 0:
            continue
        print(reverse_burrows_wheeler_transform(test))
    test_cases.close()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python %s <input_filename>" % sys.argv[0])
        sys.exit(1)
    main(sys.argv[1])
