import sys

def bipartite_match(graph):
    """
    Program to find the bipartite match.

    Hopcroft-Karp bipartite max-cardinality matching and max independent set
    David Eppstein, UC Irvine, 27 Apr 2002.

    Find maximum cardinality matching of a bipartite graph (U,V,E).
    The input format is a dictionary mapping members of U to a list
    of their neighbors in V.  The output is a triple (M,A,B) where M is a
    dictionary mapping members of V to their matches in U, A is the part
    of the maximum independent set in U, and B is the part of the MIS in V.
    The same object may occur in both U and V, and is treated as two
    distinct vertices if this happens.
    """
    matching = {}
    for u in graph:
        for v in graph[u]:
            if v not in matching:
                matching[v] = u
                break

    while True:
        predictions = {}
        unmatched = []
        prediction = dict([(u, unmatched) for u in graph])
        for v in matching:
            del prediction[matching[v]]
        layer = list(prediction)
        while layer and not unmatched:
            new_layer = {}
            for u in layer:
                for v in graph[u]:
                    if v not in predictions:
                        new_layer.setdefault(v, []).append(u)
            layer = []
            for v in new_layer:
                predictions[v] = new_layer[v]
                if v in matching:
                    layer.append(matching[v])
                    prediction[matching[v]] = v
                else:
                    unmatched.append(v)
        if not unmatched:
            not_layered = {}
            for u in graph:
                for v in graph[u]:
                    if v not in predictions:
                        not_layered[v] = None
            return matching, list(prediction), list(not_layered)

        def recurse(v):
            if v in predictions:
                L = predictions[v]
                del predictions[v]
                for u in L:
                    if u in prediction:
                        pu = prediction[u]
                        del prediction[u]
                        if pu is unmatched or recurse(pu):
                            matching[v] = u
                            return 1
            return 0

        for v in unmatched: recurse(v)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    N = int(test.split(';')[0])
    graph = {}

    for i in test.split(';')[1].split('], '):
        team_member_id = i.split(':[')[0]
        graph[team_member_id] = []

        for desk in i.split(':[')[1].split(']')[0].split(','):
            graph[team_member_id].append(int(desk.strip()))

    if len(graph) == len(bipartite_match(graph)[0]):
        print('Yes')
    else:
        print('No')

test_cases.close()
