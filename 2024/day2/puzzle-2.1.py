def is_safe(report: list) -> bool:
    for a, b in zip(report, report[1:]):
        if not 1 <= b-a <= 3:
            return False
    return True


part1 = 0

with open('2024/day2/input') as f:
    for line in f:
        report = [int(x) for x in line.split()]
        if is_safe(report) or is_safe(report[::-1]):
            part1 += 1

print(part1)
