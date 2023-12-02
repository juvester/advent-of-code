PUZZLE1_MAX = {'red': 12, 'green': 13, 'blue': 14}


def parse_game(game: str) -> dict:
    id_string, set_string = game.split(': ')
    id = int(id_string.split()[1])
    game_data = {'id': id, 'cube_sets': []}
    for cube_set in set_string.split('; '):
        rgb = {'red': 0, 'green': 0, 'blue': 0}
        for cube in cube_set.split(', '):
            n, color = cube.split()
            rgb[color] = int(n)
        game_data['cube_sets'].append(rgb)
    return game_data


def puzzle1_ok(game) -> bool:
    for cube_set in game['cube_sets']:
        for color in cube_set:
            if cube_set[color] > PUZZLE1_MAX[color]:
                return False
    return True


def puzzle2_val(game) -> int:
    r = g = b = 0
    for cube_set in game['cube_sets']:
        r = max(r, cube_set['red'])
        g = max(g, cube_set['green'])
        b = max(b, cube_set['blue'])
    return r * g * b


solution1 = 0
solution2 = 0

with open("2023/day2/input") as file:
    for line in file:
        game = parse_game(line.strip())

        if puzzle1_ok(game):
            solution1 += game['id']

        solution2 += puzzle2_val(game)

print(solution1)
print(solution2)
