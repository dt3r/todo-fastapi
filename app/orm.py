from app.database import sync_engine, Base


def create_tables():
    Base.metadata.create_all(bind=sync_engine)
