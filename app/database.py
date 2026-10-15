from sqlalchemy import URL, create_engine, text, insert
from config import settings
from models.models import metadata_object, tasks_table

sync_engine = create_engine(
    url = settings.DATABASE_URL,
    echo=True,
    pool_size=5,
    max_overflow=10,

)

def create_tables():
    metadata_object.drop_all(sync_engine)
    metadata_object.create_all(sync_engine)

def insert_data():
    with sync_engine.connect() as conn:
        statement = insert(tasks_table).values(
            [
                {"task_name": "example_task"}
            ]
            )
        conn.execute(statement)
        conn.commit()

