values = map(float, input().split(" "))

cnt_values = {}

for i in values:
    if i not in cnt_values:
        cnt_values[i] = 0
    cnt_values[i] += 1

for (value, count) in cnt_values.items():
    print(f"{value} - {count} times")
