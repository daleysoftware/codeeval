import sys

class CardSuit:
    Hearts, Spades, Clubs, Diamonds = range(1, 5)

    def __init__(self):
        pass

    @staticmethod
    def string_to_suit(s):
        return {
            'S': CardSuit.Spades,
            'D': CardSuit.Diamonds,
            'C': CardSuit.Clubs,
            'H': CardSuit.Hearts
        }[s]

class CardValue:
    One, Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, Jack, Queen, King, Ace = range(1, 15)

    def __init__(self):
        pass

    @staticmethod
    def string_to_value(s):
        return {
            '1': CardValue.One,
            '2': CardValue.Two,
            '3': CardValue.Three,
            '4': CardValue.Four,
            '5': CardValue.Five,
            '6': CardValue.Six,
            '7': CardValue.Seven,
            '8': CardValue.Eight,
            '9': CardValue.Nine,
            'T': CardValue.Ten,
            'J': CardValue.Jack,
            'Q': CardValue.Queen,
            'K': CardValue.King,
            'A': CardValue.Ace
        }[s]

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return str('{0:x}'.format(self.value)) + ":" + str(self.suit)

    def __cmp__(self, other):
        return self.value - other.value

class PokerHand:
    def __init__(self, cards):
        self.cards = sorted(cards)
        self.value_to_count_map = {}
        for c in self.cards:
            if c.value in self.value_to_count_map:
                self.value_to_count_map[c.value] += 1
            else:
                self.value_to_count_map[c.value] = 1

    def _is_x_of_a_kind(self, x):
        for value in self.value_to_count_map.keys():
            count = self.value_to_count_map[value]
            if count == x:
                return True, value
        return False, 0

    def _is_all_same_suit(self):
        suit = self.cards[0].suit
        for c in self.cards:
            if c.suit != suit:
                return False
        return True

    def _is_continuously_increasing(self):
        previous = self.cards[0].value
        for c in self.cards[1:]:
            if c.value != previous+1:
                return False
            else:
                previous = c.value
        return True

    def is_one_pair(self):
        occurrences = 0
        weight = 0
        for value in self.value_to_count_map.keys():
            count = self.value_to_count_map[value]
            if count == 2:
                occurrences += 1
                weight = value
        return occurrences, weight

    def is_two_pairs(self):
        found = 0
        max_value = 0
        for value in self.value_to_count_map.keys():
            if self.value_to_count_map[value] == 2:
                found += 1
                max_value = max(max_value, value)
        return found == 2, max_value

    def is_three_of_a_kind(self):
        return self._is_x_of_a_kind(3)

    def is_straight(self):
        return self._is_continuously_increasing(), self.cards[-1].value

    def is_flush(self):
        return self._is_all_same_suit(), self.cards[-1].value

    def is_full_house(self):
        three_result = self.is_three_of_a_kind()
        return three_result[0] and self.is_one_pair()[0], three_result[1]

    def is_four_of_a_kind(self):
        return self._is_x_of_a_kind(4)

    def is_straight_flush(self):
        return self._is_continuously_increasing() and self._is_all_same_suit(), self.cards[-1].value

    def is_royal_flush(self):
        return self.cards[0].value == CardValue.Ten and self.is_straight_flush()[0], 0

    # Return < 0 if self < other, 0 if self == other, > 0 if self > other.
    def __cmp__(self, other):
        #print self
        #print other

        def render_result(s_result, o_result):
            if s_result[0] and o_result[0] and s_result[1] != o_result[1]:
                return True, s_result[1] - o_result[1]
            if s_result[0] and not o_result[0]:
                return True, 1
            if not s_result[0] and o_result[0]:
                return True, -1
            return False, 0

        # Royal flush.
        #print '--- royal'
        result = render_result(self.is_royal_flush(), other.is_royal_flush())
        if result[0]:
            return result[1]

        # Straight flush.
        #print '--- straight'
        result = render_result(self.is_straight_flush(), other.is_straight_flush())
        if result[0]:
            return result[1]

        # Four of a kind.
        #print '--- four'
        result = render_result(self.is_four_of_a_kind(), other.is_four_of_a_kind())
        if result[0]:
            return result[1]

        # Full house.
        #print '--- full'
        result = render_result(self.is_full_house(), other.is_full_house())
        if result[0]:
            return result[1]

        # Flush.
        #print '--- flush'
        result = render_result(self.is_flush(), other.is_flush())
        if result[0]:
            return result[1]

        # Straight.
        #print '--- straight'
        result = render_result(self.is_straight(), other.is_straight())
        if result[0]:
            return result[1]

        # Three of a kind.
        #print '--- three'
        result = render_result(self.is_three_of_a_kind(), other.is_three_of_a_kind())
        if result[0]:
            return result[1]

        # Two pairs.
        #print '--- two'
        result = render_result(self.is_two_pairs(), other.is_two_pairs())
        if result[0]:
            return result[1]

        # One pairs.
        #print '--- one'
        result = render_result(self.is_one_pair(), other.is_one_pair())
        if result[0]:
            return result[1]

        # High card.
        #print '--- high'
        for c1, c2 in zip(sorted(self.cards, reverse=True), sorted(other.cards, reverse=True)):
            if c1.value != c2.value:
                return c1.value - c2.value

        return 0

    def __str__(self):
        s = []
        for c in self.cards:
            s.append(c.__str__())
        return ",".join(s)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    cards = []
    for c in test.split(' '):
        cards.append(Card(CardValue.string_to_value(c[0]), CardSuit.string_to_suit(c[1])))

    hand1 = PokerHand(cards[0:5])
    hand2 = PokerHand(cards[5:10])

    compare = hand1.__cmp__(hand2)

    if compare == 0:
        print 'none'
    elif compare < 0: # hand1 < hand2, i.e. hand2 is better.
        print 'right'
    else:
        print 'left'

test_cases.close()