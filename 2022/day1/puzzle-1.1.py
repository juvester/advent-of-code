def calories(elf):
    return sum([int(food) for food in elf.split('\n')])

elves = open("day1/input").read().strip().split('\n\n')
result = max(map(calories, elves))

print(result)
