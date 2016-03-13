import sys


def is_lucky(number):
    digits = [int(x) for x in list(str(number))]
    if len(digits) % 2 != 0:
        return False
    sum1 = sum(digits[0:len(digits)//2])
    sum2 = sum(digits[len(digits)//2:])
    return sum1 == sum2


def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0: continue
        length = int(test)
        result = 0
        for i in range(0, 10 ** length):
            result += is_lucky('0' * (length - len(str(i))) + str(i))
        print(result)
    test_cases.close()


if __name__ == '__main__':
    main()
