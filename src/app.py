"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
# from models import Person


app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Create the jackson family object
jackson_family = FamilyStructure("Jackson")


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


# Generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


# Obtener todos los miembros 


@app.route('/members', methods=['GET'])
def handle_hello():
    # This is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {"hello": "world",
                     "family": members}
    return jsonify(response_body), 200

# Obtener un miembro en especifico

@app.route("/members/<int:id>",methods=["GET"])
def member_view(id):
    miembro = jackson_family.get_member(id)
    if miembro == "":
        return jsonify(message= "recuso no encontrado"),404
    else:
        response_body ={
            "id": miembro["id"],
            "firts_name": miembro["name"],
            "last_name": miembro["last_name"],
            "age": miembro["age"]
        }   
        return jsonify(response_body),200
    
# Eliminar un miembro en especifico

@app.route("/members/<int:id>", methods=["DELETE"])
def delete_member(id):
    delete = jackson_family.delete_member(id)
    if delete == "":
        response_body={
            "done":False
        }
        return jsonify(response_body),404
    else:
        response_body={
        "done":True
        }
        return jsonify(response_body),200
    
# Ruta para postear un miembro
    
@app.route("/members", methods=["POST"])
def agregar_miembro():
    member= request.get_json()
    agregar = jackson_family.add_member(member)
    if agregar == "":
        return jsonify(message= "Falta algun atributo"),400
    else:
       response_body ={
           "done":True
       }
       return jsonify(response_body),200



# This only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
