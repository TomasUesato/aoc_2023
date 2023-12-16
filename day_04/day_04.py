def part1():
    total_points = 0
    with open("input.txt") as file:
        for line in file:
            winning_numbers_str, numbers_str = line.split("|")
            numbers = set(numbers_str.split())
            winning_numbers = set(winning_numbers_str.split(":")[1].split())
            matching_numbers = sum(
                1 for number in numbers if number in winning_numbers)

            if matching_numbers > 0:
                total_points += 2 ** (matching_numbers - 1)

    return total_points


if __name__ == "__main__":
    print(part1())
