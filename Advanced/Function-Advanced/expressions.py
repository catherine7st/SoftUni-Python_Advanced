def expressions(nums, current_sum=0, expression=""):
    if not nums:
        return [(expression, current_sum)]

    result_plus = expressions(nums[1:], current_sum+nums[0], f"{expression}+{nums[0]}")
    result_minus = expressions(nums[1:], current_sum-nums[0], f"{expression}-{nums[0]}")
    return result_plus + result_minus


nums = [int(el) for el in input().split(', ')]
print(*[f"{el[0]}={el[1]}" for el in expressions(nums)], sep="\n")


# def tri_recursion(k):
#     if k > 0:
#         result = k + tri_recursion(k - 1)
#         print(result)
#     else:
#         result = 0
#     return result
#
#
# print("\n\nRecursion Example Results")
# tri_recursion(6)
