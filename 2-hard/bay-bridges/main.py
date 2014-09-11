import sys
import re

# Parsing patterns.
NUM = "[0-9.-]+"
LINE = "([0-9]+): \(\[(%s)[, ]+(%s)\][, ]+\[(%s)[, ]+(%s)\]\)" % ((NUM,) * 4)

class Point:
    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude

class LineSegment:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def intersects_with(self, line_segment):
        # TODO finish this...
        return False

def main():
    with open(sys.argv[1], 'r') as input_file:
        line_segments = []
        for line in input_file.read().strip().split('\n'):
            match = re.match(LINE, line)
            point1 = Point(float(match.group(2)), float(match.group(3)))
            point2 = Point(float(match.group(4)), float(match.group(5)))
            line_segments.append(LineSegment(point1, point2))
        print line_segments

        ls4 = line_segments[3]
        for ls in line_segments:
            print ls4.intersects_with(ls)

if __name__ == '__main__':
    main()
