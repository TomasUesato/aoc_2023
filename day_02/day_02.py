MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


def is_game_set_valid(game_set):
    for subset in game_set:
        if not is_subset_valid(subset):
            return False
    return True


def is_subset_valid(subset):
    cubes = subset.split(",")
    for cube in cubes:
        number, color = cube.split()
        number = int(number)

        if color == "green" and MAX_GREEN < number:
            return False
        if color == "red" and MAX_RED < number:
            return False
        if color == "blue" and MAX_BLUE < number:
            return False
    return True


def main():
    total_sum = 0
    with open('input.txt', 'r') as file:
        for line in file:
            game, sets = line.split(":")
            game_index = int(game.split()[1])
            game_set = sets.split(";")

            if not is_game_set_valid(game_set):
                continue

            total_sum += game_index

    return total_sum


if __name__ == "__main__":
    print(main())
