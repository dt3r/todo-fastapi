from sqlalchemy import text, insert
from database import sync_engine, session_factory
from models.models import metadata_object, TasksOrm

def create_tables():
    metadata_object.drop_all(sync_engine)
    metadata_object.create_all(sync_engine)

def insert_data():
    with session_factory() as session:
        task_1 = TasksOrm(task_name="testname1")
        task_2 = TasksOrm(task_name="testname2")
        session.add_all([task_1, task_2])
        session.commit()

