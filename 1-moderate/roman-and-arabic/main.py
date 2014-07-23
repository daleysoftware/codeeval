import sys

def compute_ar_value(ar):
    assert len(ar) == 2
    a = int(ar[0])
    r = ar[1]
    r = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }[r]
    return a * r

def compute_aromatic_value(aromatic):
    values = []
    for ar in aromatic: values.append(compute_ar_value(ar))
    result = 0
    for i in xrange(0, len(aromatic)-1):
        if compute_ar_value("1" + aromatic[i][1]) < compute_ar_value("1" + aromatic[i+1][1]):
            result -= values[i]
        else:
            result += values[i]
    return result + values[-1]

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue
    print compute_aromatic_value([test[i:i+2] for i in range(0, len(test), 2)])

test_cases.close()
