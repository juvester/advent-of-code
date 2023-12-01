def scenic_score(trees: list[list[int]], row: int, col: int) -> int:
    left, right, top, bottom = 0, 0, 0, 0
    for j in range(col-1, -1, -1):
        left += 1
        if trees[row][j] >= trees[row][col]:
            break
    for j in range(col+1, len(trees[row])):
        right += 1
        if trees[row][j] >= trees[row][col]:
            break
    for i in range(row-1, -1, -1):
        top += 1
        if trees[i][col] >= trees[row][col]:
            break
    for i in range(row+1, len(trees)):
        bottom += 1
        if trees[i][col] >= trees[row][col]:
            break
    return left * right * top * bottom

lines = [line.strip() for line in open("day8/input")]
trees = list(map(lambda line: [int(c) for c in line], lines))
scores = []

for row in range(len(trees)):
    scores.append([])
    for col in range(len(trees[row])):
        scores[-1].append(scenic_score(trees, row, col))

highest_score = 0
for row in scores:
    for score in row:
        highest_score = max(highest_score, score)
print(highest_score)
