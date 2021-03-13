def sort_ascending_nums(nums):
    new_list = sorted(nums)
    return new_list


numbers = [int(el) for el in input().split()]
print(sort_ascending_nums(numbers))
