import sys

def search(to_search, pattern):
    to_search = to_search.replace("*", "#")
    pattern = pattern.replace("\\*", "#")

    for p in pattern.split("*"):
        found_index = to_search.find(p)
        if found_index < 0:
            return False

        to_search = to_search[found_index+len(p):]

    return True

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    to_search = test.split(",")[0]
    pattern = test.split(",")[1]

    print('true' if search(to_search, pattern) else 'false')

test_cases.close()
