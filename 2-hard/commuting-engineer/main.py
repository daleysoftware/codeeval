import sys
import math
import re
import copy

class Point:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    # Geographic distance from this point to the provided point.
    def distance_to(self, point):
        d_lat = (point.latitude - self.latitude) * math.pi/180
        d_lon = (point.longitude - self.longitude) * math.pi/180
        lat1 = self.latitude * math.pi/180
        lat2 = point.latitude * math.pi/180
        a = math.sin(d_lat/2) * math.sin(d_lat/2) + \
            math.sin(d_lon/2) * math.sin(d_lon/2) * \
            math.cos(lat1) * math.cos(lat2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        return  6371 * c

# Permutation of set s with starting point start.
def permute(start, indexes):
    prefix = [start]
    if start in indexes: indexes.remove(start)
    result = []
    _permute_implementation(indexes, result, prefix)
    return result

def _permute_implementation(indexes, result, prefix):
    if result is None: result = []
    if prefix is None: prefix = []
    if len(indexes) == 0:
        result.append(copy.deepcopy(prefix))
        return
    for i in xrange(len(indexes)):
        prefix.append(indexes[i])
        _permute_implementation(indexes[:i] + indexes[i+1:], result, prefix)
        prefix.pop()

def compute_route_distance(route, points):
    total_distance = 0
    for i in xrange(1, len(route)):
        p1 = points[route[i-1]]
        p2 = points[route[i]]
        total_distance += p1.distance_to(p2)
    return total_distance

def main():
    # Parse the input to obtain the points of interest.
    test_cases = open(sys.argv[1], 'r')
    points = {}
    for test in test_cases:
        test = test.strip()
        if len(test) == 0: continue
        m = re.match("([0-9]+) \| .*\((.*)\)", test)
        index = int(m.group(1))
        latitude = float(m.group(2).split(',')[0].strip())
        longitude = float(m.group(2).split(',')[1].strip())
        p = Point(latitude, longitude)
        points[index] = p

    # Calculate the best route.
    best_distance = float('inf')
    best_route = []
    permutations = permute(1, points.keys())
    for route in permutations:
        distance = compute_route_distance(route, points)
        if distance < best_distance:
            best_distance = distance
            best_route = route

    # Print the result.
    print '\n'.join([str(x) for x in best_route])

if __name__ == '__main__':
    main()
