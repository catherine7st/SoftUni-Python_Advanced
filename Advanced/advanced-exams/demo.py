size = int(input())
matrix = []
for row in range(size):
    matrix.append([int(el) for el in input().split()])

data = input()
while not data == "END":
    command, cor_1, cor_2, cnt = data.split()
    cor_1 = int(cor_1)
    cor_2 = int(cor_2)
    cnt = int(cnt)
    if cor_1 >= size or cor_2 >= size:
        print("Invalid coordinates")
    elif cor_1 < 0 or cor_2 < 0:
        print("Invalid coordinates")
    elif command == "Add":
        matrix[cor_1][cor_2] += cnt
    elif command == "Subtract":
        matrix[cor_1][cor_2] -= cnt

    data = input()

for row in matrix:
    print(' '.join(map(str, row)))
