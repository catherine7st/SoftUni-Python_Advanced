from _collections import deque

total_food = int(input())
orders = deque(map(int, input().split()))

print(max(orders))

while orders and orders[0] <= total_food:
    total_food -= orders.popleft()

if not orders:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(map(str, orders))}")