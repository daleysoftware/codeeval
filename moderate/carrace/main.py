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
        self.top_speed = int(info_list[1])
        self.time_to_accelerate = float(info_list[2])
        self.time_to_stop = float(info_list[3])

def calculate_lap_time(track, car):
    # TODO finish this.
    return 0

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
    print str(times[time]) + " " + str(time)