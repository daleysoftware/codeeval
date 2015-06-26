import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue
    stack = []
    for i in reversed(test.split(' ')):
        if i.isdigit():
            stack.append(i)
        else:
            op1 = float(stack.pop())
            op2 = float(stack.pop())
            if i == '+':
                result = op1 + op2
            elif i == '*':
                result = op1 * op2
            else:
                result = op1 / op2
            stack.append(result)
    print(int(stack.pop()))

test_cases.close()
