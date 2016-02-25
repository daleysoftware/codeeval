import sys

def stupid_sort(array, iterations):
    for i in range(iterations):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                tmp = array[j]
                array[j] = array[j+1]
                array[j+1] = tmp
                break
    return array

def main(input_filename):
    test_cases = open(input_filename, 'r')
    for test in test_cases:
        array, iterations = test.strip().split('|')
        array = [int(i) for i in array.split()]
        iterations = int(iterations.strip())
        stupid_sort(array, iterations)
        print(' '.join([str(s) for s in array]))
    test_cases.close()

if __name__ == '__main__':
    main(sys.argv[1])
