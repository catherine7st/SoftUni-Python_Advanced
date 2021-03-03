line = list(map(int, input().split()))
capacity = int(input())

cnt_racks = 1
rack = 0

while line:
    if line[-1] + rack <= capacity:
        rack += line[-1]
        line.pop()
    else:
        rack = 0
        cnt_racks += 1

print(cnt_racks)
