list_of_keys = ["access_level", "age"]
employee = {"name": "John", "email": "john@ecorp.com", "access_level": 5, "age": 28}

for index in range(len(list_of_keys)):
    employee.pop(list_of_keys[index])

print(employee)