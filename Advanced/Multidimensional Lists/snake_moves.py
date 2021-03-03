rows, cols = [int(el) for el in input().split()]

word = input()
matrix = []

for row_index in range(rows):
    matrix.append([0 for el in range(cols)])

word_index = 0

for row_index in range(rows):
    for col_index in range(cols):
        matrix[row_index][col_index] = word[word_index]
        word_index += 1
        if word_index == len(word):
            word_index = 0

for row_index in range(rows):
    if row_index % 2 == 1:
        matrix[row_index].reverse()
    print(''.join(matrix[row_index]))
