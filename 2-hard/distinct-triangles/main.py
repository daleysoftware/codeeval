import sys
import collections


class PairGenerator:
    def __init__(self, l):
        self.l = l
        self.i = 0
        self.j = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.j >= len(self.l):
            self.i += 1
            self.j = self.i + 1
        if self.j >= len(self.l):
            raise StopIteration
        result = self.l[self.i], self.l[self.j]
        self.j += 1
        return result


def count_distinct_triangles(graph):
    """
    Count distinct triangles in a given graph.

    Approach:
    For the set of edges belonging to a given node, enumerate all combinations of edge pairs. For a
    given edge pair, if there is a connection between the nodes, a triangle is formed. Add the
    triangle to a result set. Count the number of sets in the result at the end of comutation to
    obtain our final solution.

    Solution is O(E^2) where E is the number of edges in the graph.
    """
    triangles = set()
    for v in graph.keys():
        for pair in PairGenerator(list(graph[v])):
            if pair[1] in graph[pair[0]]:
                triangle = tuple(sorted(list(pair) + [v]))
                triangles.add(triangle)
    return len(triangles)


def main(input_filename):
    test_cases = open(input_filename, 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0:
            continue
        edges = [x.split(' ') for x in test.split(';')[1].strip().split(',')]
        graph = collections.defaultdict(set)
        for edge in edges:
            v1, v2 = edge
            graph[v1].add(v2)
            graph[v2].add(v1)
        print(count_distinct_triangles(graph))
    test_cases.close()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python %s <input_filename>" % sys.argv[0])
        sys.exit(1)
    main(sys.argv[1])
