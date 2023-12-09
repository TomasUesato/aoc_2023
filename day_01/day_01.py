def get_total_sum():
    total_sum = 0
    with open('input.txt', 'r') as file:
        for line in file:
            line_sum = get_line_sum(line)
            total_sum += line_sum
    return total_sum


def get_line_sum(line):
    return int(first_digit(line) + last_digit(line))

# part 1

# def first_digit(line):
#     alpha = ""
#     for char in line:
#         if char.isnumeric():
#             return char


# def last_digit(line):
#     alpha = ""
#     for char in reversed(line):
#         if char.isnumeric():
#             return char

def first_digit(line):
    alpha = ""
    for char in line:
        if char.isnumeric():
            return char
        else:
            alpha += char
            for key in numbers.keys():
                if key in alpha:
                    return str(numbers[key])


def last_digit(line):
    alpha = ""
    for char in reversed(line):
        if char.isnumeric():
            return char
        else:
            alpha = char + alpha
            for key in numbers.keys():
                if key in alpha:
                    return str(numbers[key])


numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


if __name__ == "__main__":
    print(get_total_sum())
