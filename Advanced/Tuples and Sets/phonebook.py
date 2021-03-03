command = input()
phonebook = {}

while not command.isdigit():
    name, number = command.split("-")
    if name not in phonebook:
        phonebook[name] = number
    else:
        phonebook[name] = number

    command = input()

for _ in range(int(command)):
    name = input()
    if name not in phonebook:
        print(f"Contact {name} does not exist.")
    else:
        print(f"{name} -> {phonebook[name]}")
