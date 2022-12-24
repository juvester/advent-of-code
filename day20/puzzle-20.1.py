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
    node = Node(int(line))
    node.left = prev
    if prev:
        prev.right = node
    prev = node
    nodes.append(node)
    if node.value == 0:
        zero = node

nodes[0].left = nodes[-1]
nodes[-1].right = nodes[0]

for N in nodes:
    for i in range(abs(N.value)):
        if N.value > 0:
            # L N R RR
            # L R N RR
            L = N.left
            R = N.right
            RR = R.right

            L.right = R
            R.left = L
            R.right = N
            N.left = R
            N.right = RR
            RR.left = N
        else:
            # LL L N R
            # LL N L R
            R = N.right
            L = N.left
            LL = L.left

            R.left = L
            L.right = R
            L.left = N
            N.right = L
            N.left = LL
            LL.right = N

def nth_from(node, n):
    for _ in range(n):
        node = node.right
    return node

a = nth_from(zero, 1000)
b = nth_from(zero, 2000)
c = nth_from(zero, 3000)

print(a.value + b.value + c.value)
