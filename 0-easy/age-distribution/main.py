import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    age = int(test)

    if age < 0 or age > 100:
        print "This program is for humans"
        continue

    if age <= 2:
        print "Still in Mama's arms"
    elif age <= 4:
        print "Preschool Maniac"
    elif age <= 11:
        print "Elementary school"
    elif age <= 14:
        print "Middle school"
    elif age <= 18:
        print "High school"
    elif age <= 22:
        print "College"
    elif age <= 65:
        print "Working for the man"
    else:
        print "The Golden Years"

test_cases.close()