import sys

def count_mismatches(s1, s2):
    mismatches = 0
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            mismatches += 1

    return mismatches

def find_matches(dna_segment, dna_sequence, m):
    result = {}
    for i in xrange(len(dna_sequence)):
        seg = dna_sequence[i:i+len(dna_segment)]

        if len(seg) != len(dna_segment):
            continue

        mismatches = count_mismatches(dna_segment, seg)
        if mismatches <= m:
            if mismatches in result:
                result[mismatches].append(seg)
            else:
                result[mismatches] = [seg]

    return result

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    dna_segment = test.split(' ')[0]
    dna_sequence = test.split(' ')[2]
    m = int(test.split(' ')[1])

    result = find_matches(dna_segment, dna_sequence, m)

    if len(result) > 0:
        printable = []
        for mismatches in sorted(result.keys()):
            for seg in sorted(result[mismatches]):
                printable.append(seg)

        print " ".join(printable)
    else:
        print 'No match'

test_cases.close()