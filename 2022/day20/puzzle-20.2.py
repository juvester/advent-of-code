class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.right = None
        self.left = None

    def __str__(self) -> str:
        return str(self.value)

nodes = []
prev = None
zero = None

lines = [l.strip() for l in open("day20/input")]
for line in lines:
    node = Node(int(line) * 811589153)
    node.left = prev
    if prev:
        prev.right = node
    prev = node
    nodes.append(node)
    if node.value == 0:
        zero = node

nodes[0].left = nodes[-1]
nodes[-1].right = nodes[0]

for j in range(10):
    for N in nodes:
        L = N.left
        R = N.right

        L.right = R
        R.left = L

        for i in range(N.value % (len(nodes) - 1)):
            L = L.right
            R = R.right

        L.right = N
        R.left = N
        N.left = L
        N.right = R

def nth_from(node, n):
    for _ in range(n):
        node = node.right
    return node

a = nth_from(zero, 1000)
b = nth_from(zero, 2000)
c = nth_from(zero, 3000)

print(a.value + b.value + c.value)
