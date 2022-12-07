class Dir:
    def __init__(self, name, parent) -> None:
        self.name = name
        self.parent = parent
        self.children = {}
        self.files = {}

    def size(self) -> int:
        size = sum(self.files.values())
        for child in self.children.values():
            size += child.size()
        return size

def print_tree(dir: Dir, level: int) -> None:
    if not dir:
        return
    print(f"{' '*2*level}+ {dir.name} (dir)")
    for child in dir.children.values():
        print_tree(child, level+1)
    for file, size in dir.files.items():
        print(f"{' '*2*(level+1)}- {file} (file, size={size})")

def puzzle1(dir: Dir) -> int:
    solution = 0
    for child in dir.children.values():
        solution += puzzle1(child)
    size = dir.size()
    if size <= 100000:
        solution += size
    return solution

lines = [l.strip() for l in open("day7/input")]

root = Dir('/', None)
dir = root

for line in lines:
    word = line.split()

    if word[0] == '$':
        if word[1] == 'cd':
            if word[2] == '/':
                dir = root
            elif word[2] == '..':
                dir = dir.parent
            else:
                dir = dir.children[word[2]]
        elif word[1] == 'ls':
            continue
    elif word[0] == 'dir':
        if word[1] not in dir.children:
            dir.children[word[1]] = Dir(word[1], dir)
    elif word[0].isdigit():
        if word[1] not in dir.files:
            dir.files[word[1]] = int(word[0])

#print_tree(root, 0)
print(puzzle1(root))
