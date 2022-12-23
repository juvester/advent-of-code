windpattern = [c for c in open("day17/input").read().strip()]
wind = 0

shapes = [
    [(0,2), (0,3), (0,4), (0,5)],
    [(0,3), (1,2), (1,3), (1,4), (2,3)],
    [(0,2), (0,3), (0,4), (1,4), (2,4)],
    [(0,2), (1,2), (2,2), (3,2)],
    [(0,2), (0,3), (1,2), (1,3)]
]

def draw(stopped, rock):
    highest = 10 if not stopped else max(stopped)[0]+7
    for y in range(highest, -1, -1):
        for x in range(7):
            if (y, x) in stopped:
                print('#', end='')
            elif (y, x) in rock:
                print('@', end='')
            else:
                print('.', end='')
        print()
    print()

def top(stopped, rock):
    highest = 0 if not stopped else max(stopped)[0] + 1
    return [(highest + 3 + p[0], p[1]) for p in rock]

def right(stopped, rock):
    moved = []
    for piece in rock:
        x = piece[1] + 1
        if x < 0 or x >= 7 or (piece[0], x) in stopped:
            return rock
        moved.append((piece[0], x))
    return moved

def left(stopped, rock):
    moved = []
    for piece in rock:
        x = piece[1] - 1
        if x < 0 or x >= 7 or (piece[0], x) in stopped:
            return rock
        moved.append((piece[0], x))
    return moved

def down(stopped, rock):
    moved = []
    for piece in rock:
        y = piece[0] - 1
        if y < 0 or (y, piece[1]) in stopped:
            return True, rock
        moved.append((y, piece[1]))
    return False, moved

stopped = set()

for i in range(2022):
    rock = shapes[i % len(shapes)]
    rock = top(stopped, rock)

    while True:
        if windpattern[wind % len(windpattern)] == '>':
            rock = right(stopped, rock)
        else:
            rock = left(stopped, rock)
        wind += 1

        stop, rock = down(stopped, rock)

        if stop:
            stopped.update(rock)
            break

print(max(stopped)[0]+1)
