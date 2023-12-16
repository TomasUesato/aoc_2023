def part1():
    with open("input.txt") as file:
        matrix = [list(line.strip()) for line in file]
        total_sum = 0
        for row, row_value in enumerate(matrix):
            number = ""
            is_adjacent = False
            for col, cell in enumerate(row_value):
                if cell.isnumeric():
                    number += cell
                    is_adjacent = is_adjacent or check_adjacent_cells(
                        matrix, row, col)
                elif number and is_adjacent:
                    total_sum += int(number)
                    number = ""
                    is_adjacent = False
                else:
                    number = ""
            if number and is_adjacent:  # Handle number that extends to the end of the row
                total_sum += int(number)

    return total_sum


def check_adjacent_cells(matrix, row, col):
    num_rows, num_cols = len(matrix), len(matrix[0])

    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1), (0, 1),
                  (1, -1), (1, 0), (1, 1)]

    for row_dir, col_dir in directions:
        new_row, new_col = row + row_dir, col + col_dir
        if 0 <= new_row < num_rows and 0 <= new_col < num_cols and is_valid_symbol(matrix[row + row_dir][col + col_dir]):
            return True

    return False


def is_valid_symbol(char):
    return not char.isnumeric() and char != '.'


# Day 03, Part 2
# Go through the matrix and look for asteriscs
# Get adjacent cells and check for unique part numbers
# Check if the asterisc has exactly two adjacent part numbers
# Multiply those two numbers and add them to the result

def part2():
    with open("input.txt") as file:
        matrix = [list(line.strip()) for line in file]
        total_sum = 0
        for row, row_data in enumerate(matrix):
            for col, cell in enumerate(row_data):
                if cell == "*":
                    adjacent_numbers = get_adjacent_numbers(matrix, row, col)
                    if len(adjacent_numbers) == 2:
                        total_sum += int(adjacent_numbers[0]) * \
                            int(adjacent_numbers[1])

    return total_sum


def get_adjacent_numbers(matrix, row, col):
    adjacent_numbers = []
    num_rows, num_cols = len(matrix), len(matrix[0])

    for i in range(-1, 2):
        for j in range(-1, 2):
            new_row, new_col = row + i, col + j
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                cell = matrix[new_row][new_col]
                if cell.isnumeric():
                    start, end = find_numeric_range(matrix[new_row], new_col)
                    number = ''.join(matrix[new_row][start:end + 1])
                    adjacent_numbers.append(number)

                    if end > new_col:
                        break

    return adjacent_numbers


def find_numeric_range(matrix_row, col):
    begin = col
    end = col

    while begin - 1 >= 0 and matrix_row[begin - 1].isnumeric():
        begin -= 1
    while end + 1 <= len(matrix_row) - 1 and matrix_row[end + 1].isnumeric():
        end += 1

    return begin, end


if __name__ == "__main__":
    print(part2())
