import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.visited = False
        self.next_node = None

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    # Map from value to node object.
    nodes_map = {}
    bad = False

    # Establish the node mapping objects.
    for path in test.split(';'):
        value1 = path.split('-')[0]
        value2 = path.split('-')[1]

        node1 = nodes_map[value1] if (value1 in nodes_map) else Node(value1)
        node2 = nodes_map[value2] if (value2 in nodes_map) else Node(value2)

        nodes_map[value1] = node1
        nodes_map[value2] = node2

        if node1.next_node is not None:
            bad = True
            break

        node1.next_node = node2

    if bad:
        print('BAD')
        continue

    # Iterate through node mapping objects, marking visited as necessary.
    current_node = nodes_map['BEGIN']

    while True:
        if current_node.visited:
            bad = True
            break

        current_node.visited = True
        current_node = current_node.next_node

        if current_node is None:
            bad = True
            break

        if current_node.value == 'END':
            current_node.visited = True
            break

    if bad:
        print('BAD')
        continue

    # Loop through all the nodes, and make sure they have all been visited.
    for node in nodes_map.values():
        if not node.visited:
            bad = True
            break

    if bad:
        print('BAD')
    else:
        print('GOOD')

test_cases.close()
