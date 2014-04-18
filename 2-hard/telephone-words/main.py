import sys

def get_telephone_words(number, prefix, index):
    if index == len(number):
        return [prefix]

    options = {
        '0': '0',
        '1': '1',
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }[number[index]]

    result = []

    for o in options:
        result.extend(get_telephone_words(number, prefix + o, index+1))

    return result

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    print ",".join(sorted(get_telephone_words(test, "", 0)))

test_cases.close()
