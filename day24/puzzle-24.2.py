def move(blizzards, width, height):
    moved = set()
    for b in blizzards:
        moved.add(((b[0]+b[2]) % width, (b[1]+b[3]) % height, b[2], b[3], b[4]))
    return moved

def show(blizzards, positions, width, height):
    occupied = {(b[0], b[1]) for b in blizzards}
    grid = [['.'] * width for _ in range(height)]
    for x, y in occupied:
        grid[y][x] = '#'
    for x, y in positions:
        assert (x, y) not in occupied
        grid[y][x] = 'E'
    for row in grid:
        print(''.join(row))
    print()

lines = [l.strip() for l in open("day24/input")]
blizzards = set()
width = len(lines[0])-2
height = len(lines)-2
start_ = (0, 0)
goal_  = (width-1, height-1)

for y, line in enumerate(lines[1:-1]):
    for x, c in enumerate(line[1:-1]):
        if   c == '<': blizzards.add((x, y, -1,  0, c))
        elif c == '>': blizzards.add((x, y,  1,  0, c))
        elif c == '^': blizzards.add((x, y,  0, -1, c))
        elif c == 'v': blizzards.add((x, y,  0,  1, c))

round = 1

for start, goal in [(start_, goal_), (goal_, start_), (start_, goal_)]:
    current_positions = set()
    #show(blizzards, current_positions, width, height)

    while goal not in current_positions:
        next_blizzards = move(blizzards, width, height)
        next_occupied = {(b[0], b[1]) for b in next_blizzards}

        next_positions = set()

        for x, y in current_positions:
            if (x, y) not in next_occupied:
                next_positions.add((x, y))
            if 0 <= x-1 < width and (x-1, y) not in next_occupied:
                next_positions.add((x-1, y))
            if 0 <= x+1 < width and (x+1, y) not in next_occupied:
                next_positions.add((x+1, y))
            if 0 <= y-1 < height and (x, y-1) not in next_occupied:
                next_positions.add((x, y-1))
            if 0 <= y+1 < height and (x, y+1) not in next_occupied:
                next_positions.add((x, y+1))

        if start not in next_occupied:
            next_positions.add(start)

        blizzards = next_blizzards
        current_positions = next_positions
        round += 1

        #show(blizzards, current_positions, width, height)

print(round)
