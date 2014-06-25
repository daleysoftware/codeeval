import sys
from collections import defaultdict

def distance(s1, s2):
    if len(s1) < len(s2):
        return distance(s2, s1)
    if len(s2) == 0:
        return len(s1)
    previous_row = xrange(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]

def count_friends(word, network, counted=None):
    if counted is None:
        counted = []
    friends = network[word]
    total = 1
    counted.append(word)
    for friend in friends:
        if friend not in counted:
            counted.append(friend)
            t, counted = count_friends(friend, network, counted)
            total += t
    return total, counted

test_cases = open(sys.argv[1], 'r')
tests = []
words = []
in_tests = True
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue
    if test == 'END OF INPUT':
        in_tests = False
        continue
    if in_tests:
        tests.append(test)
    else:
        words.append(test)

dictionary = tests + words
network = defaultdict(list)
for i in xrange(len(dictionary)):
    t1 = dictionary[i]
    network[t1].append(t1)
    for j in xrange(i+1, len(dictionary)):
        t2 = dictionary[j]
        if distance(t1, t2) == 1:
            network[t1].append(t2)
            network[t2].append(t1)

for test in tests:
    friends, counted = count_friends(test, network)
    print max(0, friends-1)

test_cases.close()