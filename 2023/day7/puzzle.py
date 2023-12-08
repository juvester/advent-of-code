def five_of_a_kind(hand: str) -> bool:
    return len(set(hand)) == 1


def four_of_a_kind(hand: str) -> bool:
    h = sorted(hand)
    return h[0] == h[1] == h[2] == h[3] or h[1] == h[2] == h[3] == h[4]


def full_house(hand: str) -> bool:
    h = sorted(hand)
    return (h[0] == h[1] == h[2] and h[3] == h[4]) or (h[0] == h[1] and h[2] == h[3] == h[4])


def three_of_a_kind(hand: str) -> bool:
    h = sorted(hand)
    return (h[0] == h[1] == h[2]) or (h[1] == h[2] == h[3]) or (h[2] == h[3] == h[4])


def two_pair(hand: str) -> bool:
    return len(set(hand)) == 3


def one_pair(hand: str) -> bool:
    return len(set(hand)) == 4


def high_card(hand: str) -> bool:
    return len(set(hand)) == 5


def strength(hand: str) -> tuple:
    card_strength = tuple(["  23456789TJQKA".index(ch) for ch in hand])

    if five_of_a_kind(hand):
        return (6, ) + card_strength
    elif (four_of_a_kind(hand)):
        return (5, ) + card_strength
    elif (full_house(hand)):
        return (4, ) + card_strength
    elif (three_of_a_kind(hand)):
        return (3, ) + card_strength
    elif (two_pair(hand)):
        return (2, ) + card_strength
    elif (one_pair(hand)):
        return (1, ) + card_strength
    elif (high_card):
        return (0, ) + card_strength
    else:
        raise Exception


def joker_stregth(hand: str) -> tuple:
    card_strength = tuple([" J23456789T QKA".index(ch) for ch in hand])

    if 'J' in hand:
        max_strength = (0, 0, 0, 0, 0, 0)
        for ch in '23456789TQKA':
            st = joker_stregth(hand.replace('J', ch, 1))
            max_strength = max(st, max_strength)
        return (max_strength[0], ) + card_strength
    else:
        if five_of_a_kind(hand):
            return (6, ) + card_strength
        elif (four_of_a_kind(hand)):
            return (5, ) + card_strength
        elif (full_house(hand)):
            return (4, ) + card_strength
        elif (three_of_a_kind(hand)):
            return (3, ) + card_strength
        elif (two_pair(hand)):
            return (2, ) + card_strength
        elif (one_pair(hand)):
            return (1, ) + card_strength
        elif (high_card):
            return (0, ) + card_strength
        else:
            raise Exception


with open('2023/day7/input') as file:
    hands = []
    for line in file:
        hand, bid = line.split()
        hands.append((hand, int(bid)))

hands1 = sorted(hands, key=lambda h: strength(h[0]))
part1 = 0
for i, hand in enumerate(hands1, 1):
    part1 += hand[1] * i
print(part1)

hands2 = sorted(hands, key=lambda h: joker_stregth(h[0]))
part2 = 0
for i, hand in enumerate(hands2, 1):
    part2 += hand[1] * i
print(part2)
