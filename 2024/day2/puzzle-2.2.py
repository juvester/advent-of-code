def is_safe(report: list) -> bool:
    for a, b in zip(report, report[1:]):
        if not 1 <= b-a <= 3:
            return False
    return True


part2 = 0

with open('2024/day2/input') as f:
    for line in f:
        report = [int(x) for x in line.split()]
        for i in range(len(report)):
            r = report[0:i] + report[i+1:]
            if is_safe(r) or is_safe(r[::-1]):
                part2 += 1
                break


print(part2)
