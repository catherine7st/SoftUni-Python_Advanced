n = int(input())

matrix = []

for _ in range(n):
    elements = [int(el) for el in input().split()]
    matrix.append(elements)

first_diagonal = 0
second_diagonal = 0
col = n - 1

for index in range(n):
    first_diagonal += matrix[index][index]
    second_diagonal += matrix[index][col]
    col -= 1

print(abs(first_diagonal-second_diagonal))
