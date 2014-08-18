import sys
import collections

def distance_is_equal_to_one(s1, s2):
    if abs(len(s1)-len(s2)) > 1:
        return False
    elif len(s1) == len(s2):
        diff_found = False
        for i in xrange(len(s1)):
            if s1[i] != s2[i]:
                if diff_found: return False
                else: diff_found = True
        return True
    else:
        lng = s1 if len(s1) > len(s2) else s2
        sht = s1 if len(s1) < len(s2) else s2
        bumper = 0
        for i in xrange(len(sht)):
            if sht[i] != lng[i+bumper]:
                if bumper > 0: return False
                else: bumper = 1
        return True

def add_word_to_network(word, network):
    result_set = set()
    result_set.add(word)
    for key in network.keys():
        if word not in network[key] and distance_is_equal_to_one(word, key):
            network[key].update(result_set)
            result_set = network[key]
    network[word] = result_set

def main():
    with open(sys.argv[1], 'r') as fh:
        data = fh.read()
        tests = data.split('END OF INPUT')[0].strip().split('\n')
        words = data.split('END OF INPUT')[1].strip().split('\n')
    network = collections.defaultdict(set)
    for word in words: add_word_to_network(word, network)
    # Go through all the given words and count the number of friends.
    for test in tests:
        result = 0
        for word in words:
            if distance_is_equal_to_one(test, word):
                result = len(network[word])-1
        print result

if __name__ == '__main__':
    main()