import sys

discrete_options = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]

discrete_options_mapping = {
    1: 'PENNY',
    5: 'NICKEL',
    10: 'DIME',
    25: 'QUARTER',
    50: 'HALF DOLLAR',
    100: 'ONE',
    200: 'TWO',
    500: 'FIVE',
    1000: 'TEN',
    2000: 'TWENTY',
    5000: 'FIFTY',
    10000: 'ONE HUNDRED'
}

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0: continue
        total = int(float(test.split(";")[0]) * 100)
        given = int(float(test.split(";")[1]) * 100)
        change = given - total
        if change == 0:
            print('ZERO')
            continue
        if change < 0:
            print('ERROR')
            continue
        result = []
        for option in discrete_options:
            while change >= option:
                change = change - option
                result.append(discrete_options_mapping[option])
        print(','.join(result))
    test_cases.close()

if __name__ == '__main__':
    main()
