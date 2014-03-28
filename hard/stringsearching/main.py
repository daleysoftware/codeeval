import sys

def search(to_search, pattern):
    for i in range(len(to_search)):

        to_search_index = i
        pattern_index = 0

        star = False
        pattern_char_prev = ''

        while True:
            if to_search_index == len(to_search) or pattern_index == len(pattern):
                break

            to_search_char = to_search[to_search_index]
            pattern_char = pattern[pattern_index]

            if pattern_char == '*' and pattern_char_prev != '\\':
                star = True
                pattern_index += 1

            if to_search_char == pattern_char:
                to_search_index += 1
                pattern_index += 1

                if pattern_index == len(pattern):
                    return True

                star = False
            else:
                if star:
                    to_search_index += 1
                    continue
                else:
                    break

    return False

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    to_search = test.split(",")[0]
    pattern = test.split(",")[1]

    print ('true' if search(to_search, pattern) else 'false')

test_cases.close()
