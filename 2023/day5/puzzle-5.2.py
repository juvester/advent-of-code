with open("2023/day5/input") as file:
    sections = file.read().split('\n\n')

seed_ranges = set()

seed_data = [int(x) for x in sections[0].split(': ')[1].split()]
for i in range(0, len(seed_data), 2):
    seed_ranges.add((seed_data[i], seed_data[i] + seed_data[i+1] - 1))

for section in sections[1:]:
    map_rules = []

    for row in section.splitlines()[1:]:
        dest, source, range_ = [int(x) for x in row.split()]
        map_rules.append((dest, source, source + range_ - 1))

    mapped_seeds = set()

    while seed_ranges:
        seed_range = seed_ranges.pop()
        for map_rule in map_rules:
            if map_rule[1] <= seed_range[0] <= map_rule[2]:
                mapped_seed_start = map_rule[0] + (seed_range[0]-map_rule[1])
                if seed_range[1] <= map_rule[2]:
                    mapped_seed_end = map_rule[0] + (seed_range[1]-map_rule[1])
                else:
                    mapped_seed_end = map_rule[0] + (map_rule[2]-map_rule[1])
                    leftover_start = map_rule[2]+1
                    leftover_end = seed_range[1]
                    seed_ranges.add((leftover_start, leftover_end))
                mapped_seeds.add((mapped_seed_start, mapped_seed_end))
                break
        else:
            mapped_seeds.add(seed_range)
    seed_ranges = mapped_seeds

print(min(seed_ranges)[0])
