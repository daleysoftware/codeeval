import sys
import re
import math

def is_ugly(x):
    return x == 0 or x % 7 == 0 or x % 5 == 0 or x % 3 == 0 or x % 2 == 0

def get_possibilities(length, prefix="", current=0):
    if current == length:
        return []
    if current+1 == length:
        return [prefix+' ', prefix+'+', prefix+'-']

    poss = []
    poss.extend(get_possibilities(length, prefix+' ', current+1))
    poss.extend(get_possibilities(length, prefix+'+', current+1))
    poss.extend(get_possibilities(length, prefix+'-', current+1))
    return poss

def evaluate_expression(expr):
    v = expr[0]
    for i in range(1, len(expr), 2):
        op = expr[i]
        value = expr[i+1]
        if op == '+':
            v += value
        else:
            v -= value
    return v

def count_uglies(num):
    possibilities = get_possibilities(len(num)-1)

    digits = []
    for d in num:
        digits.append(int(d))

    if len(digits) == 1:
        if is_ugly(digits[0]):
            return 1
        else:
            return 0

    expressions = []
    for p in possibilities:
        expr = [digits[0]]
        for i in range(1, len(digits)):
            if p[i-1] == ' ':
                expr[-1] = int(math.copysign(1, expr[-1]) * (abs(expr[-1] * 10) + digits[i]))
            else:
                expr.append(p[i-1])
                expr.append(digits[i])
        expressions.append(expr)

    uglies_count = 0
    for expr in expressions:
        value = evaluate_expression(expr)
        if is_ugly(value):
            uglies_count += 1

    return uglies_count

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    l1 = len(test)
    test = re.sub("^0+", "0", test)
    l2 = len(test)

    print(count_uglies(test) * (3 ** (l1-l2)))

test_cases.close()
