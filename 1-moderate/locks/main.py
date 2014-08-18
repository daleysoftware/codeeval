import sys

def do_lock_pass(locked):
    for i in xrange(1, len(locked), 2):
        locked[i] = True

def do_flip_pass(locked):
    for i in xrange(2, len(locked), 3):
        locked[i] = not locked[i]

def count_unlocked(locked):
    result = 0
    for l in locked:
        if not l: result += 1
    return result

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        num_locks = int(test.split(' ')[0])
        num_iterations = int(test.split(' ')[1])
        locked = [False] * num_locks

        for i in xrange(num_iterations-1):
            do_lock_pass(locked)
            do_flip_pass(locked)

        locked[-1] = not locked[-1]
        print count_unlocked(locked)

    test_cases.close()

main()
