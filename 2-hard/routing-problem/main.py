import sys
import ast
import socket
import struct
import collections

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = collections.defaultdict(list)

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)

# TODO broken, needs fixing.
def find_all_paths(graph, start, end):
    queue = [start]
    paths = collections.defaultdict(list)
    distances = collections.defaultdict(int)
    visited = set()

    while len(queue) > 0:
        node = queue.pop()
        new_paths = [p + [node] for p in paths[node]]
        if len(new_paths) == 0:
            new_paths = [[node]]
        min_distance = len(min(new_paths, key=len))

        for next_node in graph.edges[node]:
            next_node_visited = (node, next_node) in visited
            visited.add((node, next_node))

            if not next_node_visited:
                if distances[next_node] == 0 or min_distance+1 <= distances[next_node]:
                    # TODO can improve this by trimming out longer paths at this step.
                    paths[next_node].extend(new_paths)
                    distances[next_node] = len(min(paths[next_node], key=len))
                    if next_node not in queue: queue.append(next_node)

    return [p + [end] for p in paths[end]]

def make_mask(n):
    result = 0xffffffff
    for i in range(32-int(n)): result -= (1 << i)
    return result

def dotted_quad_to_num(ip):
    return struct.unpack('!I',socket.inet_aton(ip))[0]

def node1_can_reach_node2(n1, n2, node_to_ips_mapping):
    for ip1 in node_to_ips_mapping[n1]:
        for ip2 in node_to_ips_mapping[n2]:
            if ip1[0] & ip1[1] == ip2[0] & ip2[1]:
                return True
    return False

def main():
    test_cases = open(sys.argv[1], 'r')

    graph_text = test_cases.readline()
    node_to_ips_mapping = ast.literal_eval(graph_text)
    graph = Graph()
    nodes = list(node_to_ips_mapping.keys())
    for node in nodes:
        ips = node_to_ips_mapping[node]
        new_ips = []
        for ip in ips:
            new_ips.append([dotted_quad_to_num(ip.split('/')[0]),
                           make_mask(ip.split('/')[1])])
        node_to_ips_mapping[node] = new_ips

    for i in range(len(nodes)):
        node1 = nodes[i]
        graph.add_node(node1)
        for j in range(i, len(nodes)):
            node2 = nodes[j]
            graph.add_node(node2)
            if node1 == node2:
                continue
            if node1_can_reach_node2(node1, node2, node_to_ips_mapping):
                graph.add_edge(node1, node2)

    for test in test_cases:
        test = test.strip()
        if len(test) == 0:
            continue

        start = int(test.split(' ')[0])
        end = int(test.split(' ')[1])
        paths = sorted(find_all_paths(graph, start, end), key=len)
        if len(paths) == 0:
            print('No connection')
            continue
        best_length = len(paths[0])
        best_paths = []
        for path in paths:
            if len(path) != best_length:
                break
            best_paths.append(str(path))
        print(", ".join(best_paths))

    test_cases.close()

if __name__ == '__main__':
    main()
