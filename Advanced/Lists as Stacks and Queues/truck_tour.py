from _collections import deque

n_pumps = int(input())
pumps = deque([])

for _ in range(n_pumps):
    pumps.append([el for el in input().split()])

for big_circle in range(n_pumps):
    is_valid = True
    truck_petrol = 0
    for small_circle in range(n_pumps):
        truck_petrol += int(pumps[small_circle][0]) - int(pumps[small_circle][1])

        if truck_petrol < 0:
            is_valid = False
            pumps.append(pumps.popleft())
            break
    if is_valid:
        print(big_circle)
        break
