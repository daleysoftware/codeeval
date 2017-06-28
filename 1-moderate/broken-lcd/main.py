import sys


def int_to_lcd_binary(i):
    """
    Convert an integer to a sequence of bits representing the state of the LCD screen.
    """
    return {
        0: 0b11111100,
        1: 0b01100000,
        2: 0b11011010,
        3: 0b11110010,
        4: 0b01100110,
        5: 0b10110110,
        6: 0b10111110,
        7: 0b11100000,
        8: 0b11111110,
        9: 0b11110110,
    }[i]


def string_to_lcd_binary(s):
    """
    Convert a string representation of an integer to a sequence of bits representing the state of
    the LCD screen.
    """
    result = []
    for i in range(len(s)):
        current = s[i]
        if current != '.':
            result.append(int_to_lcd_binary(int(current)))
        else:
            result[-1] |= 0b00000001
    return result


def can_display_number_on_lcd(number_to_display, lcd_panel_state):
    if len(number_to_display) > len(lcd_panel_state):
        return False
    for offset in range(len(lcd_panel_state) - len(number_to_display) + 1):
        failure = False
        for i in range(len(number_to_display)):
            if number_to_display[i] & lcd_panel_state[i + offset] != number_to_display[i]:
                failure = True
                break
        if not failure:
            return True
    return False


def main(input_filename):
    test_cases = open(input_filename, 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0:
            continue
        lcd_panel_state = [int(x, 2) for x in test.split(';')[0].split(' ')]
        number_to_display = string_to_lcd_binary(test.split(';')[1].strip())
        print(1 if can_display_number_on_lcd(number_to_display, lcd_panel_state) else 0)
    test_cases.close()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python %s <input_filename>" % sys.argv[0])
        sys.exit(1)
    main(sys.argv[1])
