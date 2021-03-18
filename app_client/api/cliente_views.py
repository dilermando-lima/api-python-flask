from app_client.api.models import Client 
from app_client.api.models import db
from app_client.api.handle_excep import *

def list_client():
    cliente_list = Client.query.all()
    return cliente_list

def list_client_by_id(id):
    client = Client.query.filter_by(id=id).first()
    valid_None(404,"client {} not found".format(id), client )
    return client

def insert_client(body):

    valid_None(400, "'name' is required", body)
    valid_None(400, "'name' is required", body.get("name"))
    valid_None(400, "'email' is required", body.get("email"))

    client = Client(email=body.get("email"),name=body.get("name"))
    db.session.add(client)
    db.session.commit()
    return client

def update_cliente(body, id):

    valid_None(400, "'id' is required", id)
    valid_None(400, "'name' is required", body)
    valid_None(400, "'name' is required", body.get("name"))
    valid_None(400, "'email' is required", body.get("email"))

    client_to_update = Client.query.filter_by(id=id).first()
    valid_None(404,"client {} not found".format(id), client_to_update )
    
    client_to_update.name = body.get("name")
    # client_to_update.email = body["email"] if "email" in body else client_to_update.email
    client_to_update.email = body.get("email")

    db.session.add(client_to_update)
    db.session.commit()
    return client_to_update

    