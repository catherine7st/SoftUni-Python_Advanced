# text = input()
# mapper = {'a', 'o', 'u', 'e', 'i'}
# new_text = [el for el in text if el.lower() not in mapper]
# print(''.join(new_text))


VOWELS = {'a', 'o', 'u', 'e', 'i'}
VOWELS = VOWELS.union(x.upper() for x in VOWELS)

text = input()
new_text = [el for el in text if el not in VOWELS]
print(''.join(new_text))
