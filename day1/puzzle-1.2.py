def calories(elf):
    return sum([int(food) for food in elf.split('\n')])

elves = open("day1/input").read().strip().split('\n\n')
top3 = sorted(map(calories, elves))[-3:]
result = sum(top3)

print(result)
