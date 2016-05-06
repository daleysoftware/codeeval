import sys
import itertools


def generate_operator_options(current = ''):
    if len(current) == 4:
        return [current]
    result = []
    result += generate_operator_options(current + '+')
    result += generate_operator_options(current + '-')
    result += generate_operator_options(current + '*')
    return result


OPERATOR_OPTIONS = generate_operator_options()


def perform_operation(op, a, b):
    return {
        '+': a + b,
        '*': a * b,
        '-': a - b
    }[op]


def can_evaluate_to_42(numbers):
    for p in itertools.permutations(numbers):
        for op in OPERATOR_OPTIONS:
            result = perform_operation(op[0], p[0], p[1])
            result = perform_operation(op[1], result, p[2])
            result = perform_operation(op[2], result, p[3])
            result = perform_operation(op[3], result, p[4])
            if result == 42:
                return True
    return False


def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0: continue
        numbers = [int(t.strip()) for t in test.split(' ')]
        if can_evaluate_to_42(numbers):
            print('YES')
        else:
            print('NO')
    test_cases.close()


if __name__ == '__main__':
    main()
