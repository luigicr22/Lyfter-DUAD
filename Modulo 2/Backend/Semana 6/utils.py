import json

def read_tasks():
    try:
        with open('tasks.json', 'r', encoding='utf-8') as file:
            tasks = json.load(file)
        return tasks
    except FileNotFoundError as error:
        raise error

def write_json(tasks):
    with open("tasks.json", 'w', encoding='utf-8') as file:
        json.dump(tasks, file, indent=4)
    return True

def check_fields_task(task):
    required_fields = ["id", "title", "description", "status"]
    required_status = ["Por Hacer", "En Progreso", "Completada"]
    for field in required_fields:
        if task.get(field) is None:
            raise KeyError(field)
    if task.get('status') not in required_status:
        raise ValueError("El campo status tiene estado invalido")
    if not type(task.get('id')) is int:
        raise ValueError("El id debe ser un número entero mayor a cero")
    return True

def check_not_existed (task_to_check,tasks):
    for task in tasks:
        if task_to_check.get('id') == task.get('id'):
            raise ValueError(f"El id {task.get('id')} ya existe")
    return True

def check_existed (task_to_check,tasks):
    for index in range(len(tasks)):
        if task_to_check.get('id') == tasks[index].get('id'):
            return index
    raise ValueError(f"El id {task_to_check.get('id')} no existe")