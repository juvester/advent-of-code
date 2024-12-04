with open('2024/day4/input') as f:
    arr = [line.strip() for line in f]

h = len(arr)
w = len(arr[0])
needles = ['XMAS', 'SAMX']
part1 = 0

for i in range(h):
    for j in range(w):
        if i <= h-4:
            ver = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+3][j]
            if ver in needles:
                part1 += 1
        if j <= w-4:
            hor = arr[i][j:j+4]
            if hor in needles:
                part1 += 1
        if i <= h-4 and j <= w-4:
            diag1 = arr[i][j] + arr[i+1][j+1] + arr[i+2][j+2] + arr[i+3][j+3]
            if diag1 in needles:
                part1 += 1
        if i <= h-4 and j >= 3:
            diag2 = arr[i][j] + arr[i+1][j-1] + arr[i+2][j-2] + arr[i+3][j-3]
            if diag2 in needles:
                part1 += 1

print(part1)
