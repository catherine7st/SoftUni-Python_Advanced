result = [[el for el in list_as_str.split()] for list_as_str in input().split('|')[::-1]]
print(*[" ".join(el) for el in result])

