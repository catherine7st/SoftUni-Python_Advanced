n = int(input())
elements = []

for _ in range(n):
    chemicals = input().split()
    for el in chemicals:
        elements.append(el)

for el in set(elements):
    print(el)
