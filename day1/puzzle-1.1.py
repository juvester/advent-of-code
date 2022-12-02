with open("day1/input") as file:
    print(max([sum([int(cal) for cal in elf.split('\n')]) for elf in file.read().strip().split('\n\n')]))
