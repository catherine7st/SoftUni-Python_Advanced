names = input().split(", ")
print(*[f"{name} -> {len(name)}" for name in names], sep=", ")
