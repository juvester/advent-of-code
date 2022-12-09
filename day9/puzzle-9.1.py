lines = open("day9/input").read().splitlines()
moves = [(l[0], int(l[2:])) for l in lines]

head = [0, 0]
tail = [0, 0]
visited = set([tuple(tail)])

for m in moves:
    match m[0]:
        case 'R': head[0] += m[1]
        case 'L': head[0] -= m[1]
        case 'U': head[1] += m[1]
        case 'D': head[1] -= m[1]

    while abs(head[0] - tail[0]) > 1:
        tail[0] += 1 if head[0] > tail[0] else -1
        tail[1] = head[1]
        visited.add(tuple(tail))

    while abs(head[1] - tail[1]) > 1:
        tail[1] += 1 if head[1] > tail[1] else -1
        tail[0] = head[0]
        visited.add(tuple(tail))

print(len(visited))
