with open('2024/day1/input', 'r') as f:
    data = f.read()

list1 = [int(x) for x in data.split()[0::2]]
list2 = [int(x) for x in data.split()[1::2]]

list1.sort()
list2.sort()

part1 = sum([abs(a-b) for a, b in zip(list1, list2)])

print(part1)
