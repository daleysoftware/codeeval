import sys
import copy
import collections

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
    if counted is None: counted = set()
    # Return zero if we have already been counted.
    if word in counted: return 0, counted
    # Add this word to the counted set.
    counted.add(word)
    # Evaluate first friends of this word.
    first_friends = network[word]
    total = 0
    for friend in first_friends:
        if friend not in counted:
            t, counted = count_friends(friend, network, counted)
            total += t+1
    return total, counted

def main():
    with open(sys.argv[1], 'r') as fh:
        data = fh.read()
        tests = data.split('END OF INPUT')[0].strip().split('\n')
        words = data.split('END OF INPUT')[1].strip().split('\n')
    dictionary = words
    network = collections.defaultdict(list)
    for i in xrange(len(dictionary)):
        t1 = dictionary[i]
        for j in xrange(i+1, len(dictionary)):
            t2 = dictionary[j]
            if distance(t1, t2) == 1:
                network[t1].append(t2)
                network[t2].append(t1)
    print network
    for test in tests:
        network_deep_copy = copy.deepcopy(network)
        for i in xrange(len(dictionary)):
            if distance(test, dictionary[i]) == 1:
                network_deep_copy[test].append(dictionary[i])
                network_deep_copy[dictionary[i]].append(test)
        friends, counted = count_friends(test, network_deep_copy)
        print friends

if __name__ == '__main__':
    main()
