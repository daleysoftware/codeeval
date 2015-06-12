import sys

def decimal_degree_to_minutes_seconds(decimal_degree):
    degree = int(decimal_degree)
    minutes = int((decimal_degree-degree) * 60)
    seconds = int((decimal_degree-degree-(minutes/60.0)) * 3600)
    return degree, minutes, seconds

def format_degree_minutes_seconds(minutes_seconds_degree):
    return '%i.%02i\'%02i"' % minutes_seconds_degree

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0:
            continue
        decimal_degree = float(test)
        minutes_seconds_degree = decimal_degree_to_minutes_seconds(decimal_degree)
        print(format_degree_minutes_seconds(minutes_seconds_degree))
    test_cases.close()

if __name__ == '__main__':
    main()
