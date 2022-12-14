def get_neighbours(graph, node):
    neighbours = []
    x, y = node
    w, h = len(graph[0]), len(graph)

    if y-1 >= 0 and ord(graph[y-1][x]) - ord(graph[y][x]) <= 1:
        neighbours.append((x, y-1))
    if y+1 < h and ord(graph[y+1][x]) - ord(graph[y][x]) <= 1:
        neighbours.append((x, y+1))
    if x-1 >= 0 and ord(graph[y][x-1]) - ord(graph[y][x]) <= 1:
        neighbours.append((x-1, y))
    if x+1 < w and ord(graph[y][x+1]) - ord(graph[y][x]) <= 1:
        neighbours.append((x+1, y))

    return neighbours

def to_path(parents, node):
    path = [node]
    while parents[node]:
        node = parents[node]
        path.append(node)
    return path[::-1]

def bfs(graph, start, end):
    queue = [start]
    visited = set([start])
    parents = {start: None}

    while queue:
        node = queue.pop(0)
        if node == end:
            return to_path(parents, node)
        for neighbour in get_neighbours(graph, node):
            if neighbour not in visited:
                visited.add(neighbour)
                parents[neighbour] = node
                queue.append(neighbour)

def find_start_and_end(graph):
    for y in range(len(graph)):
        for x in range(len(graph[y])):
            if graph[y][x] == 'S':
                start = (x, y)
                graph[y][x] = 'a'
            elif graph[y][x] == 'E':
                end = (x, y)
                graph[y][x] = 'z'
    return start, end

lines = [l.strip() for l in open("day12/input")]
graph = [list(line) for line in lines]
start, end = find_start_and_end(graph)
path = bfs(graph, start, end)
print(len(path)-1)
