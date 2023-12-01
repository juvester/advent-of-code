def move(rope, knot, delta):
    rope[knot] = (rope[knot][0]+delta[0], rope[knot][1]+delta[1])

    if knot == len(rope)-1:
        return

    h_dist = abs(rope[knot][0] - rope[knot+1][0])
    v_dist = abs(rope[knot][1] - rope[knot+1][1])

    if h_dist <= 1 and v_dist <= 1:
        return

    dx = 0 if h_dist == 0 else 1 if rope[knot][0] > rope[knot+1][0] else -1
    dy = 0 if v_dist == 0 else 1 if rope[knot][1] > rope[knot+1][1] else -1

    move(rope, knot+1, (dx, dy))

rope1 = [(0, 0) for _ in range(2)]
rope2 = [(0, 0) for _ in range(10)]
visited1 = set([rope1[-1]])
visited2 = set([rope2[-1]])

for line in open("day9/input").read().splitlines():
    steps = int(line[2:])
    direction = line[0]

    match direction:
        case 'R': delta = (1, 0)
        case 'L': delta = (-1, 0)
        case 'U': delta = (0, 1)
        case 'D': delta = (0, -1)

    for _ in range(steps):
        move(rope1, 0, delta)
        move(rope2, 0, delta)
        visited1.add(rope1[-1])
        visited2.add(rope2[-1])

#print(len(visited1))
print(len(visited2))
