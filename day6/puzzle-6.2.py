s = open("day6/input").read().strip()

for i in range(14, len(s)):
    if len(set(s[i-14:i])) == 14:
        print(i)
        break
