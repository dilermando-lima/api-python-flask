from flask import request, Blueprint, jsonify
from app_client.api.handle_excep import *
from app_client.api.interceptor_resources import validate_resource
from app_client.api.cliente_views import *

client_resources = Blueprint("client_resources",__name__)

@client_resources.route("/client", methods = ['GET'])
@validate_resource
def list():
    return jsonify(list_client())

@client_resources.route("/client/<id>", methods = ['GET'])
@validate_resource
def list_by_id(id):
    return jsonify(list_client_by_id(id))
    

@client_resources.route("/client", methods = ['POST'])
@validate_resource
def insert():
    return jsonify(insert_client(request.get_json()))


@client_resources.route("/client/<id>", methods = ['PUT'])
@validate_resource
def update(id):
    return jsonify(update_cliente(request.get_json(), id))