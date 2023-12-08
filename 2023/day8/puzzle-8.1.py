with open('2023/day8/input') as file:
    lines = file.read().splitlines()

instructions = lines[0]

graph = {}
for line in lines[2:]:
    node = line[0:3]
    left = line[7:10]
    right = line[12:15]
    graph[node] = (left, right)

i = 0
pos = 'AAA'
while pos != 'ZZZ':
    pos = graph[pos][0 if instructions[i % len(instructions)] == 'L' else 1]
    i += 1

print(i)
