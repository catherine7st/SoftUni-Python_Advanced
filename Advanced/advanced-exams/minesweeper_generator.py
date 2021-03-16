size = int(input())
n_bombs = int(input())
BOMB = "*"


def check_if_matrix_valid(size_m):
    if 2 <= size_m <= 15:
        matr = [[0 for _ in range(size)] for _ in range(size)]
        return matr
    return False


def set_the_bombs(matr, cnt_bombs, bomb, size_m):
    for _ in range(cnt_bombs):
        row_index, col_index = [int(el) for el in input()[1:-1].split(', ')]
        matr[row_index][col_index] = bomb
        if not is_outside(row_index, col_index, size_m):
            matr[row_index][col_index] = bomb
        else:
            return False
    return matr


def is_outside(cur_row, cur_col, size_m):
    if 0 <= cur_row < size_m and 0 <= cur_col < size_m:
        return False
    return True


def increase_positions(matr, bomb):
    for row in range(len(matr)):
        if BOMB in matr[row]:
            bomb_col = matr[row].index(bomb)
            if not is_outside(row + 1, bomb_col, size):
                if matr[row + 1][bomb_col] != bomb:
                    matr[row + 1][bomb_col] += 1

            if not is_outside(row+1, bomb_col+1, size):
                if matr[row + 1][bomb_col + 1] != bomb:
                    matr[row + 1][bomb_col + 1] += 1

            if not is_outside(row, bomb_col+1, size):
                if matr[row][bomb_col + 1] != bomb:
                    matr[row][bomb_col + 1] += 1

            if not is_outside(row-1, bomb_col+1, size):
                if matr[row - 1][bomb_col + 1] != bomb:
                    matr[row - 1][bomb_col + 1] += 1

            if not is_outside(row-1, bomb_col, size):
                if matr[row - 1][bomb_col] != bomb:
                    matr[row - 1][bomb_col] += 1

            if not is_outside(row-1, bomb_col-1, size):
                if matr[row - 1][bomb_col - 1] != bomb:
                    matr[row - 1][bomb_col - 1] += 1

            if not is_outside(row, bomb_col-1, size):
                if matr[row][bomb_col - 1] != bomb:
                    matr[row][bomb_col - 1] += 1

            if not is_outside(row+1, bomb_col-1, size):
                if matr[row + 1][bomb_col - 1] != bomb:
                    matr[row + 1][bomb_col - 1] += 1
    return matr


def print_the_matrix(matr):
    for row in range(len(matr)):
        print(" ".join(map(str, matr[row])))


matrix = check_if_matrix_valid(size)
if matrix:
    if set_the_bombs(matrix, n_bombs, BOMB, size):
        increase_positions(matrix, BOMB)
        print_the_matrix(matrix)
