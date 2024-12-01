with open('2024/day1/input', 'r') as f:
    data = f.read()

list1 = [int(x) for x in data.split()[0::2]]
list2 = [int(x) for x in data.split()[1::2]]

counts = {}

for b in list2:
    if b not in counts:
        counts[b] = 1
    else:
        counts[b] += 1

part2 = 0

for a in list1:
    part2 += a * counts.get(a, 0)

print(part2)
