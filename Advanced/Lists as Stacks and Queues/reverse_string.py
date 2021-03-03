text = input()

stack = []
for el in text:
    stack.append(el)

result = ''

while stack:
    result += stack.pop()

print(result)

