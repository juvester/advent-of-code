instructions = [line.strip() for line in open("day10/input")]

register_x = 1
cycle = 1
cpu_time = 0
addx = False
result = 0

while instructions:
    if cpu_time == 0:
        if addx:
            register_x += v
            addx = False

        instruction = instructions.pop(0)

        if instruction == 'noop':
            cpu_time = 1
        else:
            v = int(instruction[5:])
            cpu_time = 2
            addx = True

    if cycle % 40 == 20:
        result += cycle * register_x

    cpu_time -= 1
    cycle += 1

print(result)
