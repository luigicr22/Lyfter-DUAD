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
    requeired_fields = ["id", "title", "description", "status"]
    for field in requeired_fields:
        if task.get(field) is None:
            raise KeyError(field)
    return True

def check_not_existed (task_to_check,tasks):
    for task in tasks:
        if task_to_check.get('id') == task.get('id'):
            raise ValueError(task.get('id'))
    return True

def check_existed (task_to_check,tasks):
    for index in range(len(tasks)):
        if task_to_check.get('id') == tasks[index].get('id'):
            return index
    raise ValueError(task_to_check.get('id'))