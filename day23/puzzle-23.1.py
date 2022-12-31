def neighbours(pos, elves):
    n = 0
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if (pos[0] + dx, pos[1] + dy) in elves:
                n += 1
    if pos in elves:
        n -= 1
    return n

def north(pos, elves):
    n = 0
    if (pos[0] - 1, pos[1] - 1) in elves: n += 1
    if (pos[0]    , pos[1] - 1) in elves: n += 1
    if (pos[0] + 1, pos[1] - 1) in elves: n += 1
    return n

def south(pos, elves):
    n = 0
    if (pos[0] - 1, pos[1] + 1) in elves: n += 1
    if (pos[0]    , pos[1] + 1) in elves: n += 1
    if (pos[0] + 1, pos[1] + 1) in elves: n += 1
    return n

def west(pos, elves):
    n = 0
    if (pos[0] - 1, pos[1] - 1) in elves: n += 1
    if (pos[0] - 1, pos[1]    ) in elves: n += 1
    if (pos[0] - 1, pos[1] + 1) in elves: n += 1
    return n

def east(pos, elves):
    n = 0
    if (pos[0] + 1, pos[1] - 1) in elves: n += 1
    if (pos[0] + 1, pos[1]    ) in elves: n += 1
    if (pos[0] + 1, pos[1] + 1) in elves: n += 1
    return n

def box(elves):
    x_pos = [elf[0] for elf in elves]
    y_pos = [elf[1] for elf in elves]
    n = min(y_pos)
    s = max(y_pos)
    e = max(x_pos)
    w = min(x_pos)
    return n, s, e, w

def show(elves):
    n, s, e, w = box(elves)
    for y in range(n, s + 1):
        for x in range(w, e + 1):
            print(('#' if (x, y) in elves else '.'), end='')
        print()
    print()

lines = [l.strip() for l in open("day23/input")]
elves = set()

for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == '#':
            elves.add((x, y))

#show(elves)

directions = [
    (north, 0, -1),
    (south, 0, 1),
    (west, -1, 0),
    (east, 1, 0)
]

for _ in range(10):
    proposed = {}

    for elf in elves:
        if not neighbours(elf, elves):
            continue

        for direction, dx, dy in directions:
            if not direction(elf, elves):
                dest = (elf[0] + dx, elf[1] + dy)
                if dest in proposed:
                    proposed[dest].append(elf)
                else:
                    proposed[dest] = [elf]
                break

    for dest, candidates in proposed.items():
        if len(candidates) == 1:
            elves.remove(candidates[0])
            elves.add(dest)

    directions.append(directions.pop(0))

    #show(elves)

n, s, e, w = box(elves)
size = (e - w + 1) * (s - n + 1)
empty = size - len(elves)

print(empty)
