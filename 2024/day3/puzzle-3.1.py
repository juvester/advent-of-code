import re

with open('2024/day3/input') as f:
    input_str = f.read()

instructions = re.findall(r'mul\(\d+,\d+\)', input_str)
mul = lambda a, b: a*b
part1 = sum(map(eval, instructions))

print(part1)
