import sys
import enum


class Rank(enum.IntEnum):
    TWO   = 2
    THREE = 3
    FOUR  = 4
    FIVE  = 5
    SIX   = 6
    SEVEN = 7
    EIGHT = 8
    NINE  = 9
    TEN   = 10
    JACK  = 11
    QUEEN = 12
    KING  = 13
    ACE   = 14

    @staticmethod
    def from_string(s):
        return {
            '2' : Rank.TWO,
            '3' : Rank.THREE,
            '4' : Rank.FOUR,
            '5' : Rank.FIVE,
            '6' : Rank.SIX,
            '7' : Rank.SEVEN,
            '8' : Rank.EIGHT,
            '9' : Rank.NINE,
            '10': Rank.TEN,
            'J' : Rank.JACK,
            'Q' : Rank.QUEEN,
            'K' : Rank.KING,
            'A' : Rank.ACE,
        }[s]


class Suit(enum.Enum):
    HEARTS = 1
    DIAMONDS = 2
    SPADES = 3
    CLUBS = 4

    @staticmethod
    def from_string(s):
        return {
            'H': Suit.HEARTS,
            'D': Suit.DIAMONDS,
            'S': Suit.SPADES,
            'C': Suit.CLUBS,
        }[s]


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    @staticmethod
    def from_string(s):
        rank = Rank.from_string(s[0] if len(s) == 2 else s[0:2])
        suit = Suit.from_string(s[-1])
        return Card(rank, suit)


def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        card_strings = test.split('|')[0].strip().split(' ')
        cards = [Card.from_string(c) for c in card_strings]
        card0, card1 = cards
        trump = Suit.from_string(test.split('|')[1].strip())

        # Choose the winner based on rank, then trump behavior.
        if card0.rank > card1.rank:
            winning_set = [0]
            if card1.suit == trump and card0.suit != trump:
                winning_set = [1]
        elif card1.rank > card0.rank:
            winning_set = [1]
            if card0.suit == trump and card1.suit != trump:
                winning_set = [0]
        else:
            winning_set = [0, 1]
            if card0.suit != card1.suit:
                if card0.suit == trump:
                    winning_set = [0]
                elif card1.suit == trump:
                    winning_set = [1]

        print(' '.join(card_strings[w] for w in winning_set))
    test_cases.close()

if __name__ == '__main__':
    main()
