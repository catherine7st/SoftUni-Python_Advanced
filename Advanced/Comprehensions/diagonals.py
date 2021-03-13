n = int(input())
matrix = []

for row_index in range(n):
    row = [int(num) for num in input().split(', ')]
    matrix.append(row)

diagonal_1 = []
diagonal_2 = []

for i in range(len(matrix)):
    diagonal_1.append(matrix[i][i])
    diagonal_2.append(matrix[i][n - i - 1])

print(f"First diagonal: {', '.join([str(num) for num in diagonal_1])}. Sum: {sum(diagonal_1)}")
print(f"Second diagonal: {', '.join([str(num) for num in diagonal_2])}. Sum: {sum(diagonal_2)}")
