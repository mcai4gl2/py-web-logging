import pytest
from web.logging import create_app


@pytest.fixture
def app():
    app = create_app()
    return app.test_client()
