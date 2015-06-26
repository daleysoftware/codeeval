import sys

VOCAB = ' !"#$%&\'()*+,-./0123456789:<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0: continue
        shifts = [int(x) for x in list(test.split(';')[0])]
        enciphered = test.split(';')[1]
        result = []
        for i in range(0, len(enciphered)):
            shift = shifts[i % len(shifts)]
            position = VOCAB.index(enciphered[i])
            char = VOCAB[(position - shift) % len(VOCAB)]
            result.append(char)
        print(''.join(result))
    test_cases.close()

if __name__ == '__main__':
    main()
