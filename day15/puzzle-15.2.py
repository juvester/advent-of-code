import re

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def missing_element(segments):
    # Segments [(-2, 4), (0, 3), (5, 10)] form one continous segment (-2, 10) so return None.
    # Segments [(0, 1), (3, 4)] are not continous because 2 is missing. Return missing element.

    segments = sorted(segments)

    #start = segments[0][0]
    end = segments[0][1]
    for segment in segments[1:]:
        if segment[0] <= end + 1:
            end = max(end, segment[1])
        else:
            return end + 1
    return None

lines = [l.strip() for l in open("day15/input")]

sensors = []
radiuses = {}

N = 4000000

for line in lines:
    data = [int(x) for x in re.findall('-?\d+', line)]
    sensor = (data[0], data[1])
    beacon = (data[2], data[3])
    sensors.append(sensor)
    radiuses[sensor] = manhattan(sensor, beacon)

for row in range(0, N + 1):
    # List of x coordinate segments where no beacon can exist, e.g. [(-2, 4), (0, 3), (5, 10)]
    no_beacon = []

    for sensor in sensors:
        sensor_radius = radiuses[sensor]
        dist_to_row = abs(sensor[1] - row)

        if dist_to_row <= sensor_radius:
            i = sensor[0] - (sensor_radius - dist_to_row)
            j = sensor[0] + (sensor_radius - dist_to_row)

            no_beacon.append((i, j))

    col = missing_element(no_beacon)

    if col is not None:
        print('x:', col, 'y:', row, 'freq:', col * 4000000 + row)

        # "...find the only possible position..."
        break
