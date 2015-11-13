import sys
import math

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        vampires, zombies, witches, houses = [int(x.split(':')[1].strip()) for x in test.strip().split(',')]
        total_candies = houses * (vampires * 3 + zombies * 4 + witches * 5)
        total_kids = vampires + zombies + witches
        print(math.floor(float(total_candies) / float(total_kids)))
    test_cases.close()

if __name__ == '__main__':
    main()
