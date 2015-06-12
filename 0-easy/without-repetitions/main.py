import sys

def remove_repetitions(text):
    if len(text) == 0: return text
    result = [text[0]]
    for char in text[1:]:
        if char != result[-1]:
            result.append(char)
    return ''.join(result)

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0:
            continue
        print(remove_repetitions(test))
    test_cases.close()

if __name__ == '__main__':
    main()
