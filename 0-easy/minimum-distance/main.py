import sys

def compute_difference(houses, house):
    difference = 0
    for h in houses:
        difference += abs(h - house)
    return difference

def main(input_file):
    with open(input_file, 'r') as fh:
        for line in fh:
            houses = sorted([int(x) for x in line.split(' ')[1:]])
            difference = float("inf")
            for house in houses:
                difference = min(difference, compute_difference(houses, house))
            print(difference)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: %s <input_file>" % sys.argv[0])
        sys.exit(1)
    main(sys.argv[1])
