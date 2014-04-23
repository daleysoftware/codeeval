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

def find_paths_using_bfs(graph, current, end, prefix=None, visited=set()):
    if prefix is None:
        prefix = []

    if current == end:
        return [prefix + [end]]
    if current in visited:
        return []

    visited.add(current)
    result_paths = []

    for node in graph.edges[current]:
        paths = find_paths_using_bfs(graph, node, end, prefix + [current], visited)

        if len(paths) > 0:
            result_paths.extend(paths)

    visited.remove(current)
    return result_paths

def make_mask(n):
    result = 0xffffffff
    for i in range(32-int(n)): result -= (1 << i)
    return result

def dotted_quad_to_num(ip):
    return struct.unpack('!I',socket.inet_aton(ip))[0]

def network_mask(ip, bits):
    return dotted_quad_to_num(ip) & make_mask(bits)

def node1_can_reach_node2(n1, n2, node_to_ip_mapping):
    ips1 = node_to_ip_mapping[n1]
    ips2 = node_to_ip_mapping[n2]

    for ip1 in ips1:
        nm1 = make_mask(ip1.split('/')[1])
        ip1 = dotted_quad_to_num(ip1.split('/')[0])
        for ip2 in ips2:
            nm2 = make_mask(ip2.split('/')[1])
            ip2 = dotted_quad_to_num(ip2.split('/')[0])

            if ip1 & nm1 == ip2 & nm2:
                return True

    return False

def main():
    test_cases = open(sys.argv[1], 'r')

    graph_text = test_cases.readline()
    node_to_ip_mapping = ast.literal_eval(graph_text)
    graph = Graph()

    nodes = node_to_ip_mapping.keys()

    for i in range(len(nodes)):
        node1 = nodes[i]
        graph.add_node(node1)

        for j in range(i, len(nodes)):
            node2 = nodes[j]
            graph.add_node(node2)

            if node1 == node2:
                continue

            if node1_can_reach_node2(node1, node2, node_to_ip_mapping):
                graph.add_edge(node1, node2)

    for test in test_cases:
        test = test.strip()
        if len(test) == 0:
            continue

        start = int(test.split(' ')[0])
        end = int(test.split(' ')[1])

        paths = sorted(find_paths_using_bfs(graph, start, end), key=len)
        if len(paths) == 0:
            print 'No connection'
            continue

        best_length = len(paths[0])
        best_paths = []
        for path in paths:
            if len(path) != best_length:
                break

            best_paths.append(str(path))

        print ", ".join(best_paths)

    test_cases.close()

if __name__ == '__main__':
    main()
