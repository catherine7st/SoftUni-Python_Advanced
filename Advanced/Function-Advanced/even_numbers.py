def filter_even_numbers(numbers):
    result = filter(lambda x: x % 2 == 0, numbers)
    return result


list_numbers = [int(el) for el in input().split()]
print(list(filter_even_numbers(list_numbers)))
