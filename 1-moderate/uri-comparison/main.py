import sys
import re

def normalize(uri):
    while True:
        match = re.search('%([0-9a-fA-F][0-9a-fA-F])', uri)

        if match is not None:
            old_value = match.group(0)
            new_value = bytes.fromhex(match.group(1)).decode('utf-8')
            uri = uri.replace(old_value, new_value)
        else:
            break

    return uri

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    uri1 = normalize(test.split(';')[0])
    uri2 = normalize(test.split(';')[1])

    match = "^([a-zA-Z]+)://([a-zA-Z0-9.]+):?([0-9]+)?(.*)"

    m1 = re.match(match, uri1)
    m2 = re.match(match, uri2)

    if m1 is None or m2 is None:
        print('False')
        continue

    scheme1 = m1.group(1).lower()
    scheme2 = m2.group(1).lower()

    host1 = m1.group(2).lower()
    host2 = m2.group(2).lower()

    port1 = 80 if m1.group(3) is None else int(m1.group(3))
    port2 = 80 if m2.group(3) is None else int(m2.group(3))

    path1 = m1.group(4).lower()
    path2 = m2.group(4).lower()

    if scheme1 == scheme2 and host1 == host2 and port1 == port2 and path1 == path2:
        print('True')
    else:
        print('False')

test_cases.close()
