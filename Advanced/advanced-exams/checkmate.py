def king_position(matr):
    for row_k in range(n):
        for col_k in range(n):
            if matr[row_k][col_k] == "K":
                return row_k, col_k


matrix = []
n = 8

for _ in range(n):
    row__ = input().split()
    matrix.append(row__)


king_row, king_col = king_position(matrix)
queens = []

for col in range(king_col + 1, n):
    if matrix[king_row][col] == "Q":
        queens.append([king_row, col])
        break
for col in range(0, king_col):
    if matrix[king_row][col] == "Q":
        queens.append([king_row, col])
        break
for row in range(king_row + 1, n):
    if matrix[row][king_col] == "Q":
        queens.append([row, king_col])
        break
for row in range(0, king_row):
    if matrix[row][king_col] == "Q":
        queens.append([row, king_col])
        break


for i in range(n):
    try:
        if matrix[king_row - i][king_col - i] == "Q":
            queens.append([king_row - i, king_col - i])
            break
    except:
        IndexError
    try:
        if matrix[king_row + i][king_col + i] == "Q":
            queens.append([king_row + i, king_col + i])
            break
    except:
        IndexError
    try:
        if matrix[king_row - i][king_col + i] == "Q":
            queens.append([king_row - i, king_col + i])
            break
    except:
        IndexError
    try:
        if matrix[king_row + i][king_col - i] == "Q":
            queens.append([king_row + i, king_col - i])
            break
    except:
        IndexError

if not queens:
    print("The king is safe!")
else:
    for el in queens:
        print(el)
