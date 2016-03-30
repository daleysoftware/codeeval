import sys


def count(value, last_coin=50):
    if value == 0:
        return 1
    result = 0
    for coin in [50, 25, 10, 5, 1]:
        if coin <= value and coin <= last_coin:
            result += count(value - coin, coin)
    return result


def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0: continue
        test = int(test)
        print(count(test))
    test_cases.close()


if __name__ == '__main__':
    main()
