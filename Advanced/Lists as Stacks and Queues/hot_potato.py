from collections import deque

players = input().split()
steps = int(input())

q = deque(players)

while len(q) > 1:
    for _ in range(steps - 1):
        q.append(q.popleft())
    print(f"Removed {q.popleft()}")

print(f"Last is {q.popleft()}")