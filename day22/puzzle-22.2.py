def show(board):
    for row in board:
        print(''.join(row).replace(' ', '='))
    print()

def next_square(board, y, x, dy, dx, d):
    w = len(board[0])
    h = len(board)

    if y + dy < 0:
        if x < 50:
            return next_square(board, 50 + x, 49, 0, 1, 0)
        elif x < 100:
            return next_square(board, 150 + (x - 50), -1, 0, 1, 0)
        elif x < 150:
            return next_square(board, h, x - 100, -1, 0, 3)
        else:
            assert False

    elif y + dy >= h:
        if x < 50:
            return next_square(board, -1, 100 + x, 1, 0, 1)
        elif x < 100:
            return next_square(board, 150 + (x - 50), 50, 0, -1, 2)
        elif x < 150:
            return next_square(board, 50 + (x - 100), 100, 0, -1, 2)
        else:
            assert False

    elif x + dx < 0:
        if y < 50:
            return next_square(board, 149 - y, -1, 0, 1, 0)
        elif y < 100:
            return next_square(board, 99, y - 50, 1, 0, 1)
        elif y < 150:
            return next_square(board, 49 - (y - 100), -1, 0, 1, 0)
        elif y < 200:
            return next_square(board, -1, 50 + (y - 150), 1, 0, 1)
        else:
            assert False

    elif x + dx >= w:
        if y < 50:
            return next_square(board, 149 - y, 100, 0, -1, 2)
        elif y < 100:
            return next_square(board, 50, 100 + (y - 50), -1, 0, 3)
        elif y < 150:
            return next_square(board, 49 - (y - 100), 150, 0, -1, 2)
        elif y < 200:
            return next_square(board, 150, 50 + (y - 150), -1, 0, 3)
        else:
            assert False

    elif board[y + dy][x + dx] == ' ':
        return next_square(board, y + dy, x + dx, dy, dx, d)

    else:
        return (y + dy, x + dx, d)

lines = [l.removesuffix('\n') for l in open("day22/input")]

w = max([len(l) for l in lines[:-2]])
h = len(lines) - 2

path = [(s[0], int(s[1:])) for s in ('R' + lines[-1]).replace('R', ' R').replace('L', ' L').split()]
board = [[c for c in line + ' ' * (w - len(line))] for line in lines[:-2]]

x = board[0].index('.')
y = 0

deltas = [(0, 1, '>'), (1, 0, 'v'), (0, -1, '<'), (-1, 0, '^')]
d = 3

for turn, steps in path:
    if turn == 'L':
        d = (d - 1) % len(deltas)
    else:
        d = (d + 1) % len(deltas)

    while steps:
        delta = deltas[d]
        board[y][x] = delta[2]

        next_y, next_x, next_d = next_square(board, y, x, delta[0], delta[1], d)

        if board[next_y][next_x] == '#':
            break

        y = next_y
        x = next_x
        d = next_d

        steps -= 1

    #show(board)

y += 1
x += 1

print(1000 * y + 4 * x + d)
