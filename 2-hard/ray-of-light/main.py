import sys

ROOM_SIZE = 10
LIGHT_DISTRIBUTION = 20

class Point(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __str__(self):
        return "(%i,%i)" % (self.row, self.col)

class Element(object):
    WALL = '#'
    HOLE = 'o'
    PRISM = '*'
    EMPTY = ' '
    LIGHT_X = 'X'
    LIGHT_BACK = '\\'
    LIGHT_FORWARD = '/'

class Trajectory(object):
    UP_L = 0
    UP_R = 1
    DN_L = 2
    DN_R = 3

class Room(object):
    def __init__(self, schematic):
        self.schematic = schematic

    def __str__(self):
        return '\n'.join(''.join(x) for x in self.schematic)

    def _element(self, point):
        return self.schematic[point.row][point.col]

    @property
    def _hole(self):
        # Top and bottom rows.
        for c in xrange(0, ROOM_SIZE):
            if self._element(Point(0, c)) != Element.WALL: return Point(0, c)
            if self._element(Point(ROOM_SIZE-1, c)) != Element.WALL: return Point(ROOM_SIZE-1, c)
        # Sides
        for r in xrange(1, ROOM_SIZE-1):
            if self._element(Point(r, 0)) != Element.WALL: return Point(r, 0)
            if self._element(Point(r, ROOM_SIZE-1)) != Element.WALL: return Point(r, ROOM_SIZE-1)
        # Should never reach here given valid input.
        return None

    @property
    def _initial_trajectory(self):
        hole = self._hole
        hole_element = self._element(hole)

        # Top.
        if hole.row == 0:
            return Trajectory.DN_L if hole_element == Element.LIGHT_FORWARD else Trajectory.DN_R
        # Bottom.
        if hole.row == ROOM_SIZE-1:
            return Trajectory.UP_R if hole_element == Element.LIGHT_FORWARD else Trajectory.UP_L
        # Left.
        if hole.col == 0:
            return Trajectory.UP_R if hole_element == Element.LIGHT_FORWARD else Trajectory.DN_R
        # Right.
        if hole.col == ROOM_SIZE-1:
            return Trajectory.DN_L if hole_element == Element.LIGHT_FORWARD else Trajectory.UP_L

        # Should never reach this point.
        return None

    def _propagate_light(self, rays):
        # TODO move light one unit and update room state.
        return []

    def propagate_light(self):
        rays = [(self._hole, self._initial_trajectory, LIGHT_DISTRIBUTION-1)]
        while len(rays) > 0:
            rays = self._propagate_light(rays)

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0: continue
        room = Room(zip(*[iter(test)]*ROOM_SIZE))
        room.propagate_light()
        print room
        # TODO print properly
    test_cases.close()

if __name__ == '__main__':
    main()