with open('2023/day6/input') as file:
    times = [int(x) for x in file.readline().split()[1:]]
    dists = [int(x) for x in file.readline().split()[1:]]

part1 = 1
for time, dist in zip(times, dists):
    ways = 0
    for ms in range(0, time+1):
        d = ms*(time-ms)
        if d > dist:
            ways += 1
    part1 *= ways
print(part1)
