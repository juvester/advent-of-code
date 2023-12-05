with open("2023/day5/input") as file:
    sections = file.read().split('\n\n')

seeds = [int(x) for x in sections[0].split()[1:]]

maps = []

for section in sections[1:]:
    map_ = []

    for row in section.splitlines()[1:]:
        dest, source, range_ = [int(x) for x in row.split()]
        map_.append((dest, source, range_))

    mapped_seeds = []

    for seed in seeds:
        for map_row in map_:
            if seed in range(map_row[1], map_row[1] + map_row[2]):
                mapped_seeds.append(map_row[0] + (seed-map_row[1]))
                break
        else:
            mapped_seeds.append(seed)

    seeds = mapped_seeds

print(min(mapped_seeds))
