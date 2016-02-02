import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0: continue
        card_number = [int(i) for i in list(test.replace(' ', ''))]
        a = 0
        for i in range(0, len(card_number), 2):
            a += card_number[i] * 2
        b = 0
        for i in range(1, len(card_number), 2):
            b += card_number[i]
        print('Real' if (a+b) % 10 == 0 else 'Fake')
    test_cases.close()

if __name__ == '__main__':
    main()
