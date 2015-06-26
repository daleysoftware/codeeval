import sys

class SearchString:
    def __init__(self, raw):
        self.array = []
        for c in raw:
            self.array.append(c)

    def is_match(self, s, index):
        if index + len(s) > len(self.array):
            return False

        match = True
        for i in range(len(s)):
            if self.array[index + i] != s[i]:
                match = False
                break

        return match

    def find_and_replace(self, s, r):
        for i in range(len(self.array)):
            if self.is_match(s, i):
                self.array[i] = "x" + r

                for j in range(1, len(s)):
                    self.array[i+j] = ""

    def render(self):
        return "".join(self.array).replace("x", "")

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    s = SearchString(test.split(';')[0])
    subs = test.split(';')[1].split(',')

    for i in range(0, len(subs), 2):
        s.find_and_replace(subs[i], subs[i+1])

    print(s.render())

test_cases.close()
