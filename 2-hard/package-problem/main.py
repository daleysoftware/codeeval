import sys

def compute_total_value_and_weight(used, items):
    total_value = 0
    total_weight = 0
    for i in xrange(len(used)):
        if used[i]:
            value, weight = items[i]
            total_value += value
            total_weight += weight
    return total_value, total_weight

def compute_best_packaging(max_weight, items, best_value=0, best_weight=float('inf'), best_used=None, prefix=None):
    if prefix is None: prefix = []

    if len(prefix) == len(items):
        value, weight = compute_total_value_and_weight(prefix, items)

        if weight < max_weight and (value > best_value or (value == best_value and weight < best_weight)):
            return value, weight, prefix
        else:
            return best_value, best_weight, best_used

    best_value, best_weight, best_used = compute_best_packaging(max_weight, items, best_value, best_weight, best_used, prefix + [False])
    best_value, best_weight, best_used = compute_best_packaging(max_weight, items, best_value, best_weight, best_used, prefix + [True])

    return best_value, best_weight, best_used

def main():
    with open(sys.argv[1], 'r') as test_cases:
        for test in test_cases:
            # Parsing.
            items = []
            for i in test.split(':')[1].strip().split(' '):
                value = int(i.split(',')[2][1:-1])
                weight = int(float(i.split(',')[1]) * 100)
                items.append((value, weight))
            max_weight = int(test.split(':')[0].strip()) * 100

            best_value, best_weight, best_used = compute_best_packaging(max_weight, items)

            result = []
            for i in xrange(len(best_used)):
                if best_used[i]: result.append(i)
            if len(result) == 0:
                print '-'
            else:
                print ','.join([str(x+1) for x in sorted(result)])

if __name__ == '__main__':
    main()
