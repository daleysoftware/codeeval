import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        people = test.split('|')[0].strip().split(' ')
        number = int(test.split('|')[1].strip())
        index = 0
        counter = 0
        while len(people) > 1:
            counter += 1
            if counter == number:
                counter = 0
                people.remove(people[index]) # N.B. doesn't work with duplicates.
                index = 0
            else:
                index += 1
            index %= len(people)
        print(people[0])
    test_cases.close()

if __name__ == '__main__':
    main()
