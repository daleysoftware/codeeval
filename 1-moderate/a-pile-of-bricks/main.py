import sys
import re

class TwoDimensionalPoint:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

class ThreeDimensionalPoint:
    def __init__(self, x, y, z):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)

class Rectangle:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        side1 = max(abs(p1.x - p2.x), abs(p2.x - p1.x))
        side2 = max(abs(p1.y - p2.y), abs(p2.y - p1.y))
        self.length = max(side1, side2)
        self.width = min(side1, side2)

    def larger_than(self, rectangle):
        return self.length >= rectangle.length and self.width >= rectangle.width

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue
    hole_p1_match = re.search('\[([-,0-9]+),([-,0-9]+)\]', test.split('|')[0].split(' ')[0])
    hole_p2_match = re.search('\[([-,0-9]+),([-,0-9]+)\]', test.split('|')[0].split(' ')[1])
    bricks = test.split('|')[1].split(';')
    hole = Rectangle(
        TwoDimensionalPoint(hole_p1_match.group(1), hole_p1_match.group(2)),
        TwoDimensionalPoint(hole_p2_match.group(1), hole_p2_match.group(2)))
    fitting_brick_ids = []
    counter = 1
    for brick in bricks:
        brick_split = brick.split(' ')
        p1_match = re.search('\[([-,0-9]+),([-,0-9]+),([-,0-9]+)\]', brick_split[1])
        p2_match = re.search('\[([-,0-9]+),([-,0-9]+),([-,0-9]+)\]', brick_split[2])
        p1 = ThreeDimensionalPoint(p1_match.group(1), p1_match.group(2), p1_match.group(3))
        p2 = ThreeDimensionalPoint(p2_match.group(1), p2_match.group(2), p2_match.group(3))
        r1 = Rectangle(TwoDimensionalPoint(p1.y, p1.z), TwoDimensionalPoint(p2.y, p2.z))
        r2 = Rectangle(TwoDimensionalPoint(p1.x, p1.y), TwoDimensionalPoint(p2.x, p2.y))
        r3 = Rectangle(TwoDimensionalPoint(p1.x, p1.z), TwoDimensionalPoint(p2.x, p2.z))
        if hole.larger_than(r1) or hole.larger_than(r2) or hole.larger_than(r3):
            fitting_brick_ids.append(str(counter))
        counter += 1
    if len(fitting_brick_ids) == 0:
        print("-")
    else:
        print(','.join(fitting_brick_ids))

test_cases.close()
