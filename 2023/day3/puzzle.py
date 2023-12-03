import re


def has_symbol(schematic, x1, y1, x2, y2):
    h = len(schematic)
    w = len(schematic[0])

    for y in range(y1, y2):
        for x in range(x1, x2):
            if x < 0 or x >= w or y < 0 or y >= h:
                continue
            if schematic[y][x] != '.' and schematic[y][x] not in '0123456789':
                return True

    return False

def adj_gears(schematic, x1, y1, x2, y2):
    h = len(schematic)
    w = len(schematic[0])

    gears = []

    for y in range(y1, y2):
        for x in range(x1, x2):
            if x < 0 or x >= w or y < 0 or y >= h:
                continue
            if schematic[y][x] == '*':
                gears.append((x, y))

    return gears

with open('2023/day3/input') as file:
    schematic = [line.strip() for line in file.readlines()]

p1 = 0
p2 = 0

gears = {}

for y in range(len(schematic)):
    for re_match in re.finditer(r'\d+', schematic[y]):
        number = int(re_match.group())
        x1 = re_match.start() - 1
        y1 = y - 1
        x2 = re_match.end() + 1
        y2 = y + 2

        if has_symbol(schematic, x1, y1, x2, y2):
            p1 += number

        for gear in adj_gears(schematic, x1, y1, x2, y2):
            if gear not in gears:
                gears[gear] = []
            gears[gear].append(number)

for gear, numbers in gears.items():
    if len(numbers) != 2:
        continue
    p2 += numbers[0] * numbers[1]

print(p1)
print(p2)
