rows, cols = [int(el) for el in input().split()]


def init_matrix():
    matrix = []
    for _ in range(rows):
        matrix.append(input().split())
    return matrix


def check_elements_are_equal(row, col, matr):
    current_element = matr[row][col]
    next_right_element = matr[row][col+1]
    down_element = matr[row+1][col]
    down_right_element = matr[row+1][col+1]
    if current_element == next_right_element and next_right_element == down_element and down_element == down_right_element:
        return True
    return False


matrix = init_matrix()

counter = 0

for row_index in range(rows-1):
    for col_index in range(cols-1):
        if check_elements_are_equal(row_index, col_index, matrix):
            counter += 1

print(counter)
