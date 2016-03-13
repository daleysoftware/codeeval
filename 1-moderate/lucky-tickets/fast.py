import sys
import copy


cache = {1: {0:1, 1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1, 9:1}}


def compute_sum_of_digits_map(digits):
    if digits in cache:
        return cache[digits]
    previous = compute_sum_of_digits_map(digits - 1)
    result = copy.deepcopy(previous)
    for i in range(1, 10):
        for key in previous.keys():
            if key+i not in result:
                result[key+i] = 0
            result[key+i] += previous[key]
    cache[digits] = result
    return result


def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0: continue
        digits = int(test)//2
        sum_of_digits_map = compute_sum_of_digits_map(digits)
        print(sum([a*b for a,b in zip(sum_of_digits_map.values(), sum_of_digits_map.values())]))
    test_cases.close()


if __name__ == '__main__':
    main()
