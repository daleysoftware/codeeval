import sys

def count_substring(string, substring):
    result = 0
    for i in range(0, len(string)-len(substring)+1):
        string_segment = string[i:i+len(substring)]
        if substring == string_segment:
            result += 1
    return result

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0: continue
        print(count_substring(test, '<--<<') + count_substring(test, '>>-->'))
    test_cases.close()

if __name__ == '__main__':
    main()
