from collections import deque

amount = int(input())
people_queue = deque()

while True:
    command = input()
    if command == "Start":
        break
    people_queue.append(command)

while True:
    command = input()
    if command == "End":
        print(f"{amount} liters left")
        break
    if command.startswith("refill"):
        spl_command = command.split()
        refill_liters = int(spl_command[1])
        amount += refill_liters
    else:
        person = people_queue.popleft()
        person_liters = int(command)
        if person_liters <= amount:
            print(f"{person} got water")
            amount -= person_liters
        else:
            print(f"{person} must wait")


