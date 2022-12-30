def to_expression(tree, node):
    words = tree[node].split()

    if len(words) == 1:
        return words[0]

    left = words[0]
    operation = words[1]
    right = words[2]

    return f"({to_expression(tree, left)} {operation} {to_expression(tree, right)})"

lines = [l.strip() for l in open("day21/input")]

tree = {}

for line in lines:
    words = line.split(': ')
    tree[words[0]] = words[1]

root = tree['root']
root_operation = root.split()[1]
tree['root'] = root.replace(root_operation, '-')
tree['humn'] = '1j'

# https://towardsdatascience.com/the-most-efficient-way-to-solve-any-linear-equation-in-three-lines-of-code-bb8f66f1b463
expression = to_expression(tree, 'root')
grouped = eval(expression)
x = round(-grouped.real / grouped.imag)

print(x)
