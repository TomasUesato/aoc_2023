RED_CUBES = 12
GREEN_CUBES = 13
BLUE_CUBES = 14


def is_game_set_valid(game_set):
    for subset in game_set:
        if not is_subset_valid(subset):
            return False
    return True


def is_subset_valid(subset):
    cubes = subset.split(",")
    for cube in cubes:
        number, color = get_cube_info(cube)
        if color == "green" and GREEN_CUBES < number:
            return False
        if color == "red" and RED_CUBES < number:
            return False
        if color == "blue" and BLUE_CUBES < number:
            return False
    return True


def get_cube_info(cube):
    number, color = cube.split()
    return int(number), color


def part1():
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


def part2():
    power_sum = 0
    with open('input.txt', 'r') as file:
        for line in file:
            sets = line.split(":")[1]
            game_set = sets.split(";")
            power_sum += get_power(game_set)

    return power_sum


def get_power(game_set):
    max_red = 0
    max_blue = 0
    max_green = 0

    for subset in game_set:
        cubes = subset.split(",")
        for cube in cubes:
            number, color = get_cube_info(cube)
            if color == "red" and number > max_red:
                max_red = number
            if color == "green" and number > max_green:
                max_green = number
            if color == "blue" and number > max_blue:
                max_blue = number

    return max_red * max_green * max_blue


if __name__ == "__main__":
    print(part2())
