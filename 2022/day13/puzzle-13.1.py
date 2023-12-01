def order(left, right):
    if type(left) is int and type(right) is int:
        return left - right
    elif type(left) is list and type(right) is list:
        for pair in list(zip(left, right)):
            diff = order(pair[0], pair[1])
            if diff != 0:
                return diff
        return len(left) - len(right)
    else:
        if type(left) is int:
            return order([left], right)
        return order(left, [right])

pairs = open("day13/input").read().split('\n\n')
result = 0

for i, pair in enumerate(pairs, 1):
    pair = pair.split('\n')
    left = eval(pair[0])
    right = eval(pair[1])
    if order(left, right) <= 0:
        result += i

print(result)
