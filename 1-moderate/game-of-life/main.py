import sys
import copy

class GameOfLife:
    def __init__(self, is_alive_array):
        self.is_alive_array = is_alive_array
        self.n = len(is_alive_array)

    def is_alive(self, i, j):
        if i < 0 or i >= self.n or j < 0 or j >= self.n: return False
        return self.is_alive_array[i][j]

    def count_neighbors(self, i, j):
        result = 0
        result += self.is_alive(i-1, j)
        result += self.is_alive(i+1, j)
        result += self.is_alive(i, j-1)
        result += self.is_alive(i, j+1)
        result += self.is_alive(i-1, j-1)
        result += self.is_alive(i+1, j+1)
        result += self.is_alive(i-1, j+1)
        result += self.is_alive(i+1, j-1)
        return result

    def next(self):
        """
        Any live cell with fewer than two live neighbors dies, as if caused by under-population.
        Any live cell with two or three live neighbors lives on to the next generation.
        Any live cell with more than three live neighbors dies, as if by overcrowding.
        Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
        """

        is_alive_array_new = copy.deepcopy(self.is_alive_array)

        for i in xrange(self.n):
            for j in xrange(self.n):
                neighbors_count = self.count_neighbors(i, j)

                if self.is_alive_array[i][j]:
                    # Cell is alive
                    if neighbors_count < 2:
                        is_alive_array_new[i][j] = False
                    elif neighbors_count == 2 or neighbors_count == 3:
                        pass
                    else:
                        is_alive_array_new[i][j] = False
                else:
                    # Cell is dead.
                    if neighbors_count == 3:
                        is_alive_array_new[i][j] = True

        self.is_alive_array = is_alive_array_new

    def __str__(self):
        def bool_to_char(b):
            return '*' if b else '.'

        result = []
        for array in self.is_alive_array: result.append(''.join([bool_to_char(a) for a in array]))
        return '\n'.join(result)

def main():
    with open(sys.argv[1], 'r') as test_file:
        game_of_life_input = test_file.read().strip()
        is_alive_array = []
        for line in game_of_life_input.split('\n'):
            array = []
            for char in line: array.append(True if char == '*' else False)
            is_alive_array.append(array)
        game = GameOfLife(is_alive_array)
        for i in xrange(10): game.next()
        print game

    test_file.close()

if __name__ == '__main__':
    main()