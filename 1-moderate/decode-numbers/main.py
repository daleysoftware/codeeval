import sys

def count_possible_decoding(message):
    if len(message) == 1 or len(message) == 0:
        return 1
    possibilities = 0
    num_chars = 1
    while True:
        chars = message[0:num_chars]
        if len(chars) != num_chars: break
        if int(chars) > 26: break
        possibilities += count_possible_decoding(message[num_chars:])
        num_chars += 1
    return possibilities

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue
    print(count_possible_decoding(test))

test_cases.close()
