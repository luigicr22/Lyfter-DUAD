from flask import Flask, jsonify, request, Response
from db import PgManager
from repositoryUser import UserRepository
from repositoryCar import CarsRepository
from repositoryRental import RentalRepository

app = Flask(__name__)

@app.route("/user", methods=["GET", "POST", "PATCH"])
def user():
    try: 
        if request.method == "GET":
            values = request.args
            response = users_repo.get_all(values)
            return jsonify(response), 200
        
        if request.method == "POST":
            if request.is_json:
                values = request.json
                response = users_repo.create(values)
                return Response ("Creado",status=200)
            else:
                raise KeyError ("El request no contiene un archivo Json asociado")
        
        if request.method == "PATCH":
            if request.is_json:
                values = request.json
                if len(values) == 2 and "id" in values and "status" in values:
                    response = users_repo.update_status(values["id"], values["status"])
                    return Response ("Actualizado",status=200)
                else: 
                    raise KeyError ("El json no tiene las llaves requeridas")
            else:
                raise KeyError ("El request no contiene un archivo Json asociado")

    except KeyError as error:
        return {"Error": f"{error}"}, 415
    except Exception as error:
        return {"Error": f"{error}"}, 400        

@app.route("/user/debtor/<id>", methods=["PATCH"])
def user_update_debtor(id):
    try: 
        response = users_repo.update_status(id, "Moroso")
        return Response (f"User {id} Actualizado",status=200)

    except KeyError as error:
        return {"Error": f"{error}"}, 415
    except Exception as error:
        return {"Error": f"{error}"}, 400

@app.route("/car", methods=["GET", "POST", "PATCH"])
def car():
    try: 
        if request.method == "GET":
            values = request.args
            response = cars_repo.get_all(values)
            return jsonify(response), 200
        
        if request.method == "POST":
            if request.is_json:
                values = request.json
                response = cars_repo.create(values)
                return Response ("Creado",status=200)
            else:
                raise KeyError ("El request no contiene un archivo Json asociado")
        
        if request.method == "PATCH":
            if request.is_json:
                values = request.json
                if len(values) == 2 and "id" in values and "status" in values:
                    response = cars_repo.update_status(values["id"], values["status"])
                    return Response ("Actualizado",status=200)
                else: 
                    raise KeyError ("El json no tiene las llaves requeridas")
            else:
                raise KeyError ("El request no contiene un archivo Json asociado")

    except KeyError as error:
        return {"Error": f"{error}"}, 415
    except Exception as error:
        return {"Error": f"{error}"}, 400        

@app.route("/rental", methods=["GET", "POST", "PATCH"])
def rental():
    try: 
        if request.method == "GET":
            values = request.args
            response = rentals_repo.get_all(values)
            return jsonify(response), 200
        
        if request.method == "POST":
            if request.is_json:
                values = request.json
                response = rentals_repo.create(values)
                return Response ("Creado",status=200)
            else:
                raise KeyError ("El request no contiene un archivo Json asociado")
        
        if request.method == "PATCH":
            if request.is_json:
                values = request.json
                if len(values) == 2 and "id" in values and "status" in values:
                    response = rentals_repo.update_status(values["id"], values["status"])
                    return Response ("Actualizado",status=200)
                else: 
                    raise KeyError ("El json no tiene las llaves requeridas")
            else:
                raise KeyError ("El request no contiene un archivo Json asociado")

    except KeyError as error:
        return {"Error": f"{error}"}, 415
    except Exception as error:
        return {"Error": f"{error}"}, 400        

@app.route("/rental/completed/<id>", methods=["PATCH"])
def rental_completed(id):
    try: 
        response = rentals_repo.update_status(id, "Completado")
        return Response (f"Rental {id} Actualizado",status=200)

    except KeyError as error:
        return {"Error": f"{error}"}, 415
    except Exception as error:
        return {"Error": f"{error}"}, 400

if __name__ == "__main__":
    try:
        db_manager = PgManager(
            db_name="postgres",
            user="postgres",
            password="postgres",
            host="localhost",
            port=5432
        )
        users_repo = UserRepository(db_manager)
        cars_repo = CarsRepository(db_manager)
        rentals_repo = RentalRepository(db_manager)

        app.run(host="localhost", debug=True)

    except Exception as error:
        print (error)