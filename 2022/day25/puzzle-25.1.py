def to_decimal(snafu):
    place = 1
    decimal = 0
    for c in snafu[::-1]:
        decimal += ('=-012'.index(c) - 2) * place
        place *= 5
    return decimal

def to_snafu(decimal):
    snafu = ''
    fives = decimal
    while fives:
        ones = fives % 5
        fives //= 5
        if ones > 2:
            fives += 1
        snafu = '012=-'[ones] + snafu
    return snafu

lines = [l.strip() for l in open("day25/input")]
total = 0

for line in lines:
    total += to_decimal(line)

snafu = to_snafu(total)
print(snafu)
