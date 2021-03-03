n = int(input())
stack = []

for _ in range(n):
    command = input().split()
    if command[0] == '1':
        stack.append(int(command[1]))
    elif command[0] == '2' and len(stack) > 0:
        stack.pop()
    elif command[0] == '3' and len(stack) > 0:
        print(max(stack))
    elif command[0] == '4' and len(stack) > 0:
        print(min(stack))

print(", ".join(reversed(list(map(str, stack)))))

# stack = [str(el) for el in stack]
# print(", ".join(reversed(stack)))
