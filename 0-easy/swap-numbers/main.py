import sys

def swap_numbers(word):
    return word[-1] + word[1:-1] + word[0]

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        print(' '.join([swap_numbers(word) for word in test.strip().split(' ')]))
    test_cases.close()

if __name__ == '__main__':
    main()
