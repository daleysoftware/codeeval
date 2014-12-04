import sys

def double_and_sum(digit):
    digit = int(digit)
    digit *= 2
    digit = str(digit)
    if len(digit) == 1:
        return int(digit)
    else:
        return int(digit[0]) + int(digit[1])

def is_valid(card_number):
    card_number = card_number[::-1]
    even = False
    total = 0
    for digit in card_number:
        digit = int(digit)
        if even:
            digit = double_and_sum(digit)
        even = not even
        total += digit
    return total % 10 == 0

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0:
            continue
        test = test.replace(' ', '')
        print '1' if is_valid(test) else '0'

    test_cases.close()

if __name__ == '__main__':
    main()