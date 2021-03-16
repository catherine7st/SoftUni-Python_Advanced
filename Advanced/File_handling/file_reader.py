with open('numbers.txt', 'r') as file:
    print(sum([int(el) for el in file.readlines()]))
