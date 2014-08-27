import sys

class memoized(dict):
    def __init__(self, func):
        super(memoized, self).__init__()
        self.func = func
    def __call__(self, *args):
        return self[args]
    def __missing__(self, key):
        result = self[key] = self.func(*key)
        return result

def knapsack(items, max_weight):
    """
    Solve the knapsack problem by finding the most valuable sub-sequence of
    `items` subject that weighs no more than `max_weight`.
    """
    @memoized
    def best_value(i, j):
        if i == 0: return 0
        value, weight = items[i - 1]
        if weight > j:
            return best_value(i - 1, j)
        else:
            return max(best_value(i - 1, j),
                       best_value(i - 1, j - weight) + value)

    # TODO need to fix the case where we get an identical value and diff weight.
    # This effectively finds the best value, but not necessarily the best
    # weight.
    j = max_weight
    result = []
    for i in xrange(len(items), 0, -1):
        if best_value(i, j) != best_value(i - 1, j):
            result.append(i)
            j -= items[i - 1][1]
    return best_value(len(items), max_weight), result

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

            # Use knapsack solution, above, to find our result.
            result_value, result_items = knapsack(items, max_weight)
            if len(result_items) == 0:
                print '-'
            else:
                print ','.join([str(x) for x in sorted(result_items)])

if __name__ == '__main__':
    main()
