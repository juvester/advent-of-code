s = open("day6/input").read().strip()

for i in range(4, len(s)):
    if len(set(s[i-4:i])) == 4:
        print(i)
        break
