nodes = set()
nonzero = set()
rates = {}
neighbours = {}

for line in open("day16/input").read().splitlines():
    words = line.split()
    node = words[1]
    rate = int(words[4][5:-1])

    nodes.add(node)
    rates[node] = rate
    neighbours[node] = [s.removesuffix(',') for s in words[9:]]

    if rate > 0:
        nonzero.add(node)


# Floyd-Warshall
dist = {}
inf = 999999999
for u in nodes:
    for v in nodes:
        dist[(u, v)] = inf
for v in nodes:
    for u in neighbours[v]:
        dist[(u, v)] = 1
for v in nodes:
    dist[(v, v)] = 0
for k in nodes:
    for i in nodes:
        for j in nodes:
            dist[(i, j)] = min(dist[(i, j)], dist[(i, k)] + dist[(k, j)])


def r(v, visited, time, score):
    if time <= 0:
        return score
    score += time * rates[v]
    if len(visited) == len(nonzero):
        return score
    max_ = 0
    for u in nonzero:
        if u in visited:
            continue
        max_ = max(max_, r(u, visited + [u], time-dist[v, u] - 1, score))
    return max_

score = r('AA', [], 30, 0)
print(score)
