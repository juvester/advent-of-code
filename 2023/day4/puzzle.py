with open('2023/day4/input') as file:
    lines = file.read().splitlines()

part1 = 0
part2 = 0

card_count = [1] * len(lines)

for i, line in enumerate(lines):
    numbers = line.split(': ')[1].split(' | ')

    winning_numbers = set(map(int, numbers[0].split()))
    player_numbers = set(map(int, numbers[1].split()))

    matches = len(player_numbers.intersection(winning_numbers))

    if matches > 0:
        part1 += 2**(matches-1)

    for j in range(1, matches+1):
        card_count[i+j] += card_count[i]

    part2 += card_count[i]

print(part1)
print(part2)
