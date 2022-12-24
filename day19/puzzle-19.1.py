import re

blueprints = []

for blueprint in [l.strip() for l in open("day19/input")]:
    bp = [int(x) for x in re.findall('\d+', blueprint)]
    max_ore = max(bp[1], bp[2], bp[3], bp[5])
    blueprints.append(tuple(bp + [max_ore]))

def r(bp, time, a, b, c, d, A, B, C, D):

    # never have more than double than needed
    a = min(a, bp[7]*2)
    b = min(b, bp[4]*2)
    c = min(c, bp[6]*2)

    key = (time, a, b, c, d, A, B, C, D)
    if key in cache:
        return cache[key]


    if time == 0:
        return d

    v = 0

    if a >= bp[5] and c >= bp[6]:
        # make geode robot
        v = max(v, r(bp, time-1, a-bp[5]+A, b+B, c-bp[6]+C, d+D, A, B, C, D+1))
    else:
        if a >= bp[3] and b >= bp[4] and C < bp[6]:
            # make obsidian robot
            v = max(v, r(bp, time-1, a-bp[3]+A, b-bp[4]+B, c+C, d+D, A, B, C+1, D))
        if a >= bp[2] and B < bp[4]:
            # make clay robot
            v = max(v, r(bp, time-1, a-bp[2]+A, b+B, c+C, d+D, A, B+1, C, D))
        if a >= bp[1] and A < bp[7]:
            # make ore robot
            v = max(v, r(bp, time-1, a-bp[1]+A, b+B, c+C, d+D, A+1, B, C, D))
        # just mine
        v = max(v, r(bp, time-1, a+A, b+B, c+C, d+D, A, B, C, D))

    cache[key] = v
    return v

result = 0
for bp in blueprints:
    cache = {}

    geodes = r(
        bp, 24,
        0, 0, 0, 0,
        1, 0, 0, 0
    )

    print(bp[0], geodes)
    result += bp[0] * geodes

print(result)
