def draw_rocks(grid, start, end):
    if start > end:
        start, end = end, start
    for x in range(start[0], end[0]+1):
        for y in range(start[1], end[1]+1):
            grid[y][x] = '#'

def pour_sand(grid, source):
    x, y = source

    while True:
        if y+1 >= len(grid):
            return False
        if grid[y+1][x] == '.':
            y += 1
            continue
        if grid[y+1][x-1] == '.':
            y += 1
            x -= 1
            continue
        if grid[y+1][x+1] == '.':
            y += 1
            x += 1
            continue
        break

    grid[y][x] = 'o'
    return True

N = 1000

source = (500, 0)
grid = [['.'] * N for _ in range(N)]
lines = [line.strip() for line in open("day14/input")]

for line in lines:
    points = line.split(' -> ')
    path = []
    for point in points:
        x, y = point.split(',')
        x, y = int(x), int(y)
        path.append((x, y))
    for i in range(1, len(path)):
        draw_rocks(grid, path[i-1], path[i])

grid[source[1]][source[0]] = '+'

sand_poured = 0
while pour_sand(grid, source):
    sand_poured += 1

print(sand_poured)
