def priority(char):
    if char.islower():
        return ord(char) - ord('a') + 1
    else:
        return ord(char) - ord('A') + 27

rucksacks = [line.strip() for line in open("day3/input")]
result = 0

for i in range(0, len(rucksacks), 3):
    s1 = set(rucksacks[i])
    s2 = set(rucksacks[i + 1])
    s3 = set(rucksacks[i + 2])

    common = s1.intersection(s2).intersection(s3).pop()
    result += priority(common)

print(result)
