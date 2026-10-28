from app.database import sync_engine, Base
from app.models.models import Task

def create_tables():
    Base.metadata.create_all(bind=sync_engine)
