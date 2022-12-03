def priority(char):
    if char.islower():
        return ord(char) - ord('a') + 1
    else:
        return ord(char) - ord('A') + 27

rucksacks = [line.strip() for line in open("day3/input")]
result = 0

for sack in rucksacks:
    mid = len(sack) // 2
    left = set(sack[:mid])
    right  = set(sack[mid:])
    common = left.intersection(right).pop()
    result += priority(common)

print(result)
