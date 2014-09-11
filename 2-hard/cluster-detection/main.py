import sys
from collections import defaultdict


class FriendGraph:
    def __init__(self):
        self.interactions = defaultdict(list)

    def add_one_way_interaction(self, a, b):
        if b not in self.interactions[a]: self.interactions[a].append(b)

    def is_a_friends_with_b(self, a, b):
        result = b in self.interactions[a] and a in self.interactions[b]
        return result

    def is_friend_cluster(self, s):
        for i in xrange(len(s)):
            f1 = s[i]
            for j in xrange(i+1, len(s)):
                f2 = s[j]
                if not self.is_a_friends_with_b(f1, f2):
                    return False
        return True

    @staticmethod
    def _remove_subsets_and_deduplicate(list_of_sets):
        result = list_of_sets[:]
        for m in list_of_sets:
            for n in list_of_sets:
                if set(m).issubset(set(n)) and m != n:
                    result.remove(m)
                    break
        result = sorted([sorted(list(r)) for r in result])
        result = [result[i] for i in range(len(result)) if i == 0 or result[i] != result[i-1]]
        return [set(r) for r in result]

    def get_friend_clusters_for(self, a, prefix=None, result=None, index=0):
        if prefix is None: prefix = [a]
        if result is None: result = []

        if index == len(self.interactions[a]):
            if self.is_friend_cluster(prefix) and len(prefix) >= 3:
                result.append(set(prefix))
            return result

        result = self.get_friend_clusters_for(a, prefix, result, index+1)
        result = self.get_friend_clusters_for(a, prefix + [self.interactions[a][index]], result, index+1)

        return FriendGraph._remove_subsets_and_deduplicate(result)

    def get_friend_clusters(self):
        result = []
        for f in self.interactions.keys():
            for cluster in self.get_friend_clusters_for(f):
                result.append(cluster)
        return FriendGraph._remove_subsets_and_deduplicate(result)

    def __str__(self):
        return str(self.interactions)

def main():
    with open(sys.argv[1], 'r') as input_file:
        fg = FriendGraph()
        for line in input_file:
            line = line.strip().split('\t')
            a = line[-1].strip()
            b = line[-2].strip()
            fg.add_one_way_interaction(a, b)

        print '\n'.join(sorted([', '.join(sorted(cluster)) for cluster in fg.get_friend_clusters()]))

if __name__ == '__main__':
    main()
