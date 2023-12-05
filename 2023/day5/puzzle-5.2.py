with open("2023/day5/input") as file:
    sections = file.read().split('\n\n')

seeds = set()

seed_data = [int(x) for x in sections[0].split(': ')[1].split()]
for i in range(0, len(seed_data), 2):
    seeds.add((seed_data[i], seed_data[i] + seed_data[i+1] - 1))

for section in sections[1:]:
    map_rules = []

    for row in section.splitlines()[1:]:
        dest, source, range_ = [int(x) for x in row.split()]
        map_rules.append((dest, source, source + range_ - 1))

    mapped_seeds = set()

    while seeds:
        seed_start, seed_end = seeds.pop()
        for map_destination, map_start, map_end in map_rules:
            if not map_start <= seed_start <= map_end:
                continue
            mapped_seed_start = map_destination + (seed_start - map_start)
            if seed_end <= map_end:
                mapped_seed_end = map_destination + (seed_end - map_start)
            else:
                mapped_seed_end = map_destination + (map_end - map_start)
                leftover_start = map_end + 1
                leftover_end = seed_end
                seeds.add((leftover_start, leftover_end))
            mapped_seeds.add((mapped_seed_start, mapped_seed_end))
            break
        else:
            mapped_seeds.add((seed_start, seed_end))

    seeds = mapped_seeds

print(min(seeds)[0])
