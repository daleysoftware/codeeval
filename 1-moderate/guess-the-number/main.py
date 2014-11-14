import sys
import math

class NumberGuesser:
    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def getGuess(self):
        return int(math.ceil((self.lower_bound + self.upper_bound) / 2.0))

    def hasSolution(self):
        return self.lower_bound == self.upper_bound

    def lower(self):
        self.upper_bound = self.getGuess() - 1

    def higher(self):
        self.lower_bound = self.getGuess() + 1

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0: continue
        upper_bound = int(test.split(' ' )[0])
        number_guesser = NumberGuesser(0, upper_bound)
        guesses = test.split(' ')[1:-1]
        for guess in guesses:
            if number_guesser.hasSolution(): raise Exception("solution too early")
            if guess == "Lower": number_guesser.lower()
            else: number_guesser.higher()
        print number_guesser.getGuess()

    test_cases.close()

if __name__ == '__main__':
    main()
