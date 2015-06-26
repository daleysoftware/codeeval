import sys

def get_all_possible_words(alphabet, length, prefix=""):
    if len(prefix) == length:
        return [prefix]

    result = []
    for c in alphabet:
        r = get_all_possible_words(alphabet, length, prefix + c)

        for i in r:
            result.append(i)

    return result

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    length = int(test.split(',')[0])
    chars = test.split(',')[1]

    alphabet = set()
    for c in chars:
        alphabet.add(c)

    print(",".join(sorted(get_all_possible_words(alphabet, length))))

test_cases.close()
