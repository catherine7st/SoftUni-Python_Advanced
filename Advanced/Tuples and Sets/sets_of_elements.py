n, m = map(int, input().split())

set_n = {input() for el in range(n)}
set_m = {input() for num in range(m)}

same_nums = set_n.intersection(set_m)
for num in same_nums:
    print(num)
