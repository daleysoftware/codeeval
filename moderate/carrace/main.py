import sys

class Track:
    def __init__(self, length_angle_list):
        self.length_angles = []

        for i in range(0, len(length_angle_list), 2):
            length = float(length_angle_list[i])
            angle = int(length_angle_list[i+1])
            self.length_angles.append([float(length), int(angle)])

class Car:
    def __init__(self, info_string):
        info_list = info_string.split(' ')

        self.car_number = int(info_list[0])
        self.top_speed = int(info_list[1]) / 60.0 / 60.0
        self.time_to_accelerate = float(info_list[2])
        self.time_to_stop = float(info_list[3])


# 1. A car is weightless, it is just a point.
# 2. A car accelerates and breaks with a constant acceleration.
# 3. A car can pass through a 0 degree turn with its top speed, and it must
#    break to 0 MPH if a turn degree is 180.
# 4. A car starts with 0 MPH speed, accelerates to its top speed, than goes at
#    the top speed as long as possible, than breaks as late as possible to reach
#    the allowed turn speed, then after the turn immediately accelerates from
#    the turn speed to the top speed and so on.
# 5. No time is needed to pass a turn, it's just a point and at that point the
#    speed of a car must be exactly the same as the allowed turn speed.
# 6. A length of a track section will always allow a car to reach it's top
#    speed.
def calculate_lap_time(track, car):
    a_up = car.top_speed / car.time_to_accelerate
    a_down = car.top_speed / car.time_to_stop

    total_time = 0.0
    v_i = 0.0

    for t in track.length_angles:
        length = t[0]
        angle = t[1]

        new_v_i = (1 - angle / 180.0) * car.top_speed

        # Going up.
        t_up = (car.top_speed - v_i) / a_up
        d_up = v_i * t_up + 0.5 * a_up * t_up * t_up

        # Going down.
        t_down = (car.top_speed - new_v_i) / a_down
        d_down = car.top_speed * t_down - 0.5 * a_down * t_down * t_down

        # At the top.
        d_top = length - d_up - d_down
        t_top = d_top / car.top_speed

        total_time += t_up + t_top + t_down
        v_i = new_v_i

    return total_time

test_cases = open(sys.argv[1], 'r')

track = Track(test_cases.readline().split(' '))
cars = []

for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue

    cars.append(Car(test.strip()))

test_cases.close()

times = {}
for car in cars:
    time = calculate_lap_time(track, car)
    times[time] = car.car_number

for time in sorted(times.keys()):
    print("%i %.2f" % (times[time], round(time, 2)))