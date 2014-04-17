import sys

class Rectangle:
    def __init__(self,
                 upper_left_x, upper_left_y,
                 lower_right_x, lower_right_y):
        self.upper_left_x = upper_left_x
        self.upper_left_y = upper_left_y
        self.lower_right_x = lower_right_x
        self.lower_right_y = lower_right_y

    def contains_point(self, x, y):
        fits_in_x = self.upper_left_x <= x <= self.lower_right_x
        fits_in_y = self.lower_right_y <= y <= self.upper_left_y

        return fits_in_x and fits_in_y

    def overlaps_with_rectangle(self, rectangle):
        # Left side
        for y in range(self.lower_right_y, self.upper_left_y+1):
            if rectangle.contains_point(self.upper_left_x, y):
                return True

        # Top side
        for x in range(self.upper_left_x, self.lower_right_x+1):
            if rectangle.contains_point(x, self.upper_left_y):
                return True

        # Right side
        for y in range(self.lower_right_y, self.upper_left_y+1):
            if rectangle.contains_point(self.lower_right_x, y):
                return True

        # Bottom side
        for x in range(self.upper_left_x, self.lower_right_x+1):
            if rectangle.contains_point(x, self.lower_right_y):
                return True

        return False

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    coordinates = test.split(",")

    # Upper left and lower right corners of rectangle A.
    a_upper_left_x = int(coordinates[0])
    a_upper_left_y = int(coordinates[1])
    a_lower_right_x = int(coordinates[2])
    a_lower_right_y = int(coordinates[3])

    # Upper left and lower right corners of rectangle B.
    b_upper_left_x = int(coordinates[4])
    b_upper_left_y = int(coordinates[5])
    b_lower_right_x = int(coordinates[6])
    b_lower_right_y = int(coordinates[7])

    a = Rectangle(a_upper_left_x, a_upper_left_y,
                  a_lower_right_x, a_lower_right_y)
    b = Rectangle(b_upper_left_x, b_upper_left_y,
                  b_lower_right_x, b_lower_right_y)

    print a.overlaps_with_rectangle(b)

test_cases.close()
