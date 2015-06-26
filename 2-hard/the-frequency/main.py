# FIXME codeval does not allow you to use numpy
import numpy
import sys

SEGMENTS = 10
SAMPLE_INTERVAL = 0.00005
MAX_NOISE_PERCENTAGE = 0.1

def zero(data):
    """
    Given a signal, zero it out by finding a best fit curve and subtracting out the average value
    of the signal.
    """
    result = []
    [m, b] = numpy.polyfit(list(range(0, len(data))), data, 1)

    for i in range(0, len(data)):
        result.append(data[i] - m * i + b)

    a = sum(result)/len(result)
    result = [a - r for r in result]

    return result

def normalize(data, segments):
    """
    Break a signal into segments, average out the segments, and normalize the amplitude of each
    segment using that average.
    """

    segment_length = len(data) / segments

    for i in range(0, segments):
        segment = data[i * segment_length : (i+1) * segment_length]
        segment_abs_max = max([abs(s) for s in segment])

        for j in range(0, segment_length):
            data[i * segment_length + j] /= segment_abs_max

    return data

def truncate_to_nearest_10(x):
    return x - (x % 10)

def remove_adjacent_repeated(data):
    result = [data[0]]
    for i in range(1, len(data)):
        if data[i] != data[i-1]:
            result.append(data[i])
    return result

def determine_frequency(data, max_noise_percentage, sample_interval):
    """
    Count the number of times a signal crosses the zero level. Take into consideration noise with
    some maximum amplitude as a percentage of the data amplitude.

    Assume the given signal is zeroed and normalized.
    """

    states = []
    for d in data:
        if d < max_noise_percentage:
            states.append(-1)
        elif d > max_noise_percentage:
            states.append(1)
        else:
            states.append(0)

    # Some sneaky logic to make sure that we exclude the little bits at the beginning and end of the
    # signal, so our frequency is as accurate as possible.
    start = 0
    for i in range(0, len(states)-1):
        if (states[i] == 0 or states[i] == -1) and states[i+1] == 1:
            start = i
            break

    end = len(states)-1
    for i in range(len(states)-1, 0, -1):
        if (states[i-1] == 0 or states[i-1] == -1) and states[i] == 1:
            # Important: trim the end.
            end = i-1
            break

    length = end - start + 1
    states = remove_adjacent_repeated([s for s in states[start:end+1] if s != 0])

    state_changes = len(states)
    total_seconds = length * sample_interval

    return truncate_to_nearest_10(int(state_changes / total_seconds / 2.0))

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0: continue

        data = zero([float(x) for x in test.split(' ')])
        data = normalize(data, SEGMENTS)

        print(determine_frequency(data,
                                  max_noise_percentage=MAX_NOISE_PERCENTAGE,
                                  sample_interval=SAMPLE_INTERVAL))
    test_cases.close()

if __name__ == '__main__':
    main()
