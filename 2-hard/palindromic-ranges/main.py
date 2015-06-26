import sys

def is_palindrome(x):
    x = str(x)
    counter = 0
    while counter <= len(x)/2:
        left = x[counter]
        right = x[len(x) - counter - 1]
        if left != right:
            return False
        counter += 1
    return True

def count_palindromic_ranges(palindrome_array):
    result = 0
    for width in range(1, len(palindrome_array)+1):
        for start in range(len(palindrome_array)):
            if start + width > len(palindrome_array):
                break
            palindrome_count = 0
            for i in range(start, start+width):
                if palindrome_array[i]:
                    palindrome_count += 1
            if palindrome_count % 2 == 0:
                result += 1
    return result

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue
    L = int(test.split(" ")[0])
    R = int(test.split(" ")[1])
    palindrome_array = []
    for i in range(L, R+1):
        palindrome_array.append(is_palindrome(i))
    print(count_palindromic_ranges(palindrome_array))

test_cases.close()
