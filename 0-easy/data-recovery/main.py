import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue
    scramble = test.split(';')[0].split(' ')
    indexes = test.split(';')[1].split(' ')
    result = {}
    count = 0
    for i in indexes:
        result[i] = scramble[count]
        count += 1
    output = ""
    for i in range(1, len(indexes)+2):
        if str(i) in result:
            output += result[str(i)] + " "
        else:
            output += scramble[-1] + " "
    print(output.strip())

test_cases.close()
