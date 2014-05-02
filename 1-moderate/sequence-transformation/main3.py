import sys

def pattern_matches(pattern, search, p_index=0, s_index=0,
                    continued=None):
    if p_index >= len(pattern) or s_index >= len(search):
        return False

    if pattern[p_index] == '0':
        possible_patterns = ['A']
    else:
        if continued is not None:
            possible_patterns = [continued]
        else:
            possible_patterns = ['A', 'B']

    if search[s_index] not in possible_patterns:
        return False

    if p_index+1 == len(pattern) and s_index+1 == len(search):
        return True

    return pattern_matches(pattern, search, p_index, s_index+1, search[s_index]) or \
           pattern_matches(pattern, search, p_index+1, s_index+1, None)

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0:
            continue

        pattern = test.split(' ')[0]
        search = test.split(' ')[1]

        if pattern_matches(pattern, search):
            print 'Yes'
        else:
            print 'No'

    test_cases.close()

if __name__ == "__main__":
    main()