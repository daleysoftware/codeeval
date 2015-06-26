import sys

def count_double_squares(x):
    if x == 0: return 1
    result = 0
    for b in range(0, int(x ** 0.5)+1):
        a = int((x - (b ** 2)) ** 0.5)
        if a < b: break
        if x == a ** 2 + b ** 2: result += 1
    return result

test_cases = open(sys.argv[1], 'r')
first = True

for test in test_cases:
    test = test.strip()
    if len(test) == 0: continue
    if first:
        first = False
        continue
    x = int(test)
    print(count_double_squares(x))

test_cases.close()
