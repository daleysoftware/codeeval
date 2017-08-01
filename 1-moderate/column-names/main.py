import sys
import math

OFFSET = ord('A')
ALPHABET_LENGTH = 26

def convert_to_excel_column_name(number):
    number -= 1

    result = []
    while number >= 0:
        quotient, remainder = divmod(number, ALPHABET_LENGTH)
        result.append(chr(OFFSET + remainder))
        number = quotient - 1
    return ''.join(reversed(result))

def main(input_filename):
    test_cases = open(input_filename, 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0:
            continue
        number = int(test)
        print(convert_to_excel_column_name(number))
    test_cases.close()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python %s <input_filename>" % sys.argv[0])
        sys.exit(1)
    main(sys.argv[1])
