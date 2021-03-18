from flask import abort
from sqlalchemy.exc import SQLAlchemyError
from app_client.api.models import Client, db
from app_client.api.handle_excep import valid_none


def list_client():
    try: 
        cliente_list = Client.query.all()
    except SQLAlchemyError as error: 
        abort(500, str(error.__dict__["orig"]))
    return cliente_list 


def list_client_by_id(_id):
    try: 
        client = Client.query.filter_by(id=_id).first()
    except SQLAlchemyError as error: 
        abort(500, str(error.__dict__["orig"]))

    valid_none(404,"client {} not found".format(_id), client )
    return client

def insert_client(body):

    valid_none(400, "'name' is required", body)
    valid_none(400, "'name' is required", body.get("name"))
    valid_none(400, "'email' is required", body.get("email"))


    try:
        client = Client(email=body.get("email"),name=body.get("name"))
        db.session.add(client)
        db.session.commit()
    except SQLAlchemyError as error: 
        abort(500, str(error.__dict__["orig"]))

    return client

def update_Cliente(body, _id):

    valid_none(400, "'id' is required", _id)
    valid_none(400, "'name' is required", body)
    valid_none(400, "'name' is required", body.get("name"))
    valid_none(400, "'email' is required", body.get("email"))

    try: 
        client_to_update = Client.query.filter_by(id=_id).first()
    except SQLAlchemyError as error: 
        abort(500, str(error.__dict__["orig"]))

    valid_none(404,"client {} not found".format(_id), client_to_update )
    
    client_to_update.name = body.get("name")
    # client_to_update.email = body["email"] if "email" in body else client_to_update.email
    client_to_update.email = body.get("email")

    try:
        db.session.add(client_to_update)
        db.session.commit()
    except SQLAlchemyError as error: 
        abort(500, str(error.__dict__["orig"]))

    return client_to_update

    