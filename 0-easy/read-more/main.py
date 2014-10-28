import sys

def trim(line):
    if len(line) <= 55:
        return line
    else:
        line = line[0:40]
        if line.rfind(' ') != -1: line = line[0:line.rfind(' ')]
        return line + "... <Read More>"

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        print(trim(test))
    test_cases.close()

if __name__ == '__main__':
    main()