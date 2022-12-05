import re

def read_stacks(lines):
    stacks = [[]]
    for stack_height, header_line in enumerate(lines):
        if '[' not in header_line:
            break
    for col, c in enumerate(header_line):
        if not c.isdigit():
            continue
        stack = []
        for row in range(stack_height):
            if lines[row][col].isalpha():
                stack.append(lines[row][col])
        stacks.append(stack[::-1])
    return stacks

lines = [l for l in open("day5/input")]
stacks = read_stacks(lines)

for line in lines:
    if not line.startswith("move"):
        continue
    n, source, dest = [int(x) for x in re.findall("\d+", line)]
    stacks[dest] += stacks[source][-n:]
    for _ in range(n):
        stacks[source].pop()

result = ''.join([s[-1] for s in stacks[1:]])
print(result)
