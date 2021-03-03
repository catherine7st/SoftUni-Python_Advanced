brackets = input()
is_balanced = True

open_brackets = []

mirror = {'{': '}', '[': ']', '(': ')'}

for b in brackets:
    if b in "{[(":
        open_brackets.append(b)
    else:
        if not open_brackets:
            is_balanced = False
            break
        current_open_bracket = open_brackets.pop()
        if not mirror[current_open_bracket] == b:
            is_balanced = False
            break

if is_balanced:
    print("YES")
else:
    print("NO")
