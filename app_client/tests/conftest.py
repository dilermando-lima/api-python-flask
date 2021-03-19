import pytest
from app_client.app import create_app

@pytest.fixture(scope="session")
def app():
    return create_app()

@pytest.fixture(scope="session")
def client():
    return create_app().test_client()

