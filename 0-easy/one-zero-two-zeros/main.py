import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0:continue
        num_zeros = int(test.split(' ')[0])
        num_test = int(test.split(' ')[1])
        result = 0
        for i in range(1, num_test+1):
            binary = '{0:b}'.format(i)
            zeros = binary.count('0')
            if zeros == num_zeros: result += 1
        print(result)
    test_cases.close()

if __name__ == '__main__':
    main()