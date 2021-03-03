n = int(input())
intersections = []

for _ in range(n):
    data = input()
    first_data, second_data = data.split("-")
    start_point, stop_point = [int(el) for el in first_data.split(",")]
    first_inter = range(start_point, stop_point + 1)
    start_point, stop_point = [int(el) for el in second_data.split(",")]
    second_inter = range(start_point, stop_point + 1)
    intersection = set(first_inter).intersection(second_inter)
    intersections.append(intersection)

longest = sorted(intersections, key=lambda x: -len(x))[0]

print(f"Longest intersection is {list(longest)} with length {len(longest)}")
