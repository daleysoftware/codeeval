import sys

class Node:
    def __init__(self, value):
        self.value = value

        self.counts = {}
        self.nodes = {}

    def add_link(self, node):
        if node.value in self.nodes:
            self.counts[node.value] += 1
        else:
            self.counts[node.value] = 1
            self.nodes[node.value] = node

    def remove_link(self, value):
        self.counts[value] -= 1

    def compute_longest_chain(self):
        result = 0

        for value in self.counts:
            count = self.counts[value]
            node = self.nodes[value]

            if count > 0:
                self.counts[value] -= 1
                result = max(result, node.compute_longest_chain() + 1)
                self.counts[value] += 1

        return result

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    nodes = {}
    for word in test.split(','):
        if not word[0] in nodes:
            nodes[word[0]] = Node(word[0])
        first = nodes[word[0]]

        if not word[-1] in nodes:
            nodes[word[-1]] = Node(word[-1])
        second = nodes[word[-1]]

        first.add_link(second)

    result = 0
    for value, node in nodes.iteritems():
        longest_chain = node.compute_longest_chain()

        if longest_chain > result:
            result = longest_chain

    if result <= 1:
        print 'None'
    else:
        print result

test_cases.close()
