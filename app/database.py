from sqlalchemy import URL, create_engine, text, insert
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from config import settings

sync_engine = create_engine(
    url = settings.DATABASE_URL,
    echo=True,
    pool_size=5,
    max_overflow=10,

)

session_factory = sessionmaker(sync_engine)

class Base(DeclarativeBase):
    pass



"""

OUTDATED

def insert_data():
    with sync_engine.connect() as conn:
        statement = insert(tasks_table).values(
            [
                {"task_name": "example_task"}
            ]
            )
        conn.execute(statement)
        conn.commit()
"""
