from collections import deque

customers = deque(map(int, input().split(', ')))
drivers = list(map(int, input().split(', ')))
total_time = sum(customers)

while customers:

    if not drivers:
        print("Not all customers were driven to their destinations")
        left_customers = list(map(str, customers))
        print(f"Customers left: {(', '.join(left_customers))}")
        break

    if drivers[-1] >= customers[0]:
        drivers.pop()
        customers.popleft()
    else:
        drivers.pop()

    if not customers:
        print("All customers were driven to their destinations")
        print(f"Total time: {total_time} minutes")
        break
