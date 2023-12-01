lines = [l.strip() for l in open("day7/input")]

curr_path = []
dir_sizes = {}

for line in lines:
    cmd = line.split()
    if cmd[0] == '$' and cmd[1] == 'cd':
        if cmd[2] == '..':
            curr_path.pop()
        else:
            curr_path.append(cmd[2])
    elif cmd[0].isdigit():
        for depth in range(len(curr_path)):
            path = ''.join(curr_path[:depth+1])
            dir_sizes[path] = dir_sizes.get(path, 0) + int(cmd[0])

req_space = 30000000 - (70000000 - dir_sizes['/'])
result = min([size for size in dir_sizes.values() if size >= req_space])
print(result)
