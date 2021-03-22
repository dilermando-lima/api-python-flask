import json

def test_app_is_created(app):
    assert app.name == "app_client.app"

def test_app_config_if_debub(app):
    assert app.config["DEBUG"]

def test_api_client_post(client):
    headers = { "Content-Type": "application/json"}    
    request_body = {
        "name" :"name_test",
        "email" : "teste"
    }
    response = client.post("/client", data=json.dumps(request_body) , headers=headers )
    assert response.status_code == 200
    assert response.json["name"] == request_body["name"]
    assert response.json["email"] == request_body["email"]

def test_api_client_get(client):
    headers = { "Content-Type": "application/json"}
    response = client.get("/client", headers=headers )
    assert response.status_code == 200
    assert response.json[0]["name"] == "name_test"



 