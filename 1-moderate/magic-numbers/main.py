import sys
import collections

def has_duplicate_characters(string):
    char_to_count = collections.defaultdict(int)
    for s in list(string):
        char_to_count[s] += char_to_count[s] + 1
    for i in char_to_count.values():
        if i != 1:
            return True
    return False

def do_magic_traversal(ints, current):
    step = ints[current]
    if step is None:
        return
    ints[current] = None
    current = (current + step) % len(ints)
    do_magic_traversal(ints, current)

def is_magic(number):
    if has_duplicate_characters(str(number)):
        return False
    ints = [int(x) for x in list(str(number))]
    do_magic_traversal(ints, ints[0] % len(ints))
    for i in ints:
        if i is not None:
            return False
    return True

def main(input_filename):
    test_cases = open(input_filename, 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0:
            continue
        a, b = [int(x) for x in test.split(' ')]
        magics = []
        for i in range(a, b+1):
            if is_magic(i):
                magics.append(i)
        if len(magics) == 0:
            print(-1)
        else:
            print(' '.join([str(m) for m in magics]))
    test_cases.close()

if __name__ == '__main__':
    main(sys.argv[1])
