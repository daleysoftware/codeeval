import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0: continue
        virus = sum([int(x, 16) for x in test.split('|')[0].strip().split(' ')])
        anti_virus = sum([int(x, 2) for x in test.split('|')[1].strip().split(' ')])
        # Anti-virus >= Virus, print True.
        print('True' if anti_virus >= virus else 'False')
    test_cases.close()

if __name__ == '__main__':
    main()
