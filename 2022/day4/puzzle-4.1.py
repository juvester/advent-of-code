import re

lines = [line.strip() for line in open("day4/input")]
result = 0

for line in lines:
    a, b, c, d = [int(x) for x in re.findall("\d+", line)]

    if a <= c <= d <= b or c <= a <= b <= d :
        result += 1

print(result)
