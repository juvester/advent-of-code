with open('2023/day6/input') as file:
    time = int(''.join(file.readline().split()[1:]))
    dist = int(''.join(file.readline().split()[1:]))

part2 = 0
for ms in range(0, time+1):
    d = ms*(time-ms)
    if d > dist:
        part2 += 1
print(part2)
