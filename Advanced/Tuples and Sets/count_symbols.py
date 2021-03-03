text = input()
elements = {}
for char in text:
    if char not in elements:
        elements[char] = 0
    elements[char] += 1

for char, count in sorted(elements.items()):
    print(f"{char}: {count} time/s")
