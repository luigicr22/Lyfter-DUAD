
employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]

departments = {}
for index_employee in range(len(employees)):
    if (employees[index_employee]["department"] in departments):
        list_department_employees = departments[employees[index_employee]["department"]]
        list_department_employees.append({"name": employees[index_employee]["name"],  "email": employees[index_employee]["email"]})
        departments[employees[index_employee]["department"]] = list_department_employees

    else:
        departments[employees[index_employee]["department"]] = [{"name": employees[index_employee]["name"],  "email": employees[index_employee]["email"]}]
print (departments)