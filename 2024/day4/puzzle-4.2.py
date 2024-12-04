with open('2024/day4/input') as f:
    arr = [line.strip() for line in f]

h = len(arr)
w = len(arr[0])
needles = ['MAS', 'SAM']
part2 = 0

for i in range(1, h-1):
    for j in range(1, w-1):
        if arr[i][j] != 'A':
            continue
        diag1 = arr[i-1][j-1] + arr[i][j] + arr[i+1][j+1]
        diag2 = arr[i-1][j+1] + arr[i][j] + arr[i+1][j-1]
        if diag1 in needles and diag2 in needles:
            part2 += 1

print(part2)
