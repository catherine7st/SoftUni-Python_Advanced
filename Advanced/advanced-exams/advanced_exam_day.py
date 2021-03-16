# # TODO Problem 1 (Advanced exam 14.02.2021) (edited after 50/100 - not checked)
# # from collections import deque
# #
# #
# # def check_perfect_firework(palm_cnt, willow_cnt, crossette_cnt):
# #     if palm_cnt >= 3 and willow_cnt >= 3 and crossette_cnt >= 3:
# #         return True
# #     return False
# #
# #
# # def print_if_party(check_perfect_firework):
# #     if check_perfect_firework:
# #         print("Congrats! You made the perfect firework show!")
# #     else:
# #         print("Sorry. You can’t make the perfect firework show.")
# #
# #     if firework:
# #         print(f"Firework Effects left: {', '.join(map(str, firework))}")
# #     if explosive:
# #         print(f"Explosive Power left: {', '.join(map(str, explosive))}")
# #
# #     print(f"Palm Fireworks: {palm}")
# #     print(f"Willow Fireworks: {willow}")
# #     print(f"Crossette Fireworks: {crossette}")
# #
# #     return check_perfect_firework
# #
# #
# # firework = deque([int(el) for el in input().split(', ')])
# # explosive = list([int(el) for el in input().split(', ')])
# #
# # palm = 0
# # willow = 0
# # crossette = 0
# #
# # while firework and explosive:
# #     if firework[0] <= 0:
# #         firework.pop()
# #     elif explosive[-1] <= 0:
# #         explosive.pop()
# #     else:
# #         if (firework[0] + explosive[-1]) % 3 == 0 and not (firework[0] + explosive[-1]) % 5 == 0:
# #             palm += 1
# #             firework.popleft()
# #             explosive.pop()
# #         elif (firework[0] + explosive[-1]) % 5 == 0 and not (firework[0] + explosive[-1]) % 3 == 0:
# #             willow += 1
# #             firework.popleft()
# #             explosive.pop()
# #         elif (firework[0] + explosive[-1]) % 5 == 0 and (firework[0] + explosive[-1]) % 3 == 0:
# #             crossette += 1
# #             firework.popleft()
# #             explosive.pop()
# #         else:
# #             firework[0] -= 1
# #             firework.append(firework.popleft())
# #
# #     if check_perfect_firework(palm, willow, crossette):
# #         break
# #
# # print_if_party(check_perfect_firework(palm, willow, crossette))
# #
# #
# #
# #
# #
# #
# # TODO Problem 1 (Advanced exam 14.02.2021) (college-solution 90/100 ?)
# # from collections import deque
# #
# # fireworks_effect = deque(int(el) for el in input().split(", "))
# # explosive_power = deque(int(el) for el in reversed(input().split(", ")))
# #
# # fireworks_crafted = {'Palm Fireworks': 0,
# #                      'Willow Fireworks': 0,
# #                      'Crossette Fireworks': 0
# #                      }
# #
# #
# # def palm_firework(effect, power):
# #     if ((effect[0] + power[0]) % 3 == 0) and not ((effect[0] + power[0]) % 5 == 0):
# #         fireworks_crafted['Palm Fireworks'] += 1
# #         fireworks_effect.popleft()
# #         explosive_power.popleft()
# #         return True
# #
# #
# # def willow_firework(effect, power):
# #     if ((effect[0] + power[0]) % 5 == 0) and not ((effect[0] + power[0]) % 3 == 0):
# #         fireworks_crafted['Willow Fireworks'] += 1
# #         fireworks_effect.popleft()
# #         explosive_power.popleft()
# #         return True
# #
# #
# # def crossette_firework(effect, power):
# #     if ((effect[0] + power[0]) % 3 == 0) and ((effect[0] + power[0]) % 5 == 0):
# #         fireworks_crafted['Crossette Fireworks'] += 1
# #         fireworks_effect.popleft()
# #         explosive_power.popleft()
# #         return True
# #
# #
# # def is_perfect(fireworks_list):
# #     if fireworks_list['Palm Fireworks'] >= 3 and \
# #             fireworks_list['Willow Fireworks'] >= 3 and \
# #             fireworks_list['Crossette Fireworks'] >= 3:
# #         return True
# #
# #
# # def firework_is_positive(fireworks_list):
# #     if fireworks_list[0] > 0:
# #         return True
# #
# #
# # def power_is_positive(power_list):
# #     if power_list[0] > 0:
# #         return True
# #
# #
# # def print_results(fireworks):
# #     if is_perfect(fireworks):
# #         print("Congrats! You made the perfect firework show!")
# #         for firework, qtty in fireworks.items():
# #             print(f"{firework}: {qtty}")
# #     else:
# #         print("Sorry. You can’t make the perfect firework show.")
# #         if fireworks_effect:
# #             print(f"Firework Effects left: {', '.join(str(fireworks_effect))}")
# #         if explosive_power:
# #             print(f"Explosive Power left: {', '.join([str(power) for power in reversed(explosive_power)])}")
# #         for firework, qtty in fireworks.items():
# #             print(f"{firework}: {qtty}")
# #
# #
# # def firecrackers_crafting(effect, power):
# #     if firework_is_positive(effect):
# #         if explosive_power and power_is_positive(power):
# #             if palm_firework(effect, power):
# #                 return True
# #             elif willow_firework(effect, power):
# #                 return True
# #             elif crossette_firework(effect, power):
# #                 return True
# #         else:
# #             explosive_power.popleft()
# #             return True
# #     else:
# #         fireworks_effect.popleft()
# #
# #
# # while fireworks_effect:
# #     if firecrackers_crafting(fireworks_effect, explosive_power):
# #         continue
# #     else:
# #         fireworks_effect[0] -= 1
# #         fireworks_effect.append(fireworks_effect.popleft())
# #         firecrackers_crafting(fireworks_effect, explosive_power)
# #
# # print_results(fireworks_crafted)
# #
# #
# #
# #
# #
# #
# # TODO Problem 2 (Advanced exam 14.02.2021) (not mine 100/100)
# n = int(input())
# matrix = []
# for r in range(n):
#     matrix.append(input().split())
#
# row = 0
# col = 0
# for r in range(n):
#     for c in range(n):
#         if matrix[r][c] == 'P':
#             row, col = r, c
#             break
#
# moves = {
#     'up': (-1, 0),
#     'down': (1, 0),
#     'right': (0, 1),
#     'left': (0, -1),
# }
#
# coins = 0
# positions = []
# while True:
#     command = input()
#     if command not in moves:
#         continue
#     if not command:
#         break
#     new_row = moves[command][0]
#     new_col = moves[command][1]
#
#     row += new_row
#     col += new_col
#
#     if not 0 <= row < n or not 0 <= col < n or matrix[row][col] == 'X':
#         coins = coins // 2
#         print(f"Game over! You've collected {coins} coins.")
#         break
#
#     coins += int(matrix[row][col])
#     positions.append([row, col])
#
#     if coins >= 100:
#         break
#
# if coins >= 100:
#     print(f"You won! You've collected {coins} coins.")
# print('Your path:')
# print(*[p for p in positions], sep='\n')
#
# #
# #
# #
# #
# #
# # # TODO Problem 3. (Advanced exam 14.02.2021) (before editing 90/100)
# # def stock_availability(inventory, command, *args):
# #     if command == 'delivery':
# #         inventory.extend(args)
# #     elif command == "sell":
# #         if args:
# #             data = args[0]
# #             if type(data) == int:
# #                 cnt_to_sell = int(data)
# #                 if len(inventory) < cnt_to_sell:
# #                     inventory.clear()
# #                 else:
# #                     for _ in range(cnt_to_sell):
# #                         inventory.pop()
# #             else:
# #                 inventory = list(filter(lambda pr: pr != data, inventory))
# #         else:
# #             inventory = inventory[1:]
# #
# #     return inventory
# #
# #
# # print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# # print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
# # print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
# # print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
# # print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
# # print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
# # print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
