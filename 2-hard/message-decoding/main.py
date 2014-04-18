import sys
import re

def int_to_binary_string(x, length=0):
    formatter = "{:0" + str(length) + "b}"
    return formatter.format(x)

def zero_string_of_length(length):
    result = ""
    for i in xrange(length):
        result += "0"
    return result

def is_all_ones(s):
    for c in s:
        if c != '1':
            return False
    return True

key_cache = {}
def get_key_for_index(index):
    if index in key_cache:
        return key_cache[index]

    if index == 0:
        result = zero_string_of_length(1)
    else:
        previous = get_key_for_index(index-1)
        previous_plus_one = int_to_binary_string(int(previous, 2) + 1,
                                                 len(previous))

        if is_all_ones(previous_plus_one):
            result = zero_string_of_length(len(previous) + 1)
        else:
            result = previous_plus_one

    key_cache[index] = result
    return result

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    s1 = re.search("0", test)
    s2 = re.search("1", test)
    start = min(s1.start(), s2.start())

    header = test[0:start]
    data = test[start:]

    mapping = {}
    index = 0
    for c in header:
        key = get_key_for_index(index)
        mapping[key] = c
        index += 1

    index = 0
    result = ""

    while True:
        length = int(data[index:index+3], 2)
        index += 3
        if length == 0: break

        while True:
            c = data[index:index+length]
            index += length
            if is_all_ones(c): break
            result += mapping[c]

    print result

test_cases.close()