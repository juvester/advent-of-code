def r(numbers: list) -> int:
    if all([x == 0 for x in numbers]):
        return (0, 0)

    differences = [b - a for a, b in zip(numbers[:-1], numbers[1:])]
    left, right = r(differences)

    return (numbers[0] - left, numbers[-1] + right)


with open('2023/day9/input') as file:
    lines = file.read().splitlines()

part1 = 0
part2 = 0

for line in lines:
    numbers = [int(x) for x in line.split()]
    left, right = r(numbers)
    part1 += right
    part2 += left

print(part1)
print(part2)
