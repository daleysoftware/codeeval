import sys


def gray_to_binary(num):
    result = num
    num >>= 1
    while num != 0:
        result ^= num
        num >>= 1
    return result


def main(input_filename):
    test_cases = open(input_filename, 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0:
            continue
        print(' | '.join([str(gray_to_binary(int(x.strip(), 2))) for x in test.split('|')]))
    test_cases.close()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python %s <input_filename>" % sys.argv[0])
    main(sys.argv[1])
