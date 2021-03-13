# categories = {category: [] for category in input().split(", ")}
#
# quantity = 0
# quality = 0
#
# for _ in range(int(input())):
#     data = input().split(" - ")
#     categories[data[0]].append(data[1])
#
#     information_data = data[2].split(";")
#     quantity += int(information_data[0].split(":")[1])
#     quality += int(information_data[1].split(":")[1])
#
# print(f"Count of items: {quantity}")
# print(f"Average quality: {quality/len(categories):.2f}")
# [print(f"{category} -> {', '.join(items)}") for category, items in categories.items()]

categories = input().split(', ')
items = {category: [] for category in categories}
n = int(input())
for _ in range(n):
    args = input().split(' - ')
    quantity, quality = [int(x.split(':')[1]) for x in args[2].split(';')]
    items[args[0]].append({args[1]: (quantity, quality)})
count = sum(data[0] for category in items.values() for item in category for data in list(item.values()))
quality_sum = sum(data[1] for category in items.values() for item in category for data in list(item.values()))

print(f"Count of items: {count}")
print(f"Average quality: {(quality_sum/len(items)):.2f}")
for cat, value in items.items():
    print(f"{cat} -> {', '.join([list(items.keys())[0] for item in value])}")
