import re

def load_game_data(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()


def extract_sets_from_line(line):
    return line.split(';')


def parse_set(set_text):
    pattern_colors = r'(\d*)\s(red|blue|green)'
    matches = re.finditer(pattern_colors, set_text)
    return [(int(match.group(1)), match.group(2)) for match in matches]


def is_game_valid(sets, max_colors):
    for set_text in sets:
        cubes = parse_set(set_text)
        for quantity, color in cubes:
            if quantity > max_colors[color]:
                return False
    return True


def calculate_valid_games_sum(game_data, max_colors):
    pattern_prefix = r'Game \d*:'
    valid_games_sum = 0

    for i, line in enumerate(game_data):
        line = re.sub(pattern_prefix, '', line)
        sets = extract_sets_from_line(line)

        if is_game_valid(sets, max_colors):
            valid_games_sum += i + 1

    return valid_games_sum


if __name__ == "__main__":
    file_path = './2/example.txt'
    # file_path = 'input.txt'

    game_data = load_game_data(file_path)

    max_colors = {'red': 12, 'green': 13, 'blue': 14}
    result = calculate_valid_games_sum(game_data, max_colors)

    print(result)
