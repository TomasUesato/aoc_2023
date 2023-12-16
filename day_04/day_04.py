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


def part2():
    with open("input.txt") as file:
        content = file.read()
        lines = content.split("\n")
        num_cards = len(lines)
        cards = [1] * num_cards

        for card_index, card_data in enumerate(lines):
            winning_numbers_str, numbers_str = card_data.split("|")
            numbers = set(numbers_str.split())

            winning_numbers_set = set(
                winning_numbers_str.split(":")[1].split())

            matching_numbers = sum(
                1 for number in numbers if number in winning_numbers_set)

            for i in range(1, matching_numbers + 1):
                next_card_index = card_index - 1 + i
                if next_card_index < num_cards:
                    cards[next_card_index] += cards[card_index - 1]

    return sum(cards)


if __name__ == "__main__":
    print(part2())
