instructions = [line.strip() for line in open("day10/input")]

register_x = 1
cycle = 0
cpu_time = 0
addx = False

crt = ''
crt_c = 0

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

    if cycle % 40 == 0:
        crt_c = 0
        crt += '\n'
        pass

    if register_x-1 <= crt_c <= register_x+1:
        crt += '#'
    else:
        crt += '.'

    cpu_time -= 1
    cycle += 1
    crt_c +=1

print(crt)
