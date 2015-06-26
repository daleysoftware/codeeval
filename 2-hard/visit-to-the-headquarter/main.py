import sys

# TODO finish.

def string_to_time(s):
    s_split = s.split(':')
    return int(s_split[0]) * 3600 + int(s_split[1]) * 60 + int(s_split[2])

def time_to_string(t):
    h = (t / 3600)
    m = (t / 60 ) % 60
    s = t % 3600 % 60
    return "%02d:%02d:%02d" % (h, m, s)

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0:
            continue

        test_split = test.split(' ')

        agent = ord(test_split[0])
        start_time = string_to_time(test_split[1])
        rooms_and_times = []

        for i in range(2, len(test_split), 2):
            rooms_and_times.append([test_split[i], int(test_split[i+1])])

        # TODO remove this.
        print(agent)
        print(start_time)
        print(rooms_and_times)

    test_cases.close()

if __name__ == "__main__":
    main()
