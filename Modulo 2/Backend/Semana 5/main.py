from flask import Flask, jsonify, request
import utils
import os

app = Flask(__name__)

@app.route("/tasks", methods=["GET"])
def get_tasks():
    try:
        filter_tasks = utils.read_tasks()
        status_filter = request.args.get("status")
        if status_filter:
            filter_tasks = list(filter(lambda task: task["status"] == status_filter, filter_tasks))
            return jsonify (filter_tasks),200
        return jsonify (filter_tasks),200
    
    except FileNotFoundError:
        return jsonify(message="No se encontro el archivo JSON"), 404
    except Exception:
        return jsonify(message=f"Error interno del servidor"), 500


@app.route("/newtask", methods=["POST"])
def post_task():
    try:
        new_task = request.json
        if utils.check_fields_task(new_task):
            if os.path.exists("tasks.json"):
                tasks = utils.read_tasks()
                if utils.check_not_existed(new_task,tasks):
                    tasks.append(new_task)
            else:
                tasks = []
                tasks.append(new_task)
            if utils.write_json(tasks):
                return jsonify(tasks), 200
    
    except KeyError as error:
        return jsonify(message=f"El campo {error} es requerido"), 400
    except ValueError as error:
        return jsonify(message=f"El id {error} ya existe"), 400
    except Exception:
        return jsonify(message=f"Error interno del servidor"), 500


@app.route("/updatetask", methods=["PUT"])
def put_task():
    try:
        update_task = request.json
        if utils.check_fields_task(update_task):
            tasks = utils.read_tasks()
            index = utils.check_existed(update_task,tasks)
            if index >= 0:
                tasks[index] = update_task
                if utils.write_json(tasks):
                   return jsonify(tasks), 200
    
    except KeyError as error:
        return jsonify(message=f"El campo {error} es requerido"), 400
    except ValueError as error:
        return jsonify(message=f"El id {error} no existe"), 400
    except FileNotFoundError:
        return jsonify(message="No se encontro el archivo JSON"), 404
    except Exception:
        return jsonify(message=f"Error interno del servidor"), 500


@app.route("/deletetask/<id_task>", methods=["DELETE"])
def delete_task(id_task):
    try:
        delete_task = {"id":int(id_task)}
        tasks = utils.read_tasks()
        index = utils.check_existed(delete_task,tasks)
        if index >= 0:
            tasks.pop(index)
            if utils.write_json(tasks):
                return jsonify(tasks), 200
    
    except ValueError as error:
        return jsonify(message=f"El id {error} no existe"), 400
    except FileNotFoundError:
        return jsonify(message="No se encontro el archivo JSON"), 404
    except Exception:
        return jsonify(message=f"Error interno del servidor"), 500

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)