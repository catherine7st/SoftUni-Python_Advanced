rows_count = int(input())
territory = []
food_count = 0
snake_position = ""
burrow = "B"

for row_index in range(rows_count):
    row = list(input())
    territory.append(row)

for row_index in range(len(territory)):
    if "S" in territory[row_index]:
        snake_position = territory[row_index][territory[row_index].index("S")]

move_command = input()

while food_count < 10 or "S" in len(territory):
    for row in range(len(territory)):
        for col in range(row):
            if move_command == "up":
                snake_position = territory[col][row - 1]
            elif move_command == "down":
                snake_position = territory[col][row + 1]
            elif move_command == "left":
                snake_position = territory[col - 1][row]
            elif move_command == "right":
                snake_position = territory[col + 1][row]

    move_command = input()
