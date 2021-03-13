# def convert_numbers_to_absolute(nums_list):
#     result = [abs(el) for el in nums]
#     # result = list(map(lambda x: abs(x), nums_list))
#     return result

# nums = map(lambda x: float(x), input().split())
nums = [float(num) for num in input().split()]
print([abs(num) for num in nums])

# print(convert_numbers_to_absolute(nums))
