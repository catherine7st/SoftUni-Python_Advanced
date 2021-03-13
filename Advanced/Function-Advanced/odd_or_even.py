def odd_or_even(comm, nums):
    if comm == "Odd":
        return sum([el for el in nums if el % 2 == 1]) * len(nums)
    elif comm == "Even":
        return sum([el for el in nums if el % 2 == 0]) * len(nums)


command = input()
numbers = [int(el) for el in input().split()]
print(odd_or_even(command, numbers))
