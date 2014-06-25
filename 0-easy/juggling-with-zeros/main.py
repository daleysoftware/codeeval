import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    test = test.split(' ')
    binary_string = ''

    for i in xrange(0, len(test), 2):
        code = test[i]
        seq = test[i+1]

        if code == '0':
            binary_string += seq
        else:
            binary_string += '1' * len(seq)

    print int(binary_string, 2)

test_cases.close()