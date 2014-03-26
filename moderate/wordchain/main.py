import sys
import itertools

# TODO (MP) need to improve this -- it's too slow.
def find_longest_chain_length_directed_maybe_cyclic_graph(graph):
    permutations = itertools.permutations(graph)

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
    return result


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    graph = []
    for word in test.split(','):
        graph.append(word[0] + word[-1])

    result = find_longest_chain_length_directed_maybe_cyclic_graph(graph)

    if result == 0:
        print 'None'
    else:
        print result

test_cases.close()
