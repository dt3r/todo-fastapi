from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.orm import Mapped,  mapped_column
from database import Base


class TasksOrm(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    task_name: Mapped[str]


metadata_object = MetaData()





'''
tasks_table = Table(
    "tasks",
    metadata_object,
    Column("id", Integer, primary_key=True),
    Column("task_name", String(255))
)
'''