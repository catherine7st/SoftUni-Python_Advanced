def args_length(*args):
    result = len(args)
    return result


print(args_length(1, 32, 5))
print(args_length("john", "peter"))
print(args_length([1, 2, 3]))
