import sys

CHESS_BOARD_SIZE = 8

class ChessBoardPosition(object):
    def __init__(self, col, row):
        self.col = col
        self.row = row

    @staticmethod
    def position_string_to_ints(position_string):
        col = ord(position_string[0]) - ord('a') + 1
        row = int(position_string[1])
        return col, row

    @staticmethod
    def ints_to_position_string(col, row):
        return chr(ord('a') - 1 + col) + str(row)

    def is_on_board(self):
        if self.col < 1 or self.row < 1 or self.col > 8 or self.row > 8:
            return False
        return True

    def __str__(self):
        if not self.is_on_board(): return None
        return ChessBoardPosition.ints_to_position_string(self.col, self.row)

class ChessBoard(object):
    def next_knight_moves(self, position):
        col = position.col
        row = position.row

        return [
            ChessBoardPosition(col-2,row-1),
            ChessBoardPosition(col-2,row+1),
            ChessBoardPosition(col+2,row-1),
            ChessBoardPosition(col+2,row+1),
            ChessBoardPosition(col-1,row-2),
            ChessBoardPosition(col-1,row+2),
            ChessBoardPosition(col+1,row-2),
            ChessBoardPosition(col+1,row+2)
        ]

def main(input_filename):
    with open(input_filename, 'r') as fh:
        for starting_position in fh:
            starting_position = starting_position.strip()

            if len(starting_position) == 0:
                continue

            col, row = ChessBoardPosition.position_string_to_ints(starting_position)
            next_knight_moves = ChessBoard().next_knight_moves(ChessBoardPosition(col, row))

            print ' '.join(sorted([str(n) for n in next_knight_moves if n.is_on_board()]))

    fh.close()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: %s <input_filename>" % sys.argv[0])
        sys.exit(1)
    main(sys.argv[1])
