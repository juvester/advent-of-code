windpattern = [c for c in open("day17/input").read().strip()]
wind = 0

rocks = [
    [(0,2), (0,3), (0,4), (0,5)],
    [(0,3), (1,2), (1,3), (1,4), (2,3)],
    [(0,2), (0,3), (0,4), (1,4), (2,4)],
    [(0,2), (1,2), (2,2), (3,2)],
    [(0,2), (0,3), (1,2), (1,3)]
]

"""
def draw(frozen_rocks, rock):
    highest = 10 if not frozen_rocks else max(frozen_rocks)[0]+7
    for y in range(highest, -1, -1):
        for x in range(7):
            if (y, x) in frozen_rocks:
                print('#', end='')
            elif (y, x) in rock:
                print('@', end='')
            else:
                print('.', end='')
        print()
    print()
"""

def start_pos(frozen_rocks, rock):
    highest = 0 if not frozen_rocks else max(frozen_rocks)[0] + 1
    return [(highest + 3 + p[0], p[1]) for p in rock]

def right(frozen_rocks, rock):
    moved = []
    for piece in rock:
        x = piece[1] + 1
        if x < 0 or x >= 7 or (piece[0], x) in frozen_rocks:
            return rock
        moved.append((piece[0], x))
    return moved

def left(frozen_rocks, rock):
    moved = []
    for piece in rock:
        x = piece[1] - 1
        if x < 0 or x >= 7 or (piece[0], x) in frozen_rocks:
            return rock
        moved.append((piece[0], x))
    return moved

def down(frozen_rocks, rock):
    moved = []
    for piece in rock:
        y = piece[0] - 1
        if y < 0 or (y, piece[1]) in frozen_rocks:
            return True, rock
        moved.append((y, piece[1]))
    return False, moved

def top_n_rows(frozen_rocks, n):
    """ Return top n rows of frozen rocks as if their y-coordinate started from 0. """
    if not frozen_rocks:
        return frozenset()

    max_y = max(frozen_rocks)[0]
    return frozenset([(max_y - r[0], r[1]) for r in frozen_rocks if max_y - r[0] < n])

seen_states = {}

rocks_dropped = 0
frozen_rocks = set()
N = 1000000000000
simulation_done = False

while rocks_dropped < N:
    next_rock = rocks_dropped % len(rocks)
    next_wind = wind % len(windpattern)

    current_state = (
        next_rock,
        next_wind,
        top_n_rows(frozen_rocks, 5)
    )

    if not simulation_done and current_state in seen_states:
        rocks_in_cycle = rocks_dropped - seen_states[current_state][0]
        height_of_cycle = max(frozen_rocks)[0] - seen_states[current_state][1]

        cycles_to_simulate = (N - rocks_dropped) // rocks_in_cycle
        rocks_simulated = rocks_in_cycle * cycles_to_simulate
        simulation_height = height_of_cycle * cycles_to_simulate

        rocks_dropped += rocks_simulated
        simulation_done = True

    if frozen_rocks:
        seen_states[current_state] = (rocks_dropped, max(frozen_rocks)[0])

    rock = rocks[next_rock]
    rock = start_pos(frozen_rocks, rock)

    while True:
        if windpattern[wind % len(windpattern)] == '>':
            rock = right(frozen_rocks, rock)
        else:
            rock = left(frozen_rocks, rock)
        wind += 1

        freeze, rock = down(frozen_rocks, rock)

        if freeze:
            frozen_rocks.update(rock)
            break

    rocks_dropped += 1

print(simulation_height + max(frozen_rocks)[0] + 1)
