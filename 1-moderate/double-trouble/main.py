import sys


def to_hex_repr(s):
    result = []
    for c in s:
        result.append({
            'A': 0x1,
            'B': 0x2,
            '*': 0x0
        }[c])
    return result


def compute_permutations(test):
    x = to_hex_repr(test[1:len(test)//2])
    y = to_hex_repr(test[len(test)//2:])
    result = 1
    for a, b in zip(x, y):
        if a ^ b == 3:
            return 0
        if a == 0 and b == 0:
            result *= 2
    return result


def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0: continue
        print(compute_permutations(test))
    test_cases.close()


if __name__ == '__main__':
    main()
