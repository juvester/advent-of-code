valves = set()
nonzero = set()
rates = {}
tunnels = {}

for line in open("day16/input").read().splitlines():
    words = line.split()
    valve = words[1]
    rate = int(words[4][5:-1])

    valves.add(valve)
    rates[valve] = rate
    tunnels[valve] = [s.removesuffix(',') for s in words[9:]]

    if rate > 0:
        nonzero.add(valve)


# Floyd-Warshall
dist = {}
inf = 999999999
for u in valves:
    for v in valves:
        dist[(u, v)] = inf
for v in valves:
    for u in tunnels[v]:
        dist[(u, v)] = 1
for v in valves:
    dist[(v, v)] = 0
for k in valves:
    for i in valves:
        for j in valves:
            dist[(i, j)] = min(dist[(i, j)], dist[(i, k)] + dist[(k, j)])


def traverse(v, time, visited, score, cache):
    cache[visited] = max(cache.get(visited, 0), score)
    for u in nonzero:
        newtime = time - dist[(v, u)] - 1
        if u in visited or newtime <= 0:
            continue
        newvisited = tuple(sorted(visited + (u,)))
        newscore = score + rates[u] * newtime
        traverse(u, newtime, newvisited, newscore, cache)
    return cache

cache = traverse('AA', 26, tuple(), 0, {})

result = 0
for k1, v1 in cache.items():
    for k2, v2 in cache.items():
        if len(set(k1).intersection(set(k2))) == 0:
            result = max(result, v1 + v2)

print(result)
