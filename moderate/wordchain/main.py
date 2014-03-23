import sys
import itertools

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    first_and_last = []
    for word in test.split(','):
        first_and_last.append(word[0] + word[-1])

    # Could probably be smarter about how we find the longest path in a graph,
    # but for now we'll try the permutation approach and see how it performs.
    #
    # ... Turns out this is too slow and will need to be revised.
    permutations = itertools.permutations(first_and_last)
    longest_chain_length = 0
    for p in permutations:
        chain_length = 0

        for i in range(1, len(p)):
            previous = p[i-1]
            current = p[i]

            if previous[1] == current[0]:
                chain_length += 1

        if chain_length > longest_chain_length:
            longest_chain_length = chain_length

    result = 0 if longest_chain_length == 0 else longest_chain_length + 1
    print result

test_cases.close()
