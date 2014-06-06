import sys
import re

def render_word(a, b):
    result = ['_'] * len(b)
    found = b.find(a)
    for i in range(found, found + len(a)): result[i] = a[i-found]
    return "".join(result)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    utterance1 = re.sub(' +', ' ', test.split(';')[1]).split(' ')
    utterance2 = re.sub(' +', ' ', test.split(';')[0]).split(' ')

    index = 0
    result = []
    success = False

    for a in range(len(utterance1)):
        wA = utterance1[a]

        if index == len(utterance2):
            success = False
            break

        for b in range(index, len(utterance2)):
            wB = utterance2[b]
            index = b+1
            if wA in wB:
                success = True
                result.append(render_word(wA, wB))
                break
            else:
                result.append('_' * len(wB))

    if not success:
        print 'I cannot fix history'
        continue

    result_length = len(result)
    if result_length != len(utterance2):
        for i in range(result_length, len(utterance2)):
            result.append('_' * len(utterance2[i]))

    print " ".join(result)

test_cases.close()
