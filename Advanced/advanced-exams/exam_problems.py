# TODO 1.Bombs (Advanced exam 27.06.2020) (runtime 80/100)
# DATURA_BOMBS = 40
# CHERRY_BOMBS = 60
# SMOKE_DECOY = 120
#
#
# def mix_and_calculate(effects, casing):
#     if effects[0] + casing[-1] == DATURA_BOMBS:
#         bomb_pouch['Datura Bombs'] += 1
#         return True
#     elif effects[0] + casing[-1] == CHERRY_BOMBS:
#         bomb_pouch['Cherry Bombs'] += 1
#         return True
#     elif effects[0] + casing[-1] == SMOKE_DECOY:
#         bomb_pouch['Smoke Decoy Bombs'] += 1
#         return True
#     else:
#         casing[-1] -= 5
#         return False
#
#
# def filled_bomb_pouch(bomb_dict):
#     if bomb_dict['Datura Bombs'] >= 3 and bomb_dict['Cherry Bombs'] >= 3 and bomb_dict['Smoke Decoy Bombs'] >= 3:
#         return True
#     return False
#
#
# def print_the_rest(bomb_punch, effects, casing):
#     if effects:
#         print(f"Bomb Effects: {(', '.join(list(map(str, effects))))}")
#     else:
#         print("Bomb Effects: empty")
#     if casing:
#         print(f"Bomb Casings: {(', '.join(list(map(str, casing))))}")
#     else:
#         print("Bomb Casings: empty")
#
#     print(f"Cherry Bombs: {bomb_punch['Cherry Bombs']}")
#     print(f"Datura Bombs: {bomb_punch['Datura Bombs']}")
#     print(f"Smoke Decoy Bombs: {bomb_punch['Smoke Decoy Bombs']}")
#
#
# bombs_effects = list(map(int, input().split(', ')))
# bombs_casing = list(map(int, input().split(', ')))
#
# bomb_pouch = {'Cherry Bombs': 0, 'Datura Bombs': 0, 'Smoke Decoy Bombs': 0}
#
# while bombs_effects:
#     is_bomb = False
#     if mix_and_calculate(bombs_effects, bombs_casing):
#         is_bomb = True
#
#     if is_bomb:
#         bombs_effects.pop(0)
#         bombs_casing.pop()
#
#     if filled_bomb_pouch(bomb_pouch):
#         print('Bene! You have successfully filled the bomb pouch!')
#         print_the_rest(bomb_pouch, bombs_effects, bombs_casing)
#         break
#
#     if not bombs_effects and not filled_bomb_pouch(bomb_pouch):
#         print("You don't have enough materials to fill the bomb pouch.")
#         print_the_rest(bomb_pouch, bombs_effects, bombs_casing)
#         break
#
#
#
#
#
#
# TODO 2.Snake game (Advanced exam 27.06.2020) (100/100 - not mine)
# field_size = int(input())
# territory = [list(input()) for _ in range(field_size)]
#
#
# def check_starting_position(field, start):
#     for row in range(len(field)):
#         if start in field[row]:
#             return row, field[row].index(start)
#
#
# def is_outside(cur_row, cur_col, size):
#     if 0 <= cur_row < size and 0 <= cur_col < size:
#         return False
#     return True
#
#
# def find_burrow(field, burrow):
#     burrows = 0
#     for row in range(len(field)):
#         if burrow in field[row]:
#             burrows += 1
#             if burrows == 2:
#                 return row, field[row].index(burrow)
#
#
# def print_snake_filed(field):
#     for row in range(len(field)):
#         print(''.join(field[row]))
#
#
# START = 'S'
# BURROW = 'B'
#
# food_count = 0
#
# starting_row, starting_col = check_starting_position(territory, START)
#
# current_row, current_col = starting_row, starting_col
#
# move_commands = ["up", "down", "left", "right"]
#
# UP_MOVE = (-1, 0)
# DOWN_MOVE = (1, 0)
# LEFT_MOVE = (0, -1)
# RIGHT_MOVE = (0, 1)
#
# while food_count < 10:
#     direction = input()
#
#     last_row, last_col = current_row, current_col
#     if direction in move_commands:
#         if direction == 'up':
#             current_row += UP_MOVE[0]
#             current_col += UP_MOVE[1]
#
#         elif direction == 'down':
#             current_row += DOWN_MOVE[0]
#             current_col += DOWN_MOVE[1]
#
#         elif direction == 'left':
#             current_row += LEFT_MOVE[0]
#             current_col += LEFT_MOVE[1]
#
#         elif direction == 'right':
#             current_row += RIGHT_MOVE[0]
#             current_col += RIGHT_MOVE[1]
#
#         if is_outside(current_row, current_col, field_size):
#             territory[last_row][last_col] = '.'
#             print("Game over!")
#             break
#
#         if territory[current_row][current_col] == '*':
#             food_count += 1
#             territory[last_row][last_col] = '.'
#             territory[current_row][current_col] = 'S'
#
#         elif territory[current_row][current_col] == '-':
#             territory[last_row][last_col] = '.'
#             territory[current_row][current_col] = 'S'
#
#         elif territory[current_row][current_col] == 'B':
#             burrow_end_position = find_burrow(territory, BURROW)
#             territory[last_row][last_col] = '.'
#             territory[current_row][current_col] = '.'
#             current_row, current_col = burrow_end_position[0], burrow_end_position[1]
#             territory[current_row][current_col] = 'S'
#
# if food_count >= 10:
#     print(f"You won! You fed the snake.")
#
# print(f"Food eaten: {food_count}")
# print_snake_filed(territory)
#
#
#
#
#
#
# TODO 3. List manipulator (Advanced exam 27.06.2020) (100/100)
# def list_manipulator(*args):
#     list_nums = args[0]
#     list_nums = [el for el in list_nums]
#     if args[1] == "add":
#         if args[2] == "beginning":
#             rest_args = list(args[3:])
#             list_nums = rest_args + list_nums
#         elif args[2] == "end":
#             list_nums.extend(args[3:])
#         return list_nums
#
#     elif args[1] == "remove":
#         if args[2] == "beginning":
#             if args[3:]:
#                 to_remove = int(args[3])
#                 list_nums = list_nums[to_remove:]
#             else:
#                 list_nums = list_nums[1:]
#
#         elif args[2] == "end":
#             if args[3:]:
#                 to_remove = int(args[3])
#                 list_nums = list_nums[:-to_remove]
#             else:
#                 list_nums.pop()
#         return list_nums
#
#
# print(list_manipulator([1, 2, 3], "remove", "end"))
# print(list_manipulator([1, 2, 3], "remove", "beginning"))
# print(list_manipulator([1, 2, 3], "add", "beginning", 20))
# print(list_manipulator([1, 2, 3], "add", "end", 30))
# print(list_manipulator([1, 2, 3], "remove", "end", 2))
# print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
# print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
# print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
#
#
#
#
#
#
# TODO 1.Taxi Express (Advanced retake exam 19.08.2020) (100/100)
# from collections import deque
#
# customers = deque(map(int, input().split(', ')))
# drivers = list(map(int, input().split(', ')))
# total_time = sum(customers)
#
# while customers:
#
#     if not drivers:
#         print("Not all customers were driven to their destinations")
#         left_customers = list(map(str, customers))
#         print(f"Customers left: {(', '.join(left_customers))}")
#         break
#
#     if drivers[-1] >= customers[0]:
#         drivers.pop()
#         customers.popleft()
#     else:
#         drivers.pop()
#
#     if not customers:
#         print("All customers were driven to their destinations")
#         print(f"Total time: {total_time} minutes")
#         break
#
#
#
#
#
#
# TODO 2.Minesweeper generator (Advanced retake exam 19.08.2020) (incorrect 50/100)
# size = int(input())
# n_bombs = int(input())
# BOMB = "*"
#
#
# def check_if_matrix_valid(size_m):
#     if 2 <= size_m <= 15:
#         matr = [[0 for _ in range(size)] for _ in range(size)]
#         return matr
#     return False
#
#
# def set_the_bombs(matr, cnt_bombs, bomb, size_m):
#     for _ in range(cnt_bombs):
#         row_index, col_index = [int(el) for el in input()[1:-1].split(', ')]
#         matr[row_index][col_index] = bomb
#         if not is_outside(row_index, col_index, size_m):
#             matr[row_index][col_index] = bomb
#         else:
#             return False
#     return matr
#
#
# def is_outside(cur_row, cur_col, size_m):
#     if 0 <= cur_row < size_m and 0 <= cur_col < size_m:
#         return False
#     return True
#
#
# def increase_positions(matr, bomb):
#     for row in range(len(matr)):
#         if BOMB in matr[row]:
#             bomb_col = matr[row].index(bomb)
#             if not is_outside(row + 1, bomb_col, size):
#                 if matr[row + 1][bomb_col] != bomb:
#                     matr[row + 1][bomb_col] += 1
#
#             if not is_outside(row+1, bomb_col+1, size):
#                 if matr[row + 1][bomb_col + 1] != bomb:
#                     matr[row + 1][bomb_col + 1] += 1
#
#             if not is_outside(row, bomb_col+1, size):
#                 if matr[row][bomb_col + 1] != bomb:
#                     matr[row][bomb_col + 1] += 1
#
#             if not is_outside(row-1, bomb_col+1, size):
#                 if matr[row - 1][bomb_col + 1] != bomb:
#                     matr[row - 1][bomb_col + 1] += 1
#
#             if not is_outside(row-1, bomb_col, size):
#                 if matr[row - 1][bomb_col] != bomb:
#                     matr[row - 1][bomb_col] += 1
#
#             if not is_outside(row-1, bomb_col-1, size):
#                 if matr[row - 1][bomb_col - 1] != bomb:
#                     matr[row - 1][bomb_col - 1] += 1
#
#             if not is_outside(row, bomb_col-1, size):
#                 if matr[row][bomb_col - 1] != bomb:
#                     matr[row][bomb_col - 1] += 1
#
#             if not is_outside(row+1, bomb_col-1, size):
#                 if matr[row + 1][bomb_col - 1] != bomb:
#                     matr[row + 1][bomb_col - 1] += 1
#     return matr
#
#
# def print_the_matrix(matr):
#     for row in range(len(matr)):
#         print(" ".join(map(str, matr[row])))
#
#
# matrix = check_if_matrix_valid(size)
# if matrix:
#     if set_the_bombs(matrix, n_bombs, BOMB, size):
#         increase_positions(matrix, BOMB)
#         print_the_matrix(matrix)


# TODO 3.Numbers searching (Advanced retake exam 19.08.2020) (100/100)
# def find_missing_number(*numbers):
#     min_num = min(numbers)
#     max_num = max(numbers)
#     missed_num = [num for num in range(min_num, max_num + 1) if num not in numbers]
#     return missed_num
#
#
# def numbers_searching(*numbers):
#     sorted_nums = sorted(set([num for num in numbers if numbers.count(num) > 1]))
#     missed_num = find_missing_number(*numbers)
#     missed_num.append(sorted_nums)
#     return missed_num
#
#
# print(numbers_searching(1, 2, 4, 2, 5, 4))
# print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
# print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))


# TODO 1.Scheduling (Advanced exam 24.10.2020) (runtime 71/100)
# jobs_line = [int(el) for el in input().split(', ')]
# index = int(input())
# min_el = min(jobs_line)
# cycles_cnt = 0
#
# found_the_job = False
#
# while not found_the_job:
#     for i in range(1, len(jobs_line)+1):
#         current_element = jobs_line[i-1]
#         if current_element == min_el:
#             cycles_cnt += current_element
#             if index == jobs_line.index(current_element):
#                 found_the_job = True
#                 break
#     min_el += 1
#
# print(cycles_cnt)


# 3, 1, 10, 1, 2
# 0
#
# 4, 10, 10, 6, 2, 99
# 2

# TODO 2.Checkmate (Advanced exam 24.10.2020) (incorrect 71/100)
# def king_position(matr):
#     for row_k in range(n):
#         for col_k in range(n):
#             if matr[row_k][col_k] == "K":
#                 return row_k, col_k
#
#
# matrix = []
# n = 8
#
# for _ in range(n):
#     row__ = input().split()
#     matrix.append(row__)
#
#
# king_row, king_col = king_position(matrix)
# queens = []
#
# for col in range(king_col + 1, n):
#     if matrix[king_row][col] == "Q":
#         queens.append([king_row, col])
#         break
# for col in range(0, king_col):
#     if matrix[king_row][col] == "Q":
#         queens.append([king_row, col])
#         break
# for row in range(king_row + 1, n):
#     if matrix[row][king_col] == "Q":
#         queens.append([row, king_col])
#         break
# for row in range(0, king_row):
#     if matrix[row][king_col] == "Q":
#         queens.append([row, king_col])
#         break
#
#
# for i in range(n):
#     try:
#         if matrix[king_row - i][king_col - i] == "Q":
#             queens.append([king_row - i, king_col - i])
#             break
#     except:
#         IndexError
#     try:
#         if matrix[king_row + i][king_col + i] == "Q":
#             queens.append([king_row + i, king_col + i])
#             break
#     except:
#         IndexError
#     try:
#         if matrix[king_row - i][king_col + i] == "Q":
#             queens.append([king_row - i, king_col + i])
#             break
#     except:
#         IndexError
#     try:
#         if matrix[king_row + i][king_col - i] == "Q":
#             queens.append([king_row + i, king_col - i])
#             break
#     except:
#         IndexError
#
# if not queens:
#     print("The king is safe!")
# else:
#     for el in queens:
#         print(el)
#
#
#
#
#
#
# TODO 3.List pureness (Advanced exam 24.10.2020) (100/100)
# def best_list_pureness(*args):
#     numbers = list(int(el) for el in args[0])
#     times_to_rotate = args[1]
#     best_pureness = 0
#     list_result = 0
#     rotate = 0
#
#     for time in range(times_to_rotate + 1):
#         for index in range(len(numbers)):
#             list_result += numbers[index] * index
#         if list_result > best_pureness:
#             best_pureness = list_result
#             rotate = time
#         numbers.insert(0, numbers.pop())
#         times_to_rotate -= 1
#         list_result = 0
#     return f"Best pureness {best_pureness} after {rotate} rotations"


# test = ([4, 3, 2, 6], 4)
# result = best_list_pureness(*test)
# print(result)


# test = ([7, 9, 2, 5, 3, 4], 3)
# result = best_list_pureness(*test)
# print(result)


# test = ([1, 2, 3, 4, 5], 10)
# result = best_list_pureness(*test)
# print(result)
#
#
#
#
#
#
# TODO Problem 1 (Advanced retake exam 16.12.2020) (100/100)
# from collections import deque
#
#
# def print_males_females(male, female, cnt):
#     print(f"Matches: {cnt}")
#     if male:
#         print(f"Males left: {(', '.join(map(str, reversed(male))))}")
#     else:
#         print("Males left: none")
#     if female:
#         print(f"Females left: {(', '.join(map(str, female)))}")
#     else:
#         print("Females left: none")
#
#     return male, female, cnt
#
#
# males = list(int(el) for el in input().split())
# females = deque([int(el) for el in input().split()])
# matches = 0
#
# while females and males:
#     current_male = males[-1]
#     current_female = females[0]
#     if current_male <= 0 or current_male % 25 == 0:
#         males.pop()
#         continue
#     elif current_female <= 0 or current_female % 25 == 0:
#         females.pop()
#         continue
#     elif current_male == current_female:
#         females.popleft()
#         males.pop()
#         matches += 1
#     else:
#         females.popleft()
#         males[-1] -= 2
#
# print_males_females(males, females, matches)
#
#
#
#
#
#
# TODO Problem 2 (Advanced retake exam 16.12.2020) (100/100 not mine)
# def read_matrix():
#     size_matrix = int(input())
#     matrix = []
#     for row in range(size_matrix):
#         matrix.append(list(input()))
#     return matrix
#
#
# string = input()
# matrix = read_matrix()
# player_position = []
#
# for r in range(len(matrix)):
#     for c in range(len(matrix)):
#         if matrix[r][c] == "P":
#             player_position.append(r)
#             player_position.append(c)
#
# row = player_position[0]
# col = player_position[1]
#
# commands_count = int(input())
#
# for i in range(commands_count):
#     matrix[row][col] = "-"
#     command = input()
#     previous_row = row
#     previous_col = col
#
#     if command == "up":
#         row -= 1
#
#     elif command == "down":
#         row += 1
#
#     elif command == "left":
#         col -= 1
#
#     elif command == "right":
#         col += 1
#
#     if row not in range(0, len(matrix)) or col not in range(0, len(matrix)):
#         if len(string) > 0:
#             string = string[:-1]
#             row = previous_row
#             col = previous_col
#     else:
#         if matrix[row][col].isalpha():
#             string += matrix[row][col]
#
#     matrix[row][col] = "P"
#
# print(string)
# print(*["".join(x) for x in matrix], sep="\n")
#
#
#
#
#
#
# TODO Problem 3 (Advanced retake exam 16.12.2020) (100/100 stackoverflow <3)
# def get_magic_triangle(n_rows):
#     results = []
#     for _ in range(n_rows):
#         row = [1]
#         if results:
#             last_row = results[-1]
#             row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
#             row.append(1)
#         results.append(row)
#     return results
#
#
# print(get_magic_triangle(5))
#
#
#
#
#
#
