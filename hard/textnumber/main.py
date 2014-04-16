import sys

def millions_to_number(text):
    result = 0
    split = text.split("million")
    for m in split[:-1]:
        result += thousands_to_number(m) * (10**6)
    return result + thousands_to_number(split[-1])

def thousands_to_number(text):
    result = 0
    split = text.split("thousand")
    for m in split[:-1]:
        result += hundreds_to_number(m) * 1000
    return result + hundreds_to_number(split[-1])

def hundreds_to_number(text):
    result = 0
    split = text.split("hundred")
    for m in split[:-1]:
        result += tens_to_number(m) * 100
    return result + tens_to_number(split[-1])

def tens_to_number(tens):
    tens = tens.strip()

    if len(tens) == 0:
        return 0

    result = 0
    for i in tens.split(' '):
        result += {
            'zero':      0,
            'one' :      1,
            'two':       2,
            'three':     3,
            'four':      4,
            'five':      5,
            'six':       6,
            'seven':     7,
            'eight':     8,
            'nine':      9,
            'ten':       10,
            'eleven':    11,
            'twelve':    12,
            'thirteen':  13,
            'fourteen':  14,
            'fifteen':   15,
            'sixteen':   16,
            'seventeen': 17,
            'eighteen':  18,
            'nineteen':  19,
            'twenty':    20,
            'thirty':    30,
            'forty':     40,
            'fifty':     50,
            'sixty':     60,
            'seventy':   70,
            'eighty':    80,
            'ninety':    90
        }[i]

    return result


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    negative = False
    if "negative" in test:
        negative = True
        test = test.replace("negative ", "").strip()

    result = millions_to_number(test)
    if negative:
        print (0-result)
    else:
        print result

test_cases.close()