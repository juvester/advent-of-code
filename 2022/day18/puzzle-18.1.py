lines = [l.strip() for l in open("day18/input")]

cubes = set()
result = 0

for line in lines:
    x, y, z = [int(x) for x in line.split(',')]
    sides_free = 6

    if (x+1, y, z) in cubes:
        sides_free -= 2
    if (x-1, y, z) in cubes:
        sides_free -= 2
    if (x, y+1, z) in cubes:
        sides_free -= 2
    if (x, y-1, z) in cubes:
        sides_free -= 2
    if (x, y, z+1) in cubes:
        sides_free -= 2
    if (x, y, z-1) in cubes:
        sides_free -= 2

    result += sides_free
    cubes.add((x, y, z))

print(result)
