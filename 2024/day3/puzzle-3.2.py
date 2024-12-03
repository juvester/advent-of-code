import re

with open('2024/day3/input') as f:
    input_str = f.read()

instructions = re.findall(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)', input_str)
mul = lambda a, b: a*b
do = True
part2 = 0

for instruction in instructions:
    if instruction == 'do()':
        do = True
    elif instruction == "don't()":
        do = False
    elif do:
        part2 += eval(instruction)

print(part2)
