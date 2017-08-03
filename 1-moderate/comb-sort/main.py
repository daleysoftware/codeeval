import sys


def compute_comb_sort_iterations(array):

    gap = len(array)
    shrink = 1.25
    is_sorted = False
    iterations = 0

    while not is_sorted:
        gap = int(gap / shrink)
        iterations += 1
        if gap > 1:
            is_sorted = False
        else:
            gap = 1
            is_sorted = True
        i = 0
        while i + gap < len(array):
            if array[i] > array[i+gap]:
                array[i], array[i+gap] = array[i+gap], array[i]
                is_sorted = False
            i += 1
    return iterations-1


def main(input_filename):
    test_cases = open(input_filename, 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0:
            continue
        array = [int(x) for x in test.strip().split(' ')]
        print(compute_comb_sort_iterations(array))
    test_cases.close()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python %s <input_filename>" % sys.argv[0])
    main(sys.argv[1])
