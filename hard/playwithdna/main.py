import sys

def distance(s1, s2):
    if len(s1) < len(s2):
        return distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = xrange(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

def find_matches(dna_segment, dna_sequence, m):
    result = {}
    for i in xrange(len(dna_sequence)):
        for length in xrange(max(1, len(dna_segment)-m), len(dna_segment)+m):
            seg = dna_sequence[i:i+length]

            if len(seg) != len(dna_segment):
                continue

            mismatches = distance(dna_segment, seg)
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