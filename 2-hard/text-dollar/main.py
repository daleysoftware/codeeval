import sys
import math

def number_to_text(n):
    n = math.floor(n)
    if n < 20:
        return {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen"
        }[n]
    elif n < 100:
        result = {
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety"
        }[math.floor(n/10.0)*10]
        if n % 10 != 0:
            result += number_to_text(n % 10)
        return result
    elif n < 1000:
        result = number_to_text(n/100) + "Hundred"
        if n % 100 > 0:
            result += number_to_text(n % 100)
        return result
    elif n < 1000000:
        result = number_to_text(n/1000) + "Thousand"
        if n % 1000 > 0:
            result += number_to_text(n % 1000)
        return result
    elif n < 10**9:
        result = number_to_text(n/10**6) + "Million"
        if n % 10**6 > 0:
            result += number_to_text(n % 10**6)
        return result
    else:
        result = number_to_text(n/10**9) + "Billion"
        if n % 10**9 > 0:
            result += number_to_text(n % 10**9)
        return result

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    n = int(test)
    print(number_to_text(n) + "Dollars")

test_cases.close()
