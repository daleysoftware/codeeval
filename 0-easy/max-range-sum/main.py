import sys

def main(input_file):
    with open(input_file, 'r') as fh:
        for line in fh:
            line = line.strip()
            days = int(line.split(';')[0])
            array = [int(x) for x in line.split(';')[1].split(' ')]
            result = 0
            for i in xrange(0, len(array)-days+1):
                result = max(sum(array[i:i+days]), result)
            print result

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: %s <input_file>" % sys.argv[0])
        sys.exit(1)
    main(sys.argv[1])