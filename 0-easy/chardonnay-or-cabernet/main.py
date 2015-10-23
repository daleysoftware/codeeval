import sys
import copy

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0:continue
        wines = test.split('|')[0].strip().split(' ')
        letters = list(test.split('|')[1].strip().lower())
        result = []
        for wine in wines:
            original = wine
            match = True
            for letter in letters:
                if letter not in wine.lower():
                    match = False
                    break
                wine = wine.replace(letter, '', 1)
            if match:
                result.append(original)
        print('False' if len(result) == 0 else ' '.join(result))
    test_cases.close()

if __name__ == '__main__':
    main()
