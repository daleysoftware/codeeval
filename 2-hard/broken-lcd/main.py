import sys


def main(input_filename):
    test_cases = open(input_filename, 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0:
            continue

        lcd_panel_state = test.split(';')[0].split(' ')
        number_to_display = test.split(';')[1].strip()
        # TODO finish solution

    test_cases.close()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python %s <input_filename>" % sys.argv[0])
        sys.exit(1)
    main(sys.argv[1])
