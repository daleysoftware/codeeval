import sys

PRIMES = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}


def count_possible_necklace_arrangements(beads, pos):
    if len(beads) == pos:
        return 1 if 1 + beads[- 1] in PRIMES else 0
    result = 0
    if beads[pos] + beads[pos-1] in PRIMES:
        result += count_possible_necklace_arrangements(beads, pos + 1)
    for i in range(pos+2, len(beads), 2):
        if beads[pos-1] + beads[i] in PRIMES:
            beads[i], beads[pos] = beads[pos], beads[i]
            result += count_possible_necklace_arrangements(beads, pos + 1)
            beads[i], beads[pos] = beads[pos], beads[i]
    return result


def main(input_filename):
    test_cases = open(input_filename, 'r')
    for test in test_cases:
        test = test.strip().strip('|')
        if len(test) == 0:
            continue
        print(count_possible_necklace_arrangements(list(range(1, int(test)+1)), 1))
    test_cases.close()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python %s <input_filename>" % sys.argv[0])
        sys.exit(1)
    main(sys.argv[1])