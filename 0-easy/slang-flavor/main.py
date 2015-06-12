import sys
import re

POSTFIXES =  [
    ', yeah!',
    ', this is crazy, I tell ya.',
    ', can U believe this?',
    ', eh?',
    ', aw yea.',
    ', yo.',
    '? No way!',
    '. Awesome!'
    ]

def main():
    test_cases = open(sys.argv[1], 'r')
    index = 0
    count = 0
    for test in test_cases:
        test = test.strip()
        if len(test) == 0:
            continue
        sentences = [x.strip() for x in re.split('[\.!\?]', test) if len(x) > 0]
        line = []
        for s in sentences:
            if count % 2 != 0:
                line.append(s + POSTFIXES[index])
                index = (index + 1) % len(POSTFIXES)
            else:
                punctuation = test[test.find(s) + len(s)]
                line.append(s + punctuation)
            count += 1
        print(' '.join(line))
    test_cases.close()

if __name__ == '__main__':
    main()
