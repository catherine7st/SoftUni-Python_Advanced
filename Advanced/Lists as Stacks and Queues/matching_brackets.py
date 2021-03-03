line = input()

stack = []

for index in range(len(line)):
    el = line[index]
    if el == "(":
        stack.append(index)
    elif el == ")":
        j = stack.pop()
        print(line[j:index+1])


