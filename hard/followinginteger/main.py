import sys

def get_digits_ignore_zero(x):
    digits = {}
    for digit in str(x):
        if digit == '0':
            continue

        if digit in digits:
            digits[digit] += 1
        else:
            digits[digit] = 1

    return digits

def following_integer(x):
    original_digits = get_digits_ignore_zero(x)
    while True:
        x += 1
        digits = get_digits_ignore_zero(x)

        if original_digits == digits:
            return x

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    test = int(test)
    print following_integer(test)

test_cases.close()
