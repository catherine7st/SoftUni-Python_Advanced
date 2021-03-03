(row, col) = [int(x) for x in input().split()]
matrix = []
max_sum = -999999999
best_matrix = []
for _ in range(row):
    current_row = [int(x) for x in input().split()]
    matrix.append(current_row)
for i in range(row - 2):
    for j in range(col - 2):
        current_sum = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i+1][j] + matrix[i+1][j+1] + matrix[i+1][j+2] + matrix[i+2][j] + matrix[i+2][j+1] + matrix[i+2][j+2]
        if current_sum > max_sum:
            max_sum = current_sum
            best_matrix = [[matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]], [matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2]], [matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]]]
print(f"Sum = {max_sum}")

for row_3x3 in range(len(best_matrix)):
    print(" ".join(str(x) for x in best_matrix[row_3x3]))
