import sys
import collections

def distance(s1, s2):
    if len(s1) < len(s2): return distance(s2, s1)
    if len(s2) == 0: return len(s1)
    previous_row = range(len(s2) + 1)
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
    result = collections.defaultdict(list)
    for i in range(len(dna_sequence)):
        seg = dna_sequence[i:i+len(dna_segment)]
        if len(seg) != len(dna_segment): break
        mismatches = distance(dna_segment, seg)
        if mismatches <= m: result[mismatches].append(seg)
    return result

def main():
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
            print(" ".join(printable))
        else:
            print('No match')
    test_cases.close()

if __name__ == '__main__':
    main()
