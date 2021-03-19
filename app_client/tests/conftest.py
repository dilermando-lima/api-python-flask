import pytest
from app_client.app import create_app

@pytest.fixture(scope="session")
def app():
    print("entrou no @pytest.fixture app")
    return create_app()