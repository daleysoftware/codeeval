import sys

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

def main(input_file):
    with open(input_file, 'r') as fh:
        for line in fh:
            o, p, q, r = [int(x) for x in line.split(' ')]

            current = Point(o, p)
            overlook = Point(q, r)

            if current == overlook:
                print 'here'
            elif overlook.x >  current.x and overlook.y >  current.y:
                print 'NE'
            elif overlook.x >  current.x and overlook.y == current.y:
                print 'E'
            elif overlook.x >  current.x and overlook.y <  current.y:
                print 'SE'
            elif overlook.x == current.x and overlook.y <  current.y:
                print 'S'
            elif overlook.x <  current.x and overlook.y <  current.y:
                print 'SW'
            elif overlook.x <  current.x and overlook.y == current.y:
                print 'W'
            elif overlook.x <  current.x and overlook.y >  current.y:
                print 'NW'
            else:
                print 'N'

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: %s <input_file>" % sys.argv[0])
        sys.exit(1)
    main(sys.argv[1])
