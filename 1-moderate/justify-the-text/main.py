import sys
import bisect

def get_lengths_for_word_list(word_list):
    if len(word_list) == 0:
        return []
    lengths = [len(word_list[0])]
    for i in xrange(1, len(word_list)):
        lengths.append(lengths[i-1] + len(word_list[i]) + 1)
    return lengths

def print_justified(text):
    word_list = text.split(' ')

    while True:
        lengths = get_lengths_for_word_list(word_list)
        last_word_index = bisect.bisect(lengths, 80)-1
        line_list = word_list[0:last_word_index+1]
        word_list = word_list[last_word_index+1:]

        if len(word_list) == 0:
            print ' '.join(line_list)
            break

        # TODO finish
        extra_spaces = 80 - len(' '.join(line_list))
        word_breaks = len(line_list) - 1
        average_extra_spaces = extra_spaces / word_breaks
        spare_spaces = extra_spaces - average_extra_spaces * word_breaks

        for word in line_list[:-1]:
            sys.stdout.write(word)
            sys.stdout.write(' ' * (average_extra_spaces + 1))

            if spare_spaces > 0:
                sys.stdout.write(' ')
                spare_spaces -= 1

        sys.stdout.write(line_list[-1])
        sys.stdout.write('\n')

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0: continue
        print_justified(test)
    test_cases.close()

if __name__ == '__main__':
    main()