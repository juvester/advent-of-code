lines = [l.strip() for l in open("day21/input")]

tree = {}

for line in lines:
    words = line.split(': ')
    tree[words[0]] = words[1]

def solve(tree, node):
    words = tree[node].split()

    if len(words) == 1:
        return int(words[0])

    left = words[0]
    operation = words[1]
    right = words[2]

    return int(eval(f"{solve(tree, left)} {operation} {solve(tree, right)}"))

result = solve(tree, 'root')

print(result)
