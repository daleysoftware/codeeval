import sys
import collections

class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = collections.defaultdict(list)
    self.distances = {}
  def add_node(self, value):
    self.nodes.add(value)
  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance
    self.distances[(to_node, from_node)] = distance

def dijsktra(graph, initial):
    visited = {initial: 0}
    path = {}
    nodes = set(graph.nodes)
    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break
        nodes.remove(min_node)
        current_weight = visited[min_node]
        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node
    return visited, path

def node_name(x, y):
    return str(x) + ',' + str(y)

def add_edge_helper(raw_graph, graph, x1, y1, x2, y2):
     if raw_graph[x2][y2] == ' ':
        graph.add_edge(node_name(x1, y1), node_name(x2, y2), 1)

def add_edge(raw_graph, graph, x, y):
    add_edge_helper(raw_graph, graph, x, y, x, y-1)
    add_edge_helper(raw_graph, graph, x, y, x, y+1)
    add_edge_helper(raw_graph, graph, x, y, x-1, y)
    add_edge_helper(raw_graph, graph, x, y, x+1, y)

def main():
    with open(sys.argv[1], 'r') as fh:
        raw_graph = fh.read().strip()
    raw_graph = raw_graph.split('\n')
    graph = Graph()
    # Add nodes.
    first_node = None
    last_node = None
    for x in xrange(0, len(raw_graph)):
        for y in xrange(0, len(raw_graph[x])):
            if raw_graph[x][y] == ' ':
                node = node_name(x, y)
                last_node = node
                graph.add_node(node)
                if not first_node:
                    first_node = node
    # Add edges.
    for x in xrange(1, len(raw_graph)-1):
        for y in xrange(1, len(raw_graph[x])-1):
            if raw_graph[x][y] == ' ':
                add_edge(raw_graph, graph, x, y)

    visited, path = dijsktra(graph, first_node)
    # Parse dijsktra output and compute the best path.
    best_path = set()
    previous = last_node
    while previous != first_node:
        best_path.add(previous)
        previous = path[previous]
    best_path.add(first_node)
    # Print best path.
    for x in xrange(0, len(raw_graph)):
        for y in xrange(0, len(raw_graph[x])):
            if node_name(x, y) in best_path:
                sys.stdout.write('+')
            else:
                sys.stdout.write(raw_graph[x][y])
        sys.stdout.write('\n')

if __name__ == '__main__':
    main()
