import re
from flask import Blueprint, json, abort
from werkzeug.exceptions import HTTPException, InternalServerError

error_handle = Blueprint("error_handle",__name__)


        
@error_handle.app_errorhandler(HTTPException)
def handle_http_exception(error):
    response = error.get_response()
    response.data = json.dumps({
        "status": error.code,
        "message": error.description,
    })
    response.content_type = "application/json"
    return response



@error_handle.app_errorhandler(InternalServerError)
def handle_internal_error_exception(error):
    response = error.get_response()
    response.data =  json.dumps({
        "status": error.code,
        "message": error.description,
    })
    response.content_type = "application/json"
    return response



def valid_StrNone_Or_TrimEmpty(status, message, obj):
    if obj is None:
        abort(status,message)
    elif str(obj).isspace():
        abort(status, message)


def valid_None(status, message, obj):
    if obj is None:
        abort(status,message)


def valid_CondictionIsTrue(status, message, condition):
    if condition:
        abort(status,message)

def valid_EmailSingleNotValid(status, message, email):
    if not re.match("^[\\w!#$%&'*+/=?`{|}~^-]+(?:\\.[\\w!#$%&'*+/=?`{|}~^-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,6}$",str(email)):
        abort(status,message)

def valid_EmailMultNotValid(status, message, email):
    if not re.match("[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?",str(email)):
        abort(status,message)

def valid_LinkHttpNotValid(status, message, email):
    if not re.match("^(http:\\/\\/www\\.|https:\\/\\/www\\.|http:\\/\\/|https:\\/\\/)?[a-z0-9]+([\\-\\.]{1}[a-z0-9]+)*\\.[a-z]{2,5}(:[0-9]{1,5})?(\\/.*)?$",str(email)):
        abort(status,message)

