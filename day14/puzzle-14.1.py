import re

def convert_paths(paths, min_x):
    """ Convert all x coordinates to start from 0. """
    converted = []
    for path in paths:
        converted.append(list(map(lambda c: (c[0]-min_x, c[1]), path)))
    return converted

def get_size_range(paths):
    min_x = paths[0][0][0]
    max_x = paths[0][0][0]
    min_y = 0
    max_y = paths[0][0][1]

    for path in paths:
        min_x = min(min_x, min(path)[0])
        max_x = max(max_x, max(path)[0])
        max_y = max(max_y, max(path, key=lambda coord: coord[1])[1])

    return min_x, max_x, min_y, max_y

def get_paths(lines: list[str]) -> list:
    paths = []
    for line in lines:
        numbers = [int(x) for x in re.findall('\d+', line)]
        path = [(numbers[i-1], numbers[i]) for i in range(1, len(numbers), 2)]
        paths.append(path)
    return paths

def print_grid(grid):
    for row in grid:
        print(''.join(row))
    print()

def draw_rocks(start, end, grid):
    if start > end:
        start, end = end, start
    for x in range(start[0], end[0]+1):
        for y in range(start[1], end[1]+1):
            grid[y][x] = '#'

def draw_path(path, grid):
    for i in range(1, len(path)):
        start = path[i - 1]
        end = path[i]
        draw_rocks(start, end, grid)

def pour_sand(grid, source):
    x = source[0]
    y = source[1]

    while True:
        try:
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
        except:
            return False

        break

    grid[y][x] = 'o'
    return True

def main():
    lines = [line.strip() for line in open("day14/input")]
    paths = get_paths(lines)
    min_x, max_x, min_y, max_y = get_size_range(paths)
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    grid = [['.'] * width for _ in range(height)]
    paths = convert_paths(paths, min_x)
    for path in paths:
        draw_path(path, grid)
    source = (500 - min_x, 0)
    grid[source[1]][source[0]] = '+'
    #print_grid(grid)
    result = 0
    while pour_sand(grid, source):
        result += 1
        #print_grid(grid)

    print(result)

main()
