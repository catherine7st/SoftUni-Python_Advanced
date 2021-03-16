from collections import deque

cups = deque(map(int, input().split()))
bottles = list(map(int, input().split()))

waste_water = 0
while cups:
    if bottles:
        if bottles[-1] >= cups[0]:
            waste_water += bottles[-1] - cups[0]
            cups.popleft()
            bottles.pop()
        elif cups[0] > bottles[-1]:
            cups[0] -= bottles[-1]
            bottles.pop()
    else:
        print(f"Cups: {' '.join(map(str, cups))}")
        print(f"Wasted litters of water: {waste_water}")
        break

if not cups:
    print(f"Bottles: {' '.join(map(str, bottles))}")
    print(f"Wasted litters of water: {waste_water}")
