from functools import cmp_to_key

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

divider1 = [[2]]
divider2 = [[6]]

packets = [eval(p) for p in open("day13/input").read().split()]
packets.append(divider1)
packets.append(divider2)

packets.sort(key=cmp_to_key(order))

i = packets.index(divider1) + 1
j = packets.index(divider2) + 1

print(i * j)
