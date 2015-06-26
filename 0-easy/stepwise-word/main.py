import sys

def stepwise(word):
    result = []
    for i in range(len(word)):
        result.append('*' * i + word[i])
    return ' '.join(result)

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0: continue
        test = test.split(' ')
        test.sort(key=lambda item: len(item), reverse=True)
        print(stepwise(test[0]))

    test_cases.close()

if __name__ == '__main__':
    main()
