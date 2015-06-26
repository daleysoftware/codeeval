import sys

"""
Da Vyncy Problem.

It's pretty easy to find a case where maximal overlap does not reconstruct
the message properly. You just need two fragments with identical sections at the
front and back of the string. E.g.

Ax, xBx, xCx

Merge option #1:
    AxBx xCx
    AxBxCx

Merge option #2:
    AxCx xBx
    AxCxBx
"""

compute_max_overlap_cache = {}
def compute_max_overlap(s1, s2):
    """
    Compute the overlap for s1 concatenated with s2.
    """

    key = s1 + s2
    if key in compute_max_overlap_cache:
        return compute_max_overlap_cache[key]

    max_overlap = 0
    for i in range(1, len(s2)):
        if s1.endswith(s2[0:i]):
            max_overlap = i

    compute_max_overlap_cache[key] = max_overlap
    return max_overlap

def find_max_overlapping_fragments(fragments):
    """
    Find the best overlapping pair of fragments. Return the indexes of those
    fragments.
    """
    pair = [-1, -1]
    overlap = 0

    def evaluate_pair(pair, overlap, p, o):
        if o > overlap:
            return p, o
        else:
            return pair, overlap

    for i in range(len(fragments)):
        for j in range(i+1, len(fragments)):
            for p in [[i, j], [j, i]]:
                pair, overlap = evaluate_pair(pair, overlap, p,
                    compute_max_overlap(fragments[p[0]], fragments[p[1]]))

    return overlap, pair

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    fragments = test.split(';')

    while len(fragments) > 1:
        overlap, pair = find_max_overlapping_fragments(fragments)
        if overlap == 0: break

        fragments.append(fragments[pair[0]][:-overlap] + fragments[pair[1]])
        fragments.pop(max(pair[0], pair[1]))
        fragments.pop(min(pair[0], pair[1]))

    # The fragments list may contain some sub-fragments that have no overlap.
    # Choose the longest element to avoid such sub-fragments.
    print(max(fragments, key=len))

test_cases.close()
