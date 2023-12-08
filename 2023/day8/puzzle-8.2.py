import math


with open('2023/day8/input') as file:
    lines = file.read().splitlines()

instructions = lines[0]

graph = {}
positions = []
goals = []
for line in lines[2:]:
    node = line[0:3]
    left = line[7:10]
    right = line[12:15]
    graph[node] = (left, right)
    if node[-1] == 'A':
        positions.append(node)
    if node[-1] == 'Z':
        goals.append(node)


# positions: ['JQA', 'NHA', 'AAA', 'FSA', 'LLA', 'MNA']
# goals:     ['GVZ', 'NQZ', 'DDZ', 'SCZ', 'PTZ', 'ZZZ']

# All positions seem to have a nicely constructed loop:
# JQA -> FKM -> ... -> SCZ -> FKM -> ...    (length: 13939)
# NHA -> NXC -> ... -> DDZ -> NXC -> ...    (length: 11309)
# AAA -> TTH -> ... -> ZZZ -> TTH -> ...    (length: 20777)
# FSA -> NVH -> ... -> PTZ -> NVH -> ...    (length: 15517)
# LLA -> KCL -> ... -> NQZ -> KCL -> ...    (length: 17621)
# MNA -> HRT -> ... -> GVZ -> HRT -> ...    (length: 18673)


loop_lengths = []
for pos in positions:
    i = 0
    while pos[-1] != 'Z':
        dir = 0 if instructions[i % len(instructions)] == 'L' else 1
        pos = graph[pos][dir]
        i += 1
    loop_lengths.append(i)

part2 = math.lcm(*loop_lengths)
print(part2)
