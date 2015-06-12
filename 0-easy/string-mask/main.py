import sys

def main(input_filename):
    test_cases = open(input_filename, 'r')
    for test in test_cases:
        test = test.strip()
        word = list(test.split(' ')[0])
        mask = list(test.split(' ')[1])
        result = []
        for m, w in zip(mask, word):
            if m == '1':
                result.append(w.upper())
            else:
                result.append(w.lower())
        print(''.join(result))
    test_cases.close()

if __name__ == '__main__':
    main(sys.argv[1])
