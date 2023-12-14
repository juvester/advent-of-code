def draw(grid: list):
    for row in grid:
        print(''.join(row))
    print()


def tilt_north(grid: list):
    for c in range(len(grid[0])):
        for r in range(1, len(grid)):
            while r > 0 and grid[r-1][c] == '.' and grid[r][c] == 'O':
                grid[r-1][c], grid[r][c] = grid[r][c], grid[r-1][c]
                r -= 1


def tilt_south(grid: list):
    height = len(grid)
    for c in range(len(grid[0])):
        for r in range(height-2, -1, -1):
            while r < height-1 and grid[r+1][c] == '.' and grid[r][c] == 'O':
                grid[r+1][c], grid[r][c] = grid[r][c], grid[r+1][c]
                r += 1


def tilt_west(grid: list):
    for r in range(len(grid)):
        for c in range(1, len(grid[r])):
            while c > 0 and grid[r][c-1] == '.' and grid[r][c] == 'O':
                grid[r][c-1], grid[r][c] = grid[r][c], grid[r][c-1]
                c -= 1


def tilt_east(grid: list):
    width = len(grid[0])
    for r in range(len(grid)):
        for c in range(width-2, -1, -1):
            while c < width-1 and grid[r][c+1] == '.' and grid[r][c] == 'O':
                grid[r][c+1], grid[r][c] = grid[r][c], grid[r][c+1]
                c += 1


def load(grid):
    load = 0
    for i, row in enumerate(grid):
        load += row.count('O')*(len(grid)-i)
    return load


with open("2023/day14/input") as file:
    grid = [list(line.strip()) for line in file]

tilt_north(grid)
part1 = load(grid)

for cycle in range(1, 1000):
    tilt_north(grid)
    tilt_west(grid)
    tilt_south(grid)
    tilt_east(grid)

    # The loads have formed a pattern by cycle ~130
    # The pattern is 7 items long
    # So we can skip 7n cycles:
    #   130 + 7n = 1000000000
    #          n = (1000000000 - 130) / 7
    #          n = 142857124.286
    simulated_cycle = cycle + 7*142857124

    print(load(grid), cycle, simulated_cycle)

    if simulated_cycle == 1000000000:
        part2 = load(grid)
        break

print("Part 1:", part1)
print("Part 2:", part2)
