from flask import request, Blueprint, jsonify
from app_client.api.interceptor_resources import validate_resource
from app_client.api import cliente_views 

client_resources = Blueprint("client_resources",__name__)

@client_resources.route("/client", methods = ['GET'])
@validate_resource
def list_client():
    return jsonify(cliente_views.list_client())

@client_resources.route("/client/<_id>", methods = ['GET'])
@validate_resource
def list_client_by_id(_id):
    return jsonify(cliente_views.list_client_by_id(_id))
    

@client_resources.route("/client", methods = ['POST'])
@validate_resource
def insert_client():
    return jsonify(cliente_views.insert_client(request.get_json()))


@client_resources.route("/client/<_id>", methods = ['PUT'])
@validate_resource
def update_cliente(_id):
    return jsonify(cliente_views.update_client(request.get_json(), _id))