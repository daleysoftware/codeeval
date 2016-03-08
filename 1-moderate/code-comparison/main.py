import sys


class LetterMatrix(object):
    def __init__(self, array):
        self.array = array
        self.rows = len(array)
        self.cols = len(array[0])

    def count_code_blocks(self):
        """
        Count the number of 2x2 blocks that contain the letters 'code'.
        """
        result = 0
        for i in range(self.rows-1):
            for j in range(self.cols-1):
                letters = [self.array[i][j],
                           self.array[i+1][j],
                           self.array[i][j+1],
                           self.array[i+1][j+1]]
                if 'c' in letters and 'o' in letters and 'd' in letters and 'e' in letters:
                    result += 1
        return result

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0: continue
        letter_matrix = LetterMatrix([list(s.strip()) for s in test.split('|')])
        print(letter_matrix.count_code_blocks())
    test_cases.close()


if __name__ == '__main__':
    main()
