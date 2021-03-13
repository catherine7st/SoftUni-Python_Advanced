# def strs_to_ints(strs):
#     return [int(x) for x in strs]
#
#
# def read_matrix():
#     rows_count = int(input())
#     return [strs_to_ints(input().split(', ')) for _ in range(rows_count)]
#
#
# matrix = read_matrix()
# print([x for row in matrix for x in row])


rows_count = int(input())
matrix = []
for _ in range(rows_count):
    matrix.append([int(x) for x in input().split(', ')])

print([x for row in matrix for x in row])
