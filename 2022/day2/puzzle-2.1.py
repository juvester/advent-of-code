points = {
    'X': {'A':1+3, 'B':1+0, 'C':1+6},
    'Y': {'A':2+6, 'B':2+3, 'C':2+0},
    'Z': {'A':3+0, 'B':3+6, 'C':3+3}
}

result = 0

with open("day2/input") as file:
    for line in file:
        opponent, hero = line.rstrip().split()
        result += points[hero][opponent]

print(result)
