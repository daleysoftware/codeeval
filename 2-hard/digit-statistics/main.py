import sys
import collections

# This is the trick: take advantage of the multiplicative pattern.
def get_cycle(number):
    cycle = []
    current = number
    while current not in cycle:
        cycle.append(current)
        current = (current * number) % 10
    return cycle

def get_digits(a, n):
    cycle = get_cycle(a)
    digits = collections.defaultdict(int)
    cycle_repeats = n/len(cycle)
    remaining = n - cycle_repeats * len(cycle)
    for c in cycle:
        digits[c] = cycle_repeats
    for i in range(1, int(remaining + 1)):
        digit = cycle[(i-1)%len(cycle)]
        digits[digit] += 1
    return digits

def print_pretty_default_dict(d):
    result = []
    for i in range(0, 10):
        result.append("%i: %i" % (i, d[i]))
    print(', '.join(result))

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0:
            continue
        a = int(test.split(' ')[0])
        n = int(test.split(' ')[1])
        digits = get_digits(a, n)
        print_pretty_default_dict(digits)
    test_cases.close()

if __name__ == '__main__':
    main()
