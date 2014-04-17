import sys

def get_possible_patterns(pattern, prefix, index):
    c = pattern[index]

    if index+1 == len(pattern):
        if c == '1':
            return [prefix + 'A', prefix + 'B']
        else:
            return [prefix + 'A']

    result = get_possible_patterns(pattern, prefix + 'A', index+1)
    if c == '1':
        result.extend(get_possible_patterns(pattern, prefix + 'B', index+1))

    return result

def aggregate(x):
    aggregated = []

    previous_chr = x[0]
    previous_cnt = 1

    for c in x[1:]:
        if c == previous_chr:
            previous_cnt += 1
        else:
            aggregated.append([previous_chr, previous_cnt])
            previous_cnt = 1

        previous_chr = c

    aggregated.append([previous_chr, previous_cnt])
    return aggregated

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    pattern = test.split(' ')[0]
    search = test.split(' ')[1]

    aggregated_search = aggregate(search)

    # The 1s are either an A or a B. Just go through all of the options.
    match = False
    for p in get_possible_patterns(pattern, "", 0):
        aggregated_patten = aggregate(p)

        if len(aggregated_patten) != len(aggregated_search):
            continue

        for i in xrange(len(aggregated_search)):
            letter_match = aggregated_search[i][0] == aggregated_patten[i][0]
            count_okay = aggregated_patten[i][1] < aggregated_search[i][1]

            if letter_match and count_okay:
                match = True
                break

        if match:
            break

    if match:
        print "Yes"
    else:
        print "No"

test_cases.close()
