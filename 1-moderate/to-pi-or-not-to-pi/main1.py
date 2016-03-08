import sys


# http://stackoverflow.com/questions/9004789/1000-digits-of-pi-in-python
def make_pi():
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    for j in range(21604): # experimentation to determine the loop value needed for 5k digits.
        if 4 * q + r - t < m * t:
            yield m
            q, r, t, k, m, x = 10 * q, 10 * (r - m * t), t, k, (10 * (3 * q + r)) // t - 10 * m, x
        else:
            q, r, t, k, m, x = q * k, (2 * q + r) * x, t * x, k + 1, (q * (7 * k + 2) + r * x) // (t * x), x + 2


def main():
    test_cases = open(sys.argv[1], 'r')
    digits = []
    for i in make_pi():
        digits.append(str(i))
    for test in test_cases:
        test = test.strip()
        if len(test) == 0: continue
        print(digits[int(test)-1])
    test_cases.close()


if __name__ == '__main__':
    main()
