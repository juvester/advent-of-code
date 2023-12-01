total = 0

with open("2023/day1/input") as file:
    for line in file:
        digits = [int(ch) for ch in line if ch.isdigit()]
        calibrationValue = digits[0]*10 + digits[-1]
        total += calibrationValue

print(total)
