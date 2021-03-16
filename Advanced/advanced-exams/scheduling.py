jobs_line = [int(el) for el in input().split(', ')]
index = int(input())
min_el = min(jobs_line)
cycles_cnt = 0

found_the_job = False

while not found_the_job:
    for i in range(1, len(jobs_line)+1):
        current_element = jobs_line[i-1]
        if current_element == min_el:
            cycles_cnt += current_element
            if index == jobs_line.index(current_element):
                found_the_job = True
                break
    min_el += 1

print(cycles_cnt)


# 3, 1, 10, 1, 2
# 0
#
# 4, 10, 10, 6, 2, 99
# 2