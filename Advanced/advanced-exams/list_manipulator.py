def list_manipulator(*args):
    list_nums = args[0]
    list_nums = [el for el in list_nums]
    if args[1] == "add":
        if args[2] == "beginning":
            rest_args = list(args[3:])
            list_nums = rest_args + list_nums
        elif args[2] == "end":
            list_nums.extend(args[3:])
        return list_nums

    elif args[1] == "remove":
        if args[2] == "beginning":
            if args[3:]:
                to_remove = int(args[3])
                list_nums = list_nums[to_remove:]
            else:
                list_nums = list_nums[1:]

        elif args[2] == "end":
            if args[3:]:
                to_remove = int(args[3])
                list_nums = list_nums[:-to_remove]
            else:
                list_nums.pop()
        return list_nums


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
