rows, cols = [int(el) for el in input().split()]
result = [[f"{chr(num)}{chr(num2)}{chr(num)}" for num2 in range(num, num + cols)] for num in range(97, 97 + rows)]
[print(*row) for row in result]

# rows, cols = map(int, input().split())
# matrix = [[chr(97+i)+chr(97+i+x)+(chr(97+i)) for x in range(cols)] for i in range(rows)]
# print('\n'.join(" ".join(map(str, el)) for el in matrix))
