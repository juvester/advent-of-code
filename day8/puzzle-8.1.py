def is_visble(trees: list[list[int]], row: int, col: int) -> bool:
    left, right, top, bottom = True, True, True, True
    for j in range(col-1, -1, -1):
        if trees[row][j] >= trees[row][col]:
            left = False
            break
    for j in range(col+1, len(trees[row])):
        if trees[row][j] >= trees[row][col]:
            right = False
            break
    for i in range(row-1, -1, -1):
        if trees[i][col] >= trees[row][col]:
            top = False
            break
    for i in range(row+1, len(trees)):
        if trees[i][col] >= trees[row][col]:
            bottom = False
            break
    return left or right or top or bottom

lines = [line.strip() for line in open("day8/input")]
trees = list(map(lambda line: [int(c) for c in line], lines))
result = len(trees[0])*2 + len(trees)*2 - 4

for row in range(1, len(trees)-1):
    for col in range(1, len(trees[row])-1):
        if is_visble(trees, row, col):
            result += 1

print(result)
