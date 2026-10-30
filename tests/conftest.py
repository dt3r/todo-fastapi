import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from app.config import settings
from app.main import app
from app.database import Base, get_session
from app.models.models import Task

test_engine = create_engine(settings.TEST_DATABASE_URL)

test_session_factory = sessionmaker(bind=test_engine, autoflush=False, autocommit=False,)

@pytest.fixture()
def client():
    Base.metadata.create_all(bind=test_engine)

    def override_get_session():
        with test_session_factory() as session:
            yield session

    app.dependency_overrides[get_session] = override_get_session

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()
    Base.metadata.drop_all(bind=test_engine)