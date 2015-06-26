import sys

# Determined by the input/output samples.
mapping = {
    'a': 'y',
    'b': 'h',
    'c': 'e',
    'd': 's',
    'e': 'o',
    'f': 'c',
    'g': 'v', # guess
    'h': 'x', # guess
    'i': 'd',
    'j': 'u',
    'k': 'i',
    'l': 'g',
    'm': 'l',
    'n': 'b',
    'o': 'k',
    'p': 'r',
    'q': 'z',
    'r': 't',
    's': 'n',
    't': 'w',
    'u': 'j',
    'v': 'p',
    'w': 'f',
    'x': 'm',
    'y': 'a',
    'z': 'q'}

def get_mapping(char):
    if char == ' ':
        return ' '
    else:
        return mapping[char]

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    output = ""
    for i in range(0, len(test)):
        output += get_mapping(test[i])

    print(output)

test_cases.close()
