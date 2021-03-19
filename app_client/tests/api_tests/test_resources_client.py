

def test_app_is_created(app):
    assert app.name == "app_client.app"

def test_app_config_if_debub(app):
    assert app.config["DEBUG"]