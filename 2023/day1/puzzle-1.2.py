def parseCalibrationValue(s: str) -> str:
    digits = {
        'one':   1,
        'two':   2,
        'three': 3,
        'four':  4,
        'five':  5,
        'six':   6,
        'seven': 7,
        'eight': 8,
        'nine':  9,
    }

    # Also add {'1': 1, '2': 2, ...} to digits
    digits.update({str(val): val for val in digits.values()})

    first_index = len(s)
    last_index = -1

    for digit in digits:
        i = s.find(digit)
        if i != -1 and i < first_index:
            first_index = i
            first_digit = digits[digit]

        j = s.rfind(digit)
        if j != -1 and j > last_index:
            last_index = j
            last_digit = digits[digit]

    return first_digit * 10 + last_digit


total = 0

with open("2023/day1/input") as file:
    for line in file:
        total += parseCalibrationValue(line)

print(total)
