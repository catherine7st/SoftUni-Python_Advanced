def print_min_max_sum(nums):
    print(f"The minimum number is {min(nums)}")
    print(f"The maximum number is {max(nums)}")
    print(f"The sum number is: {sum(nums)}")


numbers = [int(el) for el in input().split()]
print_min_max_sum(numbers)
