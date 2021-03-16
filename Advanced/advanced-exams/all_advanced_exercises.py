# TODO (Lists as Stacks and Queues - Exercise)
# TODO 1.Reverse numbers with a stack
# numbers = input().split()
#
# stack = []
#
# while numbers:
#     stack.append(numbers.pop())
#
# print(" ".join(stack))
#
#
#
#
# TODO 2.Maximum and minimum element
# n = int(input())
# stack = []
#
# for _ in range(n):
#     command = input().split()
#     if command[0] == '1':
#         stack.append(int(command[1]))
#     elif command[0] == '2' and len(stack) > 0:
#         stack.pop()
#     elif command[0] == '3' and len(stack) > 0:
#         print(max(stack))
#     elif command[0] == '4' and len(stack) > 0:
#         print(min(stack))
#
# print(", ".join(reversed(list(map(str, stack)))))
#
#
#
#
# TODO 3.Orders
# from _collections import deque
#
# total_food = int(input())
# orders = deque(map(int, input().split()))
#
# print(max(orders))
#
# while orders and orders[0] <= total_food:
#     total_food -= orders.popleft()
#
# if not orders:
#     print("Orders complete")
# else:
#     print(f"Orders left: {' '.join(map(str, orders))}")
#
#
#
#
# TODO 4.Fashion boutique
# line = list(map(int, input().split()))
# capacity = int(input())
#
# cnt_racks = 1
# rack = 0
#
# while line:
#     if line[-1] + rack <= capacity:
#         rack += line[-1]
#         line.pop()
#     else:
#         rack = 0
#         cnt_racks += 1
#
# print(cnt_racks)
#
#
#
#
# TODO 5.Truck tour
# from _collections import deque
#
# n_pumps = int(input())
# pumps = deque([])
#
# for _ in range(n_pumps):
#     pumps.append([el for el in input().split()])
#
# for big_circle in range(n_pumps):
#     is_valid = True
#     truck_petrol = 0
#     for small_circle in range(n_pumps):
#         truck_petrol += int(pumps[small_circle][0]) - int(pumps[small_circle][1])
#
#         if truck_petrol < 0:
#             is_valid = False
#             pumps.append(pumps.popleft())
#             break
#     if is_valid:
#         print(big_circle)
#         break
#
#
#
#
# TODO 6.Balanced parentheses
# brackets = input()
# is_balanced = True
#
# open_brackets = []
#
# mirror = {'{': '}', '[': ']', '(': ')'}
#
# for b in brackets:
#     if b in "{[(":
#         open_brackets.append(b)
#     else:
#         if not open_brackets:
#             is_balanced = False
#             break
#         current_open_bracket = open_brackets.pop()
#         if not mirror[current_open_bracket] == b:
#             is_balanced = False
#             break
#
# if is_balanced:
#     print("YES")
# else:
#     print("NO")
#
#
#
#
# TODO 7.Robotics (100/100)
# from _collections import deque
# from datetime import datetime, timedelta
#
# data = input().split(';')
# time = datetime.strptime(input(), '%H:%M:%S')
#
# robots = []
# available_robots = deque([])
# products = []
#
# for el in data:
#     robot_data = el.split('-')
#     robot = {'name': robot_data[0], 'processing_time': int(robot_data[1]), 'available_at': time}
#     robots.append(robot)
#     available_robots.append(robot)
#
# product = input()
# available_robots = deque(available_robots)
# while not product == 'End':
#     products.append(product)
#     product = input()
#
# products = deque(products)
# time = time + timedelta(seconds=1)
#
# while len(products) > 0:
#     current_product = products.popleft()
#
#     if not available_robots:
#         for r in robots:
#             if time >= r['available_at']:
#                 available_robots.append(r)
#     if not available_robots:
#         products.append(current_product)
#
#     else:
#         current_robot = available_robots.popleft()
#         current_robot['available_at'] = time + timedelta(seconds=current_robot['processing_time'])
#         robot = [el for el in robots if el == current_robot][0]
#         robot['available_at'] = time + timedelta(seconds=current_robot['processing_time'])
#         print(f"{robot['name']} - {current_product} [{time.strftime('%H:%M:%S')}]")
#
#     time = time + timedelta(seconds=1)
#
#
#
#
# # TODO 8.Crossroads (100/100)
# from collections import deque
#
# green_light = int(input())
# free_window = int(input())
# time_to_pass = green_light + free_window
# cars_on_queue = deque()
# total_cars = []
# crash_happened = False
# its_closed = False
#
# command = input()
#
# while not command == "END":
#     if command == "green":
#         for _ in range(len(cars_on_queue)):
#             if time_to_pass - free_window <= 0:
#                 its_closed = True
#                 break
#
#             elif time_to_pass - len(cars_on_queue[0]) >= 0:
#                 time_to_pass -= len(cars_on_queue[0])
#                 total_cars.append(cars_on_queue.popleft())
#
#             else:
#                 left = time_to_pass
#                 crash_happened = True
#                 print(f"A crash happened!\n{cars_on_queue[0]} was hit at {cars_on_queue[0][left]}.")
#                 break
#         time_to_pass = green_light + free_window
#     else:
#         cars_on_queue.append(command)
#
#     if crash_happened:
#         break
#
#     command = input()
#
# if crash_happened is False:
#     print(f"Everyone is safe.\n{len(total_cars)} total cars passed the crossroads.")
#
#
#
#
# TODO 9.Key revolver (100/100)
# from collections import deque
#
# price_bullet = int(input())
# size_barrel = int(input())
# bullets = list(map(int, input().split()))
# locks = deque(map(int, input().split()))
# reward = int(input())
#
# cnt_bullets = 0
# barrel = size_barrel
# while bullets:
#     if not barrel:
#         print("Reloading!")
#         barrel = size_barrel
#     if not locks:
#         break
#     else:
#         if bullets[-1] <= locks[0]:
#             print("Bang!")
#             bullets.pop()
#             locks.popleft()
#             cnt_bullets += 1
#             barrel -= 1
#         else:
#             print("Ping!")
#             bullets.pop()
#             cnt_bullets += 1
#             barrel -= 1
#
# if not locks:
#     money_for_bullets = cnt_bullets * price_bullet
#     earned_money = reward - money_for_bullets
#     print(f"{len(bullets)} bullets left. Earned ${earned_money}")
# else:
#     print(f"Couldn't get through. Locks left: {len(locks)}")
#
#
#
#
# TODO 10.Cups and bottles (100/100)
# from collections import deque
#
# cups = deque(map(int, input().split()))
# bottles = list(map(int, input().split()))
#
# waste_water = 0
# while cups:
#     if bottles:
#         if bottles[-1] >= cups[0]:
#             waste_water += bottles[-1] - cups[0]
#             cups.popleft()
#             bottles.pop()
#         elif cups[0] > bottles[-1]:
#             cups[0] -= bottles[-1]
#             bottles.pop()
#     else:
#         print(f"Cups: {' '.join(map(str, cups))}")
#         print(f"Wasted litters of water: {waste_water}")
#         break
#
# if not cups:
#     print(f"Bottles: {' '.join(map(str, bottles))}")
#     print(f"Wasted litters of water: {waste_water}")
#
#
#
#
#
#
# TODO Tuples and Sets - Exercise
# TODO 1 Unique usernames
# n = int(input())
# unique_name = set([input() for _ in range(n)])
#
# for name in unique_name:
#     print(name)
#
#
#
# TODO 2. Sets of elements
# n, m = map(int, input().split())
#
# set_n = {input() for el in range(n)}
# set_m = {input() for num in range(m)}
#
# same_nums = set_n.intersection(set_m)
# for num in same_nums:
#     print(num)
#
#
#
#
# TODO 3.Periodic Table
# n = int(input())
# elements = []
#
# for _ in range(n):
#     chemicals = input().split()
#     for el in chemicals:
#         elements.append(el)
#
# for el in set(elements):
#     print(el)
#
#
#
#
# TODO 4.Count Symbols
# text = input()
# elements = {}
# for char in text:
#     if char not in elements:
#         elements[char] = 0
#     elements[char] += 1
#
# for char, count in sorted(elements.items()):
#     print(f"{char}: {count} time/s")
#
#
#
#
#
# TODO 5.Phonebook
# command = input()
# phonebook = {}
#
# while not command.isdigit():
#     name, number = command.split("-")
#     if name not in phonebook:
#         phonebook[name] = number
#     else:
#         phonebook[name] = number
#
#     command = input()
#
# for _ in range(int(command)):
#     name = input()
#     if name not in phonebook:
#         print(f"Contact {name} does not exist.")
#     else:
#         print(f"{name} -> {phonebook[name]}")
#
#
#
#
# TODO 6.Longest Intersection
# n = int(input())
# intersections = []
#
# for _ in range(n):
#     data = input()
#     first_data, second_data = data.split("-")
#     start_point, stop_point = [int(el) for el in first_data.split(",")]
#     first_inter = range(start_point, stop_point + 1)
#     start_point, stop_point = [int(el) for el in second_data.split(",")]
#     second_inter = range(start_point, stop_point + 1)
#     intersection = set(first_inter).intersection(second_inter)
#     intersections.append(intersection)
#
# longest = sorted(intersections, key=lambda x: -len(x))[0]
#
# print(f"Longest intersection is {list(longest)} with length {len(longest)}")
#
#
#
#
# TODO 7.Battle of Names
# n = int(input())
#
# even_set = set()
# odd_set = set()
#
# for iteration in range(1, n + 1):
#     name = input()
#     current_sum = sum([ord(el) for el in name]) // iteration
#     if current_sum % 2 == 0:
#         even_set.add(current_sum)
#     else:
#         odd_set.add(current_sum)
#
# sum_evens = sum(even_set)
# sum_odds = sum(odd_set)
#
# if sum_evens == sum_odds:
#     modified_set = [str(el) for el in even_set.union(odd_set)]
#     print(f"{', '.join(modified_set)}")
# elif sum_odds > sum_evens:
#     modified_set = [str(el) for el in odd_set.difference(even_set)]
#     print(f"{', '.join(modified_set)}")
# else:
#     modified_set = [str(el) for el in odd_set.symmetric_difference(even_set)]
#     print(f"{', '.join(modified_set)}")
#
#
#
#
#
#
# TODO Multidimensional lists - Exercise
# TODO 1.Diagonal Difference
# n = int(input())
#
# matrix = []
#
# for _ in range(n):
#     elements = [int(el) for el in input().split()]
#     matrix.append(elements)
#
# first_diagonal = 0
# second_diagonal = 0
# col = n - 1
#
# for index in range(n):
#     first_diagonal += matrix[index][index]
#     second_diagonal += matrix[index][col]
#     col -= 1
#
# print(abs(first_diagonal-second_diagonal))
#
#
#
#
# TODO 2.2x2 Squares in Matrix
# rows, cols = [int(el) for el in input().split()]
#
#
# def init_matrix():
#     matrix = []
#     for _ in range(rows):
#         matrix.append(input().split())
#     return matrix
#
#
# def check_elements_are_equal(row, col, matr):
#     current_element = matr[row][col]
#     next_right_element = matr[row][col+1]
#     down_element = matr[row+1][col]
#     down_right_element = matr[row+1][col+1]
#     if current_element == next_right_element and next_right_element == down_element and down_element == down_right_element:
#         return True
#     return False
#
#
# matrix = init_matrix()
#
# counter = 0
#
# for row_index in range(rows-1):
#     for col_index in range(cols-1):
#         if check_elements_are_equal(row_index, col_index, matrix):
#             counter += 1
#
# print(counter)
#
#
#
#
# TODO 3.Maximum Sum
# (row, col) = [int(x) for x in input().split()]
# matrix = []
# max_sum = -999999999
# best_matrix = []
# for _ in range(row):
#     current_row = [int(x) for x in input().split()]
#     matrix.append(current_row)
# for i in range(row - 2):
#     for j in range(col - 2):
#         current_sum = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i+1][j] + matrix[i+1][j+1] + matrix[i+1][j+2] + matrix[i+2][j] + matrix[i+2][j+1] + matrix[i+2][j+2]
#         if current_sum > max_sum:
#             max_sum = current_sum
#             best_matrix = [[matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]], [matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2]], [matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]]]
# print(f"Sum = {max_sum}")
#
# for row_3x3 in range(len(best_matrix)):
#     print(" ".join(str(x) for x in best_matrix[row_3x3]))
#
#
#
#
# TODO 4.Matrix Shuffling
#
# def read_matrix(x):
#     matrix = []
#     for _ in range(x):
#         row = input().split()
#         matrix.append(row)
#
#     return matrix
#
#
# def print_result(matrix, line):
#     is_valid = False
#     if line[0] == "swap" and len(line) == 5:
#         is_valid = True
#         row_1, col_1, row_2, col_2 = [int(line[i]) for i in range(1, 5)]
#
#         try:
#             first_element = matrix[row_1][col_1]
#             second_element = matrix[row_2][col_2]
#             matrix[row_1].pop(col_1)
#             matrix[row_1].insert(col_1, second_element)
#             matrix[row_2].pop(col_2)
#             matrix[row_2].insert(col_2, first_element)
#         except:
#             is_valid = False
#
#     if is_valid:
#         [print(" ".join(row)) for row in matrix]
#     else:
#         print("Invalid input!")
#
#
# rows_count, cols_count = [int(el) for el in input().split()]
# matrix = read_matrix(rows_count)
#
# command = input()
#
# while not command == "END":
#     command_data = command.split()
#     print_result(matrix, command_data)
#     command = input()
#
#
#
# TODO 5.Snake move
# rows, cols = [int(el) for el in input().split()]
#
# word = input()
# matrix = []
#
# for row_index in range(rows):
#     matrix.append([0 for el in range(cols)])
#
# word_index = 0
#
# for row_index in range(rows):
#     for col_index in range(cols):
#         matrix[row_index][col_index] = word[word_index]
#         word_index += 1
#         if word_index == len(word):
#             word_index = 0
#
# for row_index in range(rows):
#     if row_index % 2 == 1:
#         matrix[row_index].reverse()
#     print(''.join(matrix[row_index]))
#
#
#
#
# TODO 6.Knight Game
# n = int(input())
# matrix = []
#
# for _ in range(n):
#     matrix.append(list(input()))
#
#
# def is_valid_bound(row, col):
#     if 0 <= row < n and 0 <= col < n:
#         return True
#     return False
#
#
# def calculate_kills(matrix, row, col):
#     kills = 0
#     rows = [-2, -2, 2, 2, 1, 1, -1, -1]
#     cols = [-1, 1, -1, 1, -2, 2, -2, 2]
#     for index in range(len(rows)):
#         potential_row = row+rows[index]
#         potential_col = col+cols[index]
#         if is_valid_bound(potential_row, potential_col):
#             potential_position = matrix[potential_row][potential_col]
#             if potential_position == "K":
#                 kills += 1
#     return kills
#
#
# removed_counter = 0
#
# while True:
#     max_kills = 0
#     killer_position = []
#
#     for row_index in range(n):
#         for col_index in range(n):
#             if matrix[row_index][col_index] == "K":
#                 kills = calculate_kills(matrix, row_index, col_index)
#                 if max_kills < kills:
#                     max_kills = kills
#                     killer_position = [row_index, col_index]
#     if not killer_position:
#         break
#     matrix[killer_position[0]][killer_position[1]] = "0"
#     removed_counter += 1
#
# print(removed_counter)
#
#
#
#
# TODO 7.Bombs
#
#
#
#
#
#
# TODO 8.Miner
#
#
#
#
#
# TODO 9.Radioactive Mutate Vampire Bunnies
#
#
#
#
#
# TODO Comprehensions - Exercise
# TODO 1.Word filter
# print(*[word for word in input().split() if len(word) % 2 == 0], sep='\n')
#
#
#
#
# TODO 2.Words lenghts
# names = input().split(", ")
# print(*[f"{name} -> {len(name)}" for name in names], sep=", ")
#
#
#
#
# TODO 3.Capitals
# countries = input().split(", ")
# capitals = input().split(", ")
#
# print(*[f"{countries[index]} -> {capitals[index]}" for index in range(len(countries))], sep='\n')
#
#
#
#
# TODO 4.Number Classification
# numbers = [int(el) for el in input().split(", ")]
#
# print(f"Positive: {', '.join([str(el) for el in numbers if el >= 0])}")
# print(f"Negative: {', '.join([str(el) for el in numbers if el < 0])}")
# print(f"Even: {', '.join([str(el) for el in numbers if el % 2 == 0])}")
# print(f"Odd: {', '.join([str(el) for el in numbers if el % 2 == 1])}")
#
#
#
#
# TODO 5.Diagonals
# n = int(input())
# matrix = []
#
# for row_index in range(n):
#     row = [int(num) for num in input().split(', ')]
#     matrix.append(row)
#
# diagonal_1 = []
# diagonal_2 = []
#
# for i in range(len(matrix)):
#     diagonal_1.append(matrix[i][i])
#     diagonal_2.append(matrix[i][n - i - 1])
#
# print(f"First diagonal: {', '.join([str(num) for num in diagonal_1])}. Sum: {sum(diagonal_1)}")
# print(f"Second diagonal: {', '.join([str(num) for num in diagonal_2])}. Sum: {sum(diagonal_2)}")
#
#
#
#
# TODO 6.Matrix of palindromes
# rows, cols = [int(el) for el in input().split()]
# result = [[f"{chr(num)}{chr(num2)}{chr(num)}" for num2 in range(num, num + cols)] for num in range(97, 97 + rows)]
# [print(*row) for row in result]
#
# rows, cols = map(int, input().split())
# matrix = [[chr(97+i)+chr(97+i+x)+(chr(97+i)) for x in range(cols)] for i in range(rows)]
# print('\n'.join(" ".join(map(str, el)) for el in matrix))
#
#
#
#
# TODO 7.Flatten lists
# input_str = input().split("|")[::-1]
#
# matrix = [x.split() for x in input_str]
#
# flatten_list = [j for i in matrix for j in i]
#
# print(" ".join(flatten_list))
#
#
# print(" ".join([j for i in [x.split() for x in input().split("|")[::-1]] for j in i]))
#
#
#
#
# TODO 8.Heroes inventory
# def update_heroes(name, item, price, hero):
#     if not hero[name].get(item):
#         hero[name].update({item: int(price)})
#     return hero
#
#
# names = input().split(', ')
#
# data = input()
# heroes = {name: {} for name in names}
#
#
# while not data == "End":
#     name, item, price = data.split('-')
#
#     heroes = update_heroes(name, item, price, heroes)
#
#     data = input()
#
# print(*[f"{name} -> Items: {len(inventory)}, Cost: {sum([inventory[item] for item in inventory])}"\n
# for name, inventory in heroes.items()], sep="\n")
#
#
#
#
# TODO 9.Bunker
# categories = {category: [] for category in input().split(", ")}
#
# quantity = 0
# quality = 0
#
# for _ in range(int(input())):
#     data = input().split(" - ")
#     categories[data[0]].append(data[1])
#
#     spl_quantity, spl_quality = data[2].split(";")
#
#     quantity += int(spl_quantity.split(":")[1])
#     quality += int(spl_quality.split(":")[1])
#
# print(f"Count of items: {quantity}")
# print(f"Average quality: {quality/len(categories):.2f}")
# [print(f"{category} -> {', '.join(items)}") for category, items in categories.items()]
#
#
#
#
# TODO 10.Matrix modification (100/100)
# size = int(input())
# matrix = []
# for row in range(size):
#     matrix.append([int(el) for el in input().split()])
#
# data = input()
# while not data == "END":
#     command, cor_1, cor_2, cnt = data.split()
#     cor_1 = int(cor_1)
#     cor_2 = int(cor_2)
#     cnt = int(cnt)
#     if cor_1 >= size or cor_2 >= size:
#         print("Invalid coordinates")
#     elif cor_1 < 0 or cor_2 < 0:
#         print("Invalid coordinates")
#     elif command == "Add":
#         matrix[cor_1][cor_2] += cnt
#     elif command == "Subtract":
#         matrix[cor_1][cor_2] -= cnt
#
#     data = input()
#
# for row in matrix:
#     print(' '.join(map(str, row)))
#
#
#
#
#
#
# TODO Functions Advanced - Exercise
# TODO 1.Even numbers
# def filter_even_numbers(numbers):
#     result = filter(lambda x: x % 2 == 0, numbers)
#     return result
#
#
# list_numbers = [int(el) for el in input().split()]
# print(list(filter_even_numbers(list_numbers)))
#
#
#
#
# TODO 2.Sort
# def sort_ascending_nums(nums):
#     new_list = sorted(nums)
#     return new_list
#
#
# numbers = [int(el) for el in input().split()]
# print(sort_ascending_nums(numbers))
#
#
#
#
# TODO 3.Min Max and Sum
# def print_min_max_sum(nums):
#     print(f"The minimum number is {min(nums)}")
#     print(f"The maximum number is {max(nums)}")
#     print(f"The sum number is: {sum(nums)}")
#
#
# numbers = [int(el) for el in input().split()]
# print_min_max_sum(numbers)
#
#
#
#
# TODO 4.Negative vs Positive
# def print_negative_positive_sums(nums):
#     negative_nums = sum(filter(lambda x: x < 0, nums))
#     positive_nums = sum(filter(lambda x: x > 0, nums))
#     print(negative_nums, positive_nums, sep='\n')
#     if positive_nums > abs(negative_nums):
#         print(f"The positives are stronger than the negatives")
#     else:
#         print(f"The negatives are stronger than the positives")
#
#
# numbers = [int(el) for el in input().split()]
# # numbers = map(int, input().split())
# print_negative_positive_sums(numbers)
#
#
#
#
# TODO 5.Odd or Even
# def odd_or_even(comm, nums):
#     if comm == "Odd":
#         return sum([el for el in nums if el % 2 == 1]) * len(nums)
#     elif comm == "Even":
#         return sum([el for el in nums if el % 2 == 0]) * len(nums)
#
#
# command = input()
# numbers = [int(el) for el in input().split()]
# print(odd_or_even(command, numbers))
#
#
#
#
# TODO 6.Arguments Length
# def args_length(*args):
#     result = len(args)
#     return result
#

#
#
# TODO 7.Concatenate
# def concatenate(*args):
#     return ''.join([el for el in args])

#
#
#
# TODO 8.Even or Odd
# def even_odd(*args):
#     command = args[-1]
#     if command == "even":
#         return list(filter(lambda x: x % 2 == 0, args[:-1]))
#     return list(filter(lambda x: x % 2 == 1, args[:-1]))
#
#
# print(even_odd(1, 2, 3, 4, 5, 6, "even"))

#
#
#
# TODO 9.Function Executor
# def sum_numbers(num1, num2):
#     return num1 + num2
#
#
# def multiply_numbers(num1, num2):
#     return num1 * num2
#
#
# def func_executor(*args):
#     result = []
#     for func_name, data in args:
#         res = func_name(*data)
#         result.append(res)
#     return result

#
#
#
# TODO 10.Keyword Arguments Length
# def kwargs_length(**kwargs):
#     return len(kwargs)
#
#
#
#
# TODO 11.Age Assignment
# def age_assignment(*names, **kwargs):
#     assignment = {}
#     for name in names:
#         for letter, age in kwargs.items():
#             if name.startswith(letter):
#                 assignment[name] = age
#     return assignment
#
#
#
#
# TODO 12.Recursion Palindrome
# def palindrome(word, index=0, left_index=-1):
#     if index == len(word) // 2:
#         return f"{word} is a palindrome"
#
#     if word[index] == word[left_index]:
#         return palindrome(word, index+1, left_index-1)
#     else:
#         return f"{word} is not a palindrome"
#
#
#
#
# TODO 13.Recursive Power
# def recursive_power(number, power):
#     if power == 1:
#         return number
#     return number * recursive_power(number, power-1)
