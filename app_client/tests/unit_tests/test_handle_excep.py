import pytest
from werkzeug.exceptions import HTTPException
from app_client.api import handle_excep

def test_valid_str_none_or_trim_empty():
    with pytest.raises(HTTPException):
        handle_excep.valid_str_none_or_trim_empty(400,"testing",None)
    handle_excep.valid_str_none_or_trim_empty(400,"testing","Some Name")
    with pytest.raises(HTTPException):
        obj = {}
        handle_excep.valid_str_none_or_trim_empty(400,"testing",obj.get("attr_not_exist"))
    with pytest.raises(HTTPException):
        handle_excep.valid_str_none_or_trim_empty(400,"testing","")
    with pytest.raises(HTTPException):
        handle_excep.valid_str_none_or_trim_empty(400,"testing","      ")

def test_valid_none():
    with pytest.raises(HTTPException):
        handle_excep.valid_none(400,"testing",None)
    handle_excep.valid_none(400,"testing","")
    handle_excep.valid_none(400,"testing","     ")
    with pytest.raises(HTTPException):
        obj = None
        handle_excep.valid_none(400,"testing",obj)

def test_valid_condiction_is_true():
    with pytest.raises(HTTPException):
        handle_excep.valid_condiction_is_true(400,"testing",True)
    handle_excep.valid_condiction_is_true(400,"testing",False)
    

def test_valid_email_single_not_valid():
    with pytest.raises(HTTPException):
        handle_excep.valid_email_single_not_valid(400,"testing","some word not like email")
    with pytest.raises(HTTPException):
        handle_excep.valid_email_single_not_valid(400,"testing","email@email")
    handle_excep.valid_email_single_not_valid(400,"testing","email@email.com")
    handle_excep.valid_email_single_not_valid(400,"testing",None)

def test_valid_email_mult_not_valid():
    with pytest.raises(HTTPException):
        handle_excep.valid_email_mult_not_valid(400,"testing","some word not like email")
    with pytest.raises(HTTPException):
        handle_excep.valid_email_mult_not_valid(400,"testing","email@")
    with pytest.raises(HTTPException):
        handle_excep.valid_email_mult_not_valid(400,"testing","email@;email@email.com")   
    handle_excep.valid_email_mult_not_valid(400,"testing","email@email.com")
    handle_excep.valid_email_mult_not_valid(400,"testing","email@email.com;email@email.com")
    handle_excep.valid_email_mult_not_valid(400,"testing","email@email.com;email@email.com;email@email.com")
    handle_excep.valid_email_mult_not_valid(400,"testing",None)

def test_valid_linkhttp_not_valid():
    with pytest.raises(HTTPException):
        handle_excep.valid_linkhttp_not_valid(400,"testing","some word not like http link")
    with pytest.raises(HTTPException):
        handle_excep.valid_linkhttp_not_valid(400,"testing","http//site.com")
    handle_excep.valid_linkhttp_not_valid(400,"testing","http://site.com.br")
    handle_excep.valid_linkhttp_not_valid(400,"testing","https://site.com.br")
    handle_excep.valid_linkhttp_not_valid(400,"testing","http://site.com.br/resource")
    handle_excep.valid_linkhttp_not_valid(400,"testing","https://site.com.br/resource")
    handle_excep.valid_linkhttp_not_valid(400,"testing","http://site.com.br/resource/")
    handle_excep.valid_linkhttp_not_valid(400,"testing","https://site.com.br/resource/")
    handle_excep.valid_linkhttp_not_valid(400,"testing","http://site.com.br/resource?TESTE=TESTE")
    handle_excep.valid_linkhttp_not_valid(400,"testing","https://site.com.br/resource?TESTE=TESTE")



