def find_missing_number(*numbers):
    min_num = min(numbers)
    max_num = max(numbers)
    missed_num = [num for num in range(min_num, max_num + 1) if num not in numbers]
    return missed_num


def numbers_searching(*numbers):
    sorted_nums = sorted(set([num for num in numbers if numbers.count(num) > 1]))
    missed_num = find_missing_number(*numbers)
    missed_num.append(sorted_nums)
    return missed_num


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
