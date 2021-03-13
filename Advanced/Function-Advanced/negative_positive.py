def print_negative_positive_sums(nums):
    negative_nums = sum(filter(lambda x: x < 0, nums))
    positive_nums = sum(filter(lambda x: x > 0, nums))
    print(negative_nums, positive_nums, sep='\n')
    if positive_nums > abs(negative_nums):
        print(f"The positives are stronger than the negatives")
    else:
        print(f"The negatives are stronger than the positives")


numbers = [int(el) for el in input().split()]
# numbers = map(int, input().split())
print_negative_positive_sums(numbers)
