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

def limits(cubes):
    min_x = min([c[0] for c in cubes])
    max_x = max([c[0] for c in cubes])
    min_y = min([c[1] for c in cubes])
    max_y = max([c[1] for c in cubes])
    min_z = min([c[2] for c in cubes])
    max_z = max([c[2] for c in cubes])
    return (min_x, min_y, min_z), (max_x, max_y, max_z)

def adjacent(pos, cubes):
    adj = []
    if (pos[0]+1, pos[1], pos[2]) not in cubes:
        adj.append((pos[0]+1, pos[1], pos[2]))
    if (pos[0]-1, pos[1], pos[2]) not in cubes:
        adj.append((pos[0]-1, pos[1], pos[2]))
    if (pos[0], pos[1]+1, pos[2]) not in cubes:
        adj.append((pos[0], pos[1]+1, pos[2]))
    if (pos[0], pos[1]-1, pos[2]) not in cubes:
        adj.append((pos[0], pos[1]-1, pos[2]))
    if (pos[0], pos[1], pos[2]+1) not in cubes:
        adj.append((pos[0], pos[1], pos[2]+1))
    if (pos[0], pos[1], pos[2]-1) not in cubes:
        adj.append((pos[0], pos[1], pos[2]-1))
    return adj

def is_pocket(pos, cubes, cube_min, cube_max):
    """ BFS to see if there's a path from pos to outside """
    q = [pos]
    visited = set([pos])
    while q:
        v = q.pop(0)
        if (
            v[0] < cube_min[0] or v[1] < cube_min[1] or v[2] < cube_min[2] or
            v[0] > cube_max[0] or v[1] > cube_max[1] or v[2] > cube_max[2]
        ):
            return False
        for w in adjacent(v, cubes):
            if w not in visited:
                visited.add(w)
                q.append(w)
    return True

cube_min, cube_max = limits(cubes)

for x in range(cube_min[0], cube_max[0]+1):
    for y in range(cube_min[1], cube_max[1]+1):
        for z in range(cube_min[2], cube_max[2]+1):
            if (x, y, z) in cubes:
                continue
            if is_pocket((x, y, z), cubes, cube_min, cube_max):
                if (x+1, y, z) in cubes:
                    result -= 1
                if (x-1, y, z) in cubes:
                    result -= 1
                if (x, y+1, z) in cubes:
                    result -= 1
                if (x, y-1, z) in cubes:
                    result -= 1
                if (x, y, z+1) in cubes:
                    result -= 1
                if (x, y, z-1) in cubes:
                    result -= 1

print(result)
