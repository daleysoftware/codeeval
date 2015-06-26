import sys

def count_sub_strings(str1, str2):
    if len(str1) < len(str2):
        return 0
    if str1 == str2 or len(str2) == 0:
        return 1
    result = 0
    if str1[0] == str2[0]:
        result += count_sub_strings(str1[1:], str2[1:])
    return result + count_sub_strings(str1[1:], str2)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue
    str1 = test.split(',')[0]
    str2 = test.split(',')[1]
    print(count_sub_strings(str1, str2))

test_cases.close()
