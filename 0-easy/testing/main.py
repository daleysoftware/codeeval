import sys

def count_mistakes(case, design):
    mistakes = 0
    for c, d in zip(case, design):
        if c != d:
            mistakes += 1
    return mistakes + abs(len(case) - len(design))

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        case, design = [x.strip() for x in test.strip().split('|')]
        mistakes = count_mistakes(case, design)
        if mistakes == 0:
            print('Done')
        elif mistakes <= 2:
            print('Low')
        elif mistakes <= 4:
            print('Medium')
        elif mistakes <= 6:
            print('High')
        else:
            print('Critical')
    test_cases.close()

if __name__ == '__main__':
    main()
