import re

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

lines = [l.strip() for l in open("day15/input")]

target_row = 2000000
no_beacon = set()
beacons = set()

for line in lines:
    data = [int(x) for x in re.findall('-?\d+', line)]
    sensor = (data[0], data[1])
    beacon = (data[2], data[3])

    beacons.add(beacon)

    sensor_radius = manhattan(sensor, beacon)
    sensor_to_row = manhattan(sensor, (sensor[0], target_row))

    if sensor_to_row <= sensor_radius:
        i = sensor[0] - (sensor_radius - sensor_to_row)
        j = sensor[0] + (sensor_radius - sensor_to_row)

        no_beacon.update(range(i, j+1))

for beacon in beacons:
    if beacon[1] == target_row and beacon[0] in no_beacon:
        no_beacon.remove(beacon[0])

print(len(no_beacon))
