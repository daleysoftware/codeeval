import sys

test_cases = open(sys.argv[1], 'r')

big_digits = [
    # Zero - 0
    ['-**-',
     '*--*',
     '*--*',
     '*--*',
     '-**-'],
    # One - 1
    ['--*-',
     '-**-',
     '--*-',
     '--*-',
     '-***'],
    # Two - 2
    ['***-',
     '---*',
     '-**-',
     '*---',
     '****'],
    # Three - 3
    ['***-',
     '---*',
     '-**-',
     '---*',
     '***-'],
    # Four - 4
    ['-*--',
     '*--*',
     '****',
     '---*',
     '---*'],
    # Five - 5
    ['****',
     '*---',
     '***-',
     '---*',
     '***-'],
    # Six - 6
    ['-**-',
     '*---',
     '***-',
     '*--*',
     '-**-'],
    # Seven - 7
    ['****',
     '---*',
     '--*-',
     '-*--',
     '-*--'],
    # Eight - 8
    ['-**-',
     '*--*',
     '-**-',
     '*--*',
     '-**-'],
    # Nine - 9
    ['-**-',
     '*--*',
     '-***',
     '---*',
     '-**-']
]

for test in test_cases:
    test = test.strip()
    if len(test) == 0: continue
    digits = []
    for t in test:
        if t.isdigit(): digits.append(int(t))

    for line in xrange(0, 5):
        for d in digits:
            sys.stdout.write(big_digits[d][line])
            sys.stdout.write('-')
        print
    print '-----' * len(digits)

test_cases.close()
