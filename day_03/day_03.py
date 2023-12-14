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


if __name__ == "__main__":
    print(part1())
