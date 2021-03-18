from functools import wraps
from flask import request

def validate_resource(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        # headers = request.headers
        # data = request.data
        # print(data)
        return function(*args, **kwargs)
    return wrapper
