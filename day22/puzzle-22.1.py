def show(board):
    for row in board:
        print(''.join(row).replace(' ', '='))
    print()

def next_square(board, y, x, dy, dx):
    if y + dy < 0:
        return next_square(board, len(board), x, dy, dx)
    elif y + dy >= len(board):
        return next_square(board, -1, x, dy, dx)
    elif x + dx < 0:
        return next_square(board, y, len(board[y]), dy, dx)
    elif x + dx >= len(board[0]):
        return next_square(board, y, -1, dy, dx)
    elif board[y + dy][x + dx] == ' ':
        return next_square(board, y+dy, x+dx, dy, dx)
    else:
        return y+dy, x+dx

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
    delta = deltas[d]

    while steps:
        board[y][x] = delta[2]

        next_y, next_x = next_square(board, y, x, delta[0], delta[1])

        if board[next_y][next_x] == '#':
            break

        y = next_y
        x = next_x

        steps -= 1

y += 1
x += 1

print(1000*y + 4*x + d)
