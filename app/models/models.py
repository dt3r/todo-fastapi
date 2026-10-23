from sqlalchemy import String, MetaData, Boolean
from sqlalchemy.orm import Mapped,  mapped_column
from database import Base


class Task(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    task_name: Mapped[str] = mapped_column(String(255))
    finished: Mapped[bool] = mapped_column(Boolean, default=False)


metadata_object = MetaData()



