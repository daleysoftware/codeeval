import sys
import math
import collections

class UnionFind:
    def __init__(self):
        self.weights = {}
        self.parents = {}

    def __getitem__(self, object):
        if object not in self.parents:
            self.parents[object] = object
            self.weights[object] = 1
            return object

        path = [object]
        root = self.parents[object]
        while root != path[-1]:
            path.append(root)
            root = self.parents[root]

        for ancestor in path:
            self.parents[ancestor] = root
        return root

    def union(self, *objects):
        roots = [self[x] for x in objects]
        heaviest = max([(self.weights[r],r) for r in roots])[1]
        for r in roots:
            if r != heaviest:
                self.weights[heaviest] += self.weights[r]
                self.parents[r] = heaviest

def min_spanning_tree(G):
    for u in G:
        for v in G[u]:
            if G[u][v] != G[v][u]:
                raise ValueError("asymmetric weights")

    subtrees = UnionFind()
    tree = []
    for W,u,v in sorted((G[u][v],u,v) for u in G for v in G[u]):
        if subtrees[u] != subtrees[v]:
            tree.append((u,v))
            subtrees.union(u,v)
    return tree        

def length_from_p1_to_p2(p1, p2):
    a = p1[0] - p2[0]
    b = p1[1] - p2[1]
    c2 = a*a + b*b
    return math.sqrt(c2)

def main():
    with open(sys.argv[1], 'r') as fh:
        for line in fh:
            points = [(int(p.split(',')[0]), int(p.split(',')[1])) for p in line.strip().split(' ')]
            g = collections.defaultdict(dict)

            for i in xrange(len(points)):
                for j in xrange(i+1, len(points)):
                    length = length_from_p1_to_p2(points[i], points[j])
                    g[i][j] = length
                    g[j][i] = length

            t = min_spanning_tree(g)
            mst_weight = sum([g[u][v] for u,v in t])
            print int(math.ceil(mst_weight))

if __name__ == '__main__':
    main()
