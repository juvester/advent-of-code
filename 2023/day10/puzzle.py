from collections import deque


def find_start(grid) -> tuple:
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                return (i, j)


def draw3x(G, i, j, ch):
    i = i*3+1
    j = j*3+1

    pipe = '█'
    match ch:
        case '|':
            G[i-1][j] = pipe
            G[i+0][j] = pipe
            G[i+1][j] = pipe
        case '-':
            G[i][j-1] = pipe
            G[i][j+0] = pipe
            G[i][j+1] = pipe
        case 'F':
            G[i][j] = pipe
            G[i+1][j] = pipe
            G[i][j+1] = pipe
        case '7':
            G[i][j] = pipe
            G[i][j-1] = pipe
            G[i+1][j] = pipe
        case 'L':
            G[i][j] = pipe
            G[i-1][j] = pipe
            G[i][j+1] = pipe
        case 'J':
            G[i][j] = pipe
            G[i-1][j] = pipe
            G[i][j-1] = pipe


with open("2023/day10/input") as file:
    grid = [list(line.strip()) for line in file]

grid3x = [[' ']*(3*len(grid[0])) for i in range(3*len(grid))]

i, j = find_start(grid)
delta_i = delta_j = 0

if i-1 >= 0 and grid[i-1][j] in '|F7':
    delta_i = -1
elif i+1 < len(grid) and grid[i+1][j] in '|JL':
    delta_i = 1
elif j-1 >= 0 and grid[i][j-1] in '-FL':
    delta_j = -1
elif j+1 < len(grid[i]) and grid[i][j+1] in '-7J':
    delta_j = 1

# S is F in my input
draw3x(grid3x, i, j, 'F')

i += delta_i
j += delta_j
part1 = 1

while grid[i][j] != 'S':
    draw3x(grid3x, i, j, grid[i][j])

    if grid[i][j] in '7L':
        delta_i, delta_j = delta_j, delta_i
    elif grid[i][j] in 'JF':
        delta_i, delta_j = -delta_j, -delta_i

    i += delta_i
    j += delta_j

    part1 += 1

print(part1//2)

"""
 1  procedure BFS(G, root) is
 2      let Q be a queue
 3      label root as explored
 4      Q.enqueue(root)
 5      while Q is not empty do
 6          v := Q.dequeue()
 7          if v is the goal then
 8              return v
 9          for all edges from v to w in G.adjacentEdges(v) do
10              if w is not labeled as explored then
11                  label w as explored
12                  w.parent := v
13                  Q.enqueue(w)
"""


def bfs(grid3x, grid, i, j):
    q = deque()
    visited = set()

    visited.add((i, j))
    grid3x[i][j] = 'X'
    grid[i//3][j//3] = 'X'

    q.append((i, j))
    while q:
        vi, vj = q.popleft()
        for ii, jj in [(vi-1, vj), (vi+1, vj), (vi, vj-1), (vi, vj+1)]:
            if ii < 0 or ii >= len(grid3x) or jj < 0 or jj >= len(grid3x[ii]):
                continue
            if grid3x[ii][jj] == '█':
                grid[ii//3][jj//3] = ' '
                continue
            if grid3x[ii][jj] != ' ':
                continue
            if (ii, jj) not in visited:
                grid3x[ii][jj] = 'X'
                grid[ii//3][jj//3] = ' '
                visited.add((ii, jj))
                q.append((ii, jj))


bfs(grid3x, grid, 0, 0)

part2 = 0
for line in grid:
    part2 += len(line) - line.count(' ')

print(part2)
