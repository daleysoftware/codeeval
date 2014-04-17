import sys
import re

test_cases = open(sys.argv[1], 'r')

def decode_letter_mapping_list(mapper, values):
    result = []
    for v in values:
        result.append(decode_letter_mapping(mapper, v))
    return result

def decode_letter_mapping(mapper, value):
    result = ""
    for c in value:
        index = ord(c) - ord('a')
        result += mapper[index]
    return int(result)

for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    mapper = test.split(' ')[0]
    expression = test.split(' ')[1]

    operands = decode_letter_mapping_list(
            mapper,
            expression.replace('+', ' ').replace('-', ' ').split(' '))
    operators = list(re.sub('[a-z]+', '', expression))

    result = operands[0]
    for i in range(1, len(operands)):
        operand = operands[i]
        operator = operators[i-1]

        if operator == '+':
            result += operand
        else:
            result -= operand

    print result

test_cases.close()
