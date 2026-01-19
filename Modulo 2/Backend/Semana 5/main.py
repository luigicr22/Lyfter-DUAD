from flask import Flask, jsonify, request
import utils
import os

app = Flask(__name__)

@app.route("/tasks", methods=["GET","POST","PUT","DELETE"])
def tasks():
    try:
        if request.method == "GET":
            filter_tasks = utils.read_tasks()
            status_filter = request.args.get("status")
            if status_filter:
                filter_tasks = list(filter(lambda task: task["status"] == status_filter, filter_tasks))
            return jsonify (filter_tasks),200
        
        if request.method == "POST":
            new_task = request.json
            if utils.check_fields_task(new_task):
                print
                new_task['id'] = int(new_task['id'])
                if os.path.exists("tasks.json"):
                    tasks = utils.read_tasks()
                    if utils.check_not_existed(new_task,tasks):
                        tasks.append(new_task)
                else:
                    tasks = []
                    tasks.append(new_task)
                if utils.write_json(tasks):
                    return jsonify(tasks), 201

        if request.method == "PUT":
            update_task = request.json
            if utils.check_fields_task(update_task):
                update_task['id'] = int(update_task['id'])
                tasks = utils.read_tasks()
                index = utils.check_existed(update_task,tasks)
                if index >= 0:
                    tasks[index] = update_task
                    if utils.write_json(tasks):
                        return jsonify(tasks), 200
        
        if request.method == "DELETE":
            id_task = request.args.get("id")
            if id_task is None:
                return jsonify(message="El parametro id es requerido"), 400
            if not id_task.isdecimal():
                return jsonify(message="El id debe ser un número entero mayor a cero"), 400
            tasks = utils.read_tasks()
            index = utils.check_existed({'id': int(id_task)},tasks)
            if index >= 0:
                tasks.pop(index)
                if utils.write_json(tasks):
                    return jsonify(tasks), 200

    except KeyError as error:
        return jsonify(message=f"El campo {error} es requerido"), 400
    except ValueError as error:
        return jsonify(message=str(error)), 400
    except FileNotFoundError:
        return jsonify(message="No se encontro el archivo JSON"), 404
    except Exception as error:
        print (error)
        return jsonify(message=f"Error interno del servidor: {error}"), 500

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)