import sys

def format_text(text):
    result = ''
    uppercase = True
    for character in text:
        if character.isalpha():
            result += character.upper() if uppercase else character.lower()
            uppercase = not uppercase
        else:
            result += character
    return result

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    print format_text(test)
