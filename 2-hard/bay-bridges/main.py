import sys
import re

# Parsing patterns.
NUM = "[0-9.-]+"
LINE = "([0-9]+): \(\[(%s)[, ]+(%s)\][, ]+\[(%s)[, ]+(%s)\]\)" % ((NUM,) * 4)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class LineSegment:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    @staticmethod
    def ccw(a, b, c):
        """
        Return true if the points A, B, and C are listed in counter clockwise order.
        """
        return (c.y - a.y) * (b.x - a.x) > (b.y - a.y) * (c.x - a.x)

    @staticmethod
    def does_ab_intersect_with_cd(a, b, c, d):
        """
        Return True when line segment AB intersects with line segment CD. Does not test for
        co-linearity.
        """
        return (LineSegment.ccw(a, c, d) != LineSegment.ccw(b, c, d) and
                LineSegment.ccw(a, b, c) != LineSegment.ccw(a, b, d))

    def intersects_with(self, line_segment):
        return LineSegment.does_ab_intersect_with_cd(self.p1, self.p2,
                                                     line_segment.p1, line_segment.p2)

def is_intersecting_set(s, intersect):
    for i in range(len(s)):
        si = s[i]
        for j in range(i+1, len(s)):
            sj = s[j]
            if intersect[si][sj]: return True
    return False

def find_largest_non_intersecting_set(s, intersect, result=None, prefix=None, index=0):
    if prefix is None: prefix = []
    if result is None: result = []

    if index == len(s):
        if not is_intersecting_set(prefix, intersect):
            if len(prefix) > len(result):
                return prefix
        return result

    result = find_largest_non_intersecting_set(s, intersect, result, prefix, index+1)
    result = find_largest_non_intersecting_set(s, intersect, result, prefix + [s[index]], index+1)

    return result

def main():
    with open(sys.argv[1], 'r') as input_file:
        # Parse the input; store line segments in line_segments array.
        line_segments = []
        for line in input_file.read().strip().split('\n'):
            m = re.match(LINE, line)
            p1 = Point(float(m.group(2)), float(m.group(3)))
            p2 = Point(float(m.group(4)), float(m.group(5)))
            line_segments.append(LineSegment(p1, p2))

        # Create an array of whether or not a pair of line segments intersect.
        intersect = []
        for i in range(len(line_segments)): intersect.append([False] * len(line_segments))
        for i in range(0, len(line_segments)):
            ls1 = line_segments[i]
            for j in range(i+1, len(line_segments)):
                ls2 = line_segments[j]
                if ls1.intersects_with(ls2):
                    intersect[i][j] = True
                    intersect[j][i] = True

        # Print the final result.
        result = find_largest_non_intersecting_set(range(len(line_segments)), intersect)
        print '\n'.join([str(i+1) for i in result])

if __name__ == '__main__':
    main()
