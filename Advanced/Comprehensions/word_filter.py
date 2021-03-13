# words = input().split()
# even_words_length = [word for word in words if len(word) % 2 == 0]
# print(*even_words_length, sep='\n')


print(*[word for word in input().split() if len(word) % 2 == 0], sep='\n')
